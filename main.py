#!/usr/bin/env python3
"""
Claude Code Extensions Manager - Simple CLI for managing Claude Code extensions
"""

import os
import shutil
import sys
import yaml
from pathlib import Path
from typing import Optional, List, Tuple, Dict, Any

import typer
import questionary
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from typing import Optional
from rich.text import Text

__version__ = "1.0.0"

app = typer.Typer(
    name="claude-ext",
    help="Manage Claude Code extensions",
    add_completion=False,
)
console = Console()

# Create subcommands for agent, command, and workflow
agent_app = typer.Typer(help="Manage Claude Code agents")
command_app = typer.Typer(help="Manage Claude Code commands")
workflow_app = typer.Typer(help="Manage Claude Code workflows")

app.add_typer(agent_app, name="agent")
app.add_typer(command_app, name="command")
app.add_typer(workflow_app, name="workflow")


def get_claude_dir(project_path: Optional[Path] = None) -> Path:
    """Get the .claude directory path."""
    if project_path:
        return Path(project_path) / ".claude"
    else:
        # User level if no project specified
        return Path.home() / ".claude"


def get_extensions_dir() -> Path:
    """Get the extensions directory in the current package."""
    return Path(__file__).parent / "extensions"


def get_claude_projects() -> List[Tuple[str, Path]]:
    """Get list of available Claude projects.

    Returns:
        List of tuples containing (friendly_name, full_path)
    """
    projects_dir = Path.home() / ".claude" / "projects"
    if not projects_dir.exists():
        return []

    projects = []
    for project_dir in projects_dir.iterdir():
        if project_dir.is_dir():
            # The directory name format is path components separated by hyphens
            # e.g., "-Users-chris-cheng-projects-chris-my-awesome-claude-code"
            # Challenge: both path separators AND hyphens in names become hyphens
            encoded_name = project_dir.name

            # Remove leading hyphen if present
            if encoded_name.startswith("-"):
                encoded_name = encoded_name[1:]

            # Try multiple reconstruction strategies to find the actual path
            # This is necessary because hyphens in project names are indistinguishable
            # from path separator hyphens in the encoding
            parts = encoded_name.split("-")

            # Strategy: We know it starts with Users/username on macOS
            # Try to find a valid path by testing different combinations
            if parts[0] == "Users" and len(parts) > 2:
                home_path = Path.home()
                home_parts = str(home_path).split("/")

                if len(home_parts) > 2:
                    actual_username = home_parts[2]
                    username_dot_parts = actual_username.split(".")

                    # Find where the username ends in the parts list
                    username_end_idx = len(username_dot_parts) + 1  # +1 for "Users"

                    # Start with base path
                    base_path = Path("/Users") / actual_username

                    # Now we have the remaining parts after the username
                    remaining = parts[username_end_idx:]

                    # Try to find valid paths by testing different combinations
                    # Start from the end and work backwards, joining with hyphens
                    found_path = None

                    # Try different split points to handle hyphenated directory names
                    for i in range(len(remaining), 0, -1):
                        # Try treating the last i parts as a single hyphenated name
                        if i == len(remaining):
                            # All parts separate
                            test_path = base_path
                            for part in remaining:
                                if part:  # Skip empty parts
                                    test_path = test_path / part
                        else:
                            # Join the last (len(remaining) - i + 1) parts with hyphens
                            test_path = base_path
                            # Add the first parts as separate directories
                            for j in range(i - 1):
                                if remaining[j]:
                                    test_path = test_path / remaining[j]
                            # Join the remaining parts with hyphens as a single directory
                            if i - 1 < len(remaining):
                                hyphenated = "-".join(remaining[i-1:])
                                if hyphenated:
                                    test_path = test_path / hyphenated

                        if test_path.exists() and test_path.is_dir():
                            found_path = test_path
                            break

                    if found_path:
                        actual_path = found_path
                    else:
                        # Fallback: try the most likely pattern
                        # (projects folder usually comes after username)
                        actual_path = base_path
                        for part in remaining:
                            if part:
                                actual_path = actual_path / part
                else:
                    # Fallback to simple join
                    actual_path = Path("/" + "/".join(parts))
            else:
                # For non-macOS or unrecognized patterns
                actual_path = Path("/" + "/".join(parts))

            # Only add if the path exists
            if actual_path.exists() and actual_path.is_dir():
                # Get a friendly project name from the last few meaningful parts
                path_str = str(actual_path)
                path_parts = path_str.split("/")

                # Find the project name - usually the last component or last few
                if "projects" in path_parts:
                    idx = path_parts.index("projects")
                    if idx < len(path_parts) - 1:
                        # Get everything after "projects" as the project identifier
                        project_parts = path_parts[idx+1:]
                        project_name = "/".join(project_parts)
                    else:
                        project_name = path_parts[-1] if path_parts else "unknown"
                else:
                    project_name = path_parts[-1] if path_parts else "unknown"

                projects.append((project_name, actual_path))

    return sorted(projects, key=lambda x: x[0].lower())


def list_available(ext_type: str):
    """List available extensions of given type."""
    extensions_dir = get_extensions_dir()
    type_dir = extensions_dir / f"{ext_type}s"

    if not type_dir.exists():
        return []

    results = []
    for item in type_dir.iterdir():
        if ext_type == "workflow":
            # Workflows use YAML files
            if item.is_file() and item.suffix in ['.yaml', '.yml']:
                results.append(item.stem)
        else:
            # Agents and commands use MD files
            if item.is_file() and item.suffix == '.md':
                results.append(item.stem)

    return results


def list_installed(ext_type: str, project_path: Optional[Path] = None):
    """List installed extensions of given type."""
    claude_dir = get_claude_dir(project_path)
    type_dir = claude_dir / f"{ext_type}s"

    if not type_dir.exists():
        return []

    results = []
    for item in type_dir.iterdir():
        if item.is_file() and item.suffix == '.md':
            # Remove .md extension from name
            results.append((item.stem, str(item)))

    return results


def check_extension_exists(
    ext_type: str,
    name: str,
    project_path: Optional[Path] = None
) -> bool:
    """Check if an extension is already installed."""
    claude_dir = get_claude_dir(project_path)
    target_file = claude_dir / f"{ext_type}s" / f"{name}.md"
    return target_file.exists()


def install_extension(
    ext_type: str,
    name: str,
    project_path: Optional[Path] = None,
    force: bool = False
):
    """Install an extension."""
    # Source path - look for .md file
    extensions_dir = get_extensions_dir()
    source_file = extensions_dir / f"{ext_type}s" / f"{name}.md"

    if not source_file.exists():
        console.print(f"[red]❌ {ext_type.capitalize()} '{name}' not found[/red]")
        console.print(f"[dim]Run 'claude-ext {ext_type} list' to see available {ext_type}s[/dim]")
        raise typer.Exit(1)

    # Target path - also .md file
    claude_dir = get_claude_dir(project_path)
    target_file = claude_dir / f"{ext_type}s" / f"{name}.md"

    # Check if already exists
    if target_file.exists() and not force:
        console.print(f"[yellow]⚠️  {ext_type.capitalize()} '{name}' already installed[/yellow]")
        console.print("[dim]Use --force to overwrite[/dim]")
        raise typer.Exit(1)

    # Create directory structure
    target_file.parent.mkdir(parents=True, exist_ok=True)

    # Copy file
    shutil.copy2(source_file, target_file)

    level = "project" if project_path else "user"
    console.print(f"[green]✅ Installed {ext_type} '{name}' to {level} level[/green]")
    console.print(f"[dim]📍 Location: {target_file}[/dim]")


def uninstall_extension(
    ext_type: str,
    name: str,
    project_path: Optional[Path] = None
):
    """Uninstall an extension."""
    claude_dir = get_claude_dir(project_path)
    target_file = claude_dir / f"{ext_type}s" / f"{name}.md"

    if not target_file.exists():
        level = "project" if project_path else "user"
        console.print(f"[red]❌ {ext_type.capitalize()} '{name}' not found at {level} level[/red]")
        raise typer.Exit(1)

    target_file.unlink()  # Remove the .md file
    console.print(f"[green]✅ Uninstalled {ext_type} '{name}'[/green]")


# Agent commands
@agent_app.command("list")
def agent_list(
    installed: bool = typer.Option(False, "--installed", "-i", help="Show installed agents"),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help="Project path"),
):
    """List available or installed agents."""

    if installed:
        agents = list_installed("agent", project)
        if not agents:
            level = "project" if project else "user"
            console.print(f"[yellow]No agents installed at {level} level[/yellow]")
            return

        table = Table(title=f"Installed Agents ({'project' if project else 'user'} level)")
        table.add_column("Name", style="green")
        table.add_column("Location", style="dim")

        for name, location in agents:
            table.add_row(name, location)

        console.print(table)
    else:
        agents = list_available("agent")
        if not agents:
            console.print("[yellow]No agents available[/yellow]")
            return

        table = Table(title="Available Agents")
        table.add_column("Name", style="green")

        for name in sorted(agents):
            table.add_row(name)

        console.print(table)
        console.print("\n[dim]Install with: claude-ext agent install <name>[/dim]")


@agent_app.command("install")
def agent_install(
    names: List[str] = typer.Argument(None, help="Agent name(s) to install (space-separated for multiple)"),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help="Project path (if not specified, installs to user level)"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite if exists"),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="Interactive multi-select mode"),
):
    """Install Claude Code agents."""
    if interactive or not names:
        # Interactive mode
        extensions = list_available("agent")
        if not extensions:
            console.print("[yellow]No agents available to install[/yellow]")
            raise typer.Exit()

        selected = multi_select(
            sorted(extensions),
            title="Select agents to install",
            instructions="↑↓ Navigate | SPACE Select/Deselect | A Select All | ENTER Confirm | Q Quit"
        )

        if not selected:
            console.print("[yellow]No agents selected[/yellow]")
            raise typer.Exit()

        successful, failed = install_multiple_extensions("agent", selected, project, force)

        # Summary
        if successful:
            console.print(f"\n[green]✅ Successfully installed {len(successful)} agent(s)[/green]")
        if failed:
            console.print(f"[red]❌ Failed to install {len(failed)} agent(s)[/red]")

    elif len(names) == 1:
        # Single installation
        install_extension("agent", names[0], project, force)

    else:
        # Multiple installation
        successful, failed = install_multiple_extensions("agent", names, project, force)

        # Summary
        if successful:
            console.print(f"\n[green]✅ Successfully installed {len(successful)} agent(s)[/green]")
        if failed:
            console.print(f"[red]❌ Failed to install {len(failed)} agent(s)[/red]")


@agent_app.command("uninstall")
def agent_uninstall(
    name: str = typer.Argument(..., help="Agent name to uninstall"),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help="Project path (if not specified, uninstalls from user level)"),
):
    """Uninstall a Claude Code agent."""
    uninstall_extension("agent", name, project)


# Command commands
@command_app.command("list")
def command_list(
    installed: bool = typer.Option(False, "--installed", "-i", help="Show installed commands"),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help="Project path"),
):
    """List available or installed commands."""

    if installed:
        commands = list_installed("command", project)
        if not commands:
            level = "project" if project else "user"
            console.print(f"[yellow]No commands installed at {level} level[/yellow]")
            return

        table = Table(title=f"Installed Commands ({'project' if project else 'user'} level)")
        table.add_column("Name", style="green")
        table.add_column("Location", style="dim")

        for name, location in commands:
            table.add_row(name, location)

        console.print(table)
    else:
        commands = list_available("command")
        if not commands:
            console.print("[yellow]No commands available[/yellow]")
            return

        table = Table(title="Available Commands")
        table.add_column("Name", style="green")

        for name in sorted(commands):
            table.add_row(name)

        console.print(table)
        console.print("\n[dim]Install with: claude-ext command install <name>[/dim]")


@command_app.command("install")
def command_install(
    names: List[str] = typer.Argument(None, help="Command name(s) to install (space-separated for multiple)"),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help="Project path (if not specified, installs to user level)"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite if exists"),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="Interactive multi-select mode"),
):
    """Install Claude Code commands."""
    if interactive or not names:
        # Interactive mode
        extensions = list_available("command")
        if not extensions:
            console.print("[yellow]No commands available to install[/yellow]")
            raise typer.Exit()

        selected = multi_select(
            sorted(extensions),
            title="Select commands to install",
            instructions="↑↓ Navigate | SPACE Select/Deselect | A Select All | ENTER Confirm | Q Quit"
        )

        if not selected:
            console.print("[yellow]No commands selected[/yellow]")
            raise typer.Exit()

        successful, failed = install_multiple_extensions("command", selected, project, force)

        # Summary
        if successful:
            console.print(f"\n[green]✅ Successfully installed {len(successful)} command(s)[/green]")
        if failed:
            console.print(f"[red]❌ Failed to install {len(failed)} command(s)[/red]")

    elif len(names) == 1:
        # Single installation
        install_extension("command", names[0], project, force)

    else:
        # Multiple installation
        successful, failed = install_multiple_extensions("command", names, project, force)

        # Summary
        if successful:
            console.print(f"\n[green]✅ Successfully installed {len(successful)} command(s)[/green]")
        if failed:
            console.print(f"[red]❌ Failed to install {len(failed)} command(s)[/red]")


@command_app.command("uninstall")
def command_uninstall(
    name: str = typer.Argument(..., help="Command name to uninstall"),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help="Project path (if not specified, uninstalls from user level)"),
):
    """Uninstall a Claude Code command."""
    uninstall_extension("command", name, project)


@app.command()
def list_projects():
    """List available Claude projects."""
    projects = get_claude_projects()

    if not projects:
        console.print("[yellow]No Claude projects found[/yellow]")
        console.print("[dim]Projects are created when you use Claude Code in a directory[/dim]")
        return

    table = Table(title="Available Claude Projects")
    table.add_column("Project Name", style="green")
    table.add_column("Path", style="dim")

    for name, path in projects:
        table.add_row(name, str(path))

    console.print(table)
    console.print("\n[dim]Use --project <path> to install to a specific project[/dim]")


@app.command()
def interactive():
    """Interactive mode for managing extensions"""
    console.print("[bold cyan]Claude Code Extensions Manager - Interactive Mode[/bold cyan]\n")

    # Choose extension type using select
    ext_type = single_select(
        ["workflow", "agent", "command", "quit"],
        title="What would you like to manage?",
        default_index=0
    )

    if ext_type == "quit":
        console.print("[yellow]Goodbye![/yellow]")
        raise typer.Exit()

    # Choose action using select
    if ext_type == "workflow":
        actions = ["list", "install", "info", "quit"]
    else:
        actions = ["list", "install", "uninstall", "quit"]

    action = single_select(
        actions,
        title=f"What would you like to do with {ext_type}s?",
        default_index=0
    )

    if action == "quit":
        console.print("[yellow]Goodbye![/yellow]")
        raise typer.Exit()

    # Execute action
    if action == "list":
        # Ask if listing available or installed using select
        list_type = single_select(
            ["available", "installed"],
            title="List which extensions?",
            default_index=0
        )

        if list_type == "available":
            extensions = list_available(ext_type)
            if not extensions:
                console.print(f"[yellow]No {ext_type}s available[/yellow]")
            else:
                console.print(f"\n[bold]Available {ext_type.capitalize()}s:[/bold]")
                for i, name in enumerate(sorted(extensions), 1):
                    console.print(f"  {i}. [green]{name}[/green]")
        else:
            # Ask for level using select
            level = single_select(
                ["user-level (~/.claude)", "project-level"],
                title="Which level?",
                default_index=0
            )
            if level == "user-level (~/.claude)":
                project = None
            else:
                # Get available Claude projects
                claude_projects = get_claude_projects()

                # Build project choices
                project_choices = []
                if claude_projects:
                    project_choices.append("--- Claude Projects ---")
                    for name, _ in claude_projects:
                        project_choices.append(f"  📁 {name}")
                    project_choices.append("--- Other Locations ---")

                project_choices.extend([
                    "current directory (.)",
                    "parent directory (..)",
                    "enter custom path"
                ])

                project_choice = single_select(
                    project_choices,
                    title="Select project location",
                    default_index=0 if not claude_projects else len(claude_projects) + 2
                )

                # Parse the selection
                project = None  # Initialize to avoid UnboundLocalError
                if project_choice.startswith("  📁 "):
                    # It's a Claude project
                    selected_name = project_choice[5:]  # Remove "  📁 " prefix
                    # Find the matching project
                    for name, path in claude_projects:
                        if name == selected_name:
                            project = path
                            break
                    if project is None:
                        console.print(f"[red]Error: Could not find project '{selected_name}'[/red]")
                        raise typer.Exit()
                elif project_choice == "current directory (.)":
                    project = Path(".")
                elif project_choice == "parent directory (..)":
                    project = Path("..")
                elif project_choice in ["--- Claude Projects ---", "--- Other Locations ---"]:
                    # User selected a separator, treat as cancelled
                    console.print("[yellow]Operation cancelled[/yellow]")
                    raise typer.Exit()
                else:
                    project = Path(Prompt.ask("Enter project path", default="."))

            installed = list_installed(ext_type, project)
            if not installed:
                level = "user" if project is None else "project"
                console.print(f"[yellow]No {ext_type}s installed at {level} level[/yellow]")
            else:
                console.print(f"\n[bold]Installed {ext_type.capitalize()}s:[/bold]")
                for name, location in installed:
                    console.print(f"  • [green]{name}[/green] ({location})")

    elif action == "info" and ext_type == "workflow":
        # Show workflow info
        workflows = list_available("workflow")
        if not workflows:
            console.print("[yellow]No workflows available[/yellow]")
            raise typer.Exit()

        selected = single_select(
            sorted(workflows),
            title="Select workflow to get info about",
            default_index=0
        )
        if selected:
            workflow_info(selected)

    elif action == "install":
        # Show available extensions
        extensions = list_available(ext_type)
        if not extensions:
            console.print(f"[yellow]No {ext_type}s available to install[/yellow]")
            raise typer.Exit()

        # Determine selection mode intelligently
        if ext_type == "workflow":
            # Workflows are always single selection
            mode = "single"
        elif len(extensions) <= 3:
            # For small lists, default to single selection
            mode = "single"
        else:
            # For larger lists, ask user preference
            mode = single_select(
                ["multiple (select many)", "single (select one)"],
                title="Selection mode?",
                default_index=0
            )
            mode = "multiple" if "multiple" in mode else "single"

        if mode == "multiple":
            # Multi-select mode
            selected_items = multi_select(
                sorted(extensions),
                title=f"Select {ext_type}s to install (SPACE to select, ENTER to confirm)",
                instructions="↑↓ Navigate | SPACE Select/Deselect | A Select All | ENTER Confirm | Q Quit"
            )

            if not selected_items:
                console.print("[yellow]No items selected[/yellow]")
                raise typer.Exit()

            # Choose installation level
            console.print(f"\n[cyan]Selected {len(selected_items)} {ext_type}(s) for installation[/cyan]")
            for item in selected_items:
                console.print(f"  • {item}")

            # Choose installation level using select
            level = single_select(
                ["user-level (~/.claude)", "project-level"],
                title="Where to install?",
                default_index=0
            )
            if level == "user-level (~/.claude)":
                project = None
                console.print("[dim]Installing to user level (~/.claude)[/dim]")
            else:
                # Get available Claude projects
                claude_projects = get_claude_projects()

                # Build project choices
                project_choices = []
                if claude_projects:
                    project_choices.append("--- Claude Projects ---")
                    for name, _ in claude_projects:
                        project_choices.append(f"  📁 {name}")
                    project_choices.append("--- Other Locations ---")

                project_choices.extend([
                    "current directory (.)",
                    "parent directory (..)",
                    "enter custom path"
                ])

                project_choice = single_select(
                    project_choices,
                    title="Select project location",
                    default_index=0 if not claude_projects else len(claude_projects) + 2
                )

                # Parse the selection
                project = None  # Initialize to avoid UnboundLocalError
                if project_choice.startswith("  📁 "):
                    # It's a Claude project
                    selected_name = project_choice[5:]  # Remove "  📁 " prefix
                    # Find the matching project
                    for name, path in claude_projects:
                        if name == selected_name:
                            project = path
                            break
                    if project is None:
                        console.print(f"[red]Error: Could not find project '{selected_name}'[/red]")
                        raise typer.Exit()
                elif project_choice == "current directory (.)":
                    project = Path(".")
                elif project_choice == "parent directory (..)":
                    project = Path("..")
                elif project_choice in ["--- Claude Projects ---", "--- Other Locations ---"]:
                    # User selected a separator, treat as cancelled
                    console.print("[yellow]Installation cancelled[/yellow]")
                    raise typer.Exit()
                else:
                    project = Path(Prompt.ask("Enter project path", default="."))

                console.print(f"[dim]Installing to project: {project}[/dim]")

            # Check for existing installations
            existing_items = []
            for item in selected_items:
                if check_extension_exists(ext_type, item, project):
                    existing_items.append(item)

            if existing_items:
                level_str = "project" if project else "user"
                console.print(f"\n[yellow]⚠️  The following items are already installed at {level_str} level:[/yellow]")
                for item in existing_items:
                    console.print(f"  • {item}")

                overwrite_choice = single_select(
                    ["Overwrite all existing", "Skip existing", "Cancel installation"],
                    title="What would you like to do?",
                    default_index=1
                )

                if overwrite_choice == "Cancel installation":
                    console.print("[yellow]Installation cancelled[/yellow]")
                    raise typer.Exit()
                elif overwrite_choice == "Skip existing":
                    # Remove existing items from selection
                    selected_items = [item for item in selected_items if item not in existing_items]
                    if not selected_items:
                        console.print("[yellow]No new items to install[/yellow]")
                        raise typer.Exit()
                    force = False
                else:  # Overwrite all existing
                    force = True
            else:
                force = False

            # Confirm using select
            confirm = single_select(
                ["Yes, proceed", "No, cancel"],
                title=f"Proceed with installation of {len(selected_items)} {ext_type}(s)?",
                default_index=0
            )
            if confirm == "Yes, proceed":
                successful, failed = install_multiple_extensions(ext_type, selected_items, project, force)

                # Summary
                console.print(f"\n[bold]Installation Summary:[/bold]")
                if successful:
                    console.print(f"[green]✅ Successfully installed: {len(successful)} {ext_type}(s)[/green]")
                if failed:
                    console.print(f"[red]❌ Failed: {len(failed)} {ext_type}(s)[/red]")
            else:
                console.print("[yellow]Installation cancelled[/yellow]")

        else:
            # Single selection mode using select
            selected = single_select(
                sorted(extensions),
                title=f"Select {ext_type} to install",
                default_index=0
            )
            if not selected:
                console.print("[yellow]Cancelled[/yellow]")
                raise typer.Exit()

            # Choose installation level using select
            level = single_select(
                ["user-level (~/.claude)", "project-level"],
                title=f"Where to install '{selected}'?",
                default_index=0
            )
            if level == "user-level (~/.claude)":
                project = None
                console.print("[dim]Installing to user level (~/.claude)[/dim]")
            else:
                # Get available Claude projects
                claude_projects = get_claude_projects()

                # Build project choices
                project_choices = []
                if claude_projects:
                    project_choices.append("--- Claude Projects ---")
                    for name, _ in claude_projects:
                        project_choices.append(f"  📁 {name}")
                    project_choices.append("--- Other Locations ---")

                project_choices.extend([
                    "current directory (.)",
                    "parent directory (..)",
                    "enter custom path"
                ])

                project_choice = single_select(
                    project_choices,
                    title="Select project location",
                    default_index=0 if not claude_projects else len(claude_projects) + 2
                )

                # Parse the selection
                project = None  # Initialize to avoid UnboundLocalError
                if project_choice.startswith("  📁 "):
                    # It's a Claude project
                    selected_name = project_choice[5:]  # Remove "  📁 " prefix
                    # Find the matching project
                    for name, path in claude_projects:
                        if name == selected_name:
                            project = path
                            break
                    if project is None:
                        console.print(f"[red]Error: Could not find project '{selected_name}'[/red]")
                        raise typer.Exit()
                elif project_choice == "current directory (.)":
                    project = Path(".")
                elif project_choice == "parent directory (..)":
                    project = Path("..")
                elif project_choice in ["--- Claude Projects ---", "--- Other Locations ---"]:
                    # User selected a separator, treat as cancelled
                    console.print("[yellow]Installation cancelled[/yellow]")
                    raise typer.Exit()
                else:
                    project = Path(Prompt.ask("Enter project path", default="."))

                console.print(f"[dim]Installing to project: {project}[/dim]")

            # Check if extension already exists
            already_exists = False
            force_install = False

            if ext_type != "workflow":
                already_exists = check_extension_exists(ext_type, selected, project)
                if already_exists:
                    level_str = "project" if project else "user"
                    console.print(f"\n[yellow]⚠️  '{selected}' is already installed at {level_str} level[/yellow]")

                    overwrite_choice = single_select(
                        ["Overwrite existing", "Cancel installation"],
                        title="What would you like to do?",
                        default_index=0
                    )

                    if overwrite_choice == "Cancel installation":
                        console.print("[yellow]Installation cancelled[/yellow]")
                        raise typer.Exit()
                    else:
                        force_install = True
                        console.print("[dim]Will overwrite existing installation...[/dim]")

            # Confirm installation if not already handled
            if not already_exists:
                confirm = single_select(
                    ["Yes, proceed", "No, cancel"],
                    title="Proceed with installation?",
                    default_index=0
                )
                if confirm != "Yes, proceed":
                    console.print("[yellow]Installation cancelled[/yellow]")
                    raise typer.Exit()

            # Proceed with installation
            if ext_type == "workflow":
                # Install workflow
                success, components = install_workflow(selected, project, force=force_install)
                if not success and not components:
                    console.print(f"[red]❌ Failed to install workflow '{selected}'[/red]")
            else:
                # Install single extension
                try:
                    install_extension(ext_type, selected, project, force=force_install)
                    if force_install:
                        console.print(f"[green]✅ Successfully installed '{selected}' (overwritten)![/green]")
                    else:
                        console.print(f"[green]✅ Successfully installed '{selected}'![/green]")
                except typer.Exit:
                    pass  # Error already displayed

    elif action == "uninstall":
        # Choose level first using select
        level = single_select(
            ["user-level (~/.claude)", "project-level"],
            title="Uninstall from which level?",
            default_index=0
        )
        if level == "user-level (~/.claude)":
            project = None
        else:
            # Get available Claude projects
            claude_projects = get_claude_projects()

            # Build project choices
            project_choices = []
            if claude_projects:
                project_choices.append("--- Claude Projects ---")
                for name, _ in claude_projects:
                    project_choices.append(f"  📁 {name}")
                project_choices.append("--- Other Locations ---")

            project_choices.extend([
                "current directory (.)",
                "parent directory (..)",
                "enter custom path"
            ])

            project_choice = single_select(
                project_choices,
                title="Select project location",
                default_index=0 if not claude_projects else len(claude_projects) + 2
            )

            # Parse the selection
            project = None  # Initialize to avoid UnboundLocalError
            if project_choice.startswith("  📁 "):
                # It's a Claude project
                selected_name = project_choice[5:]  # Remove "  📁 " prefix
                # Find the matching project
                for name, path in claude_projects:
                    if name == selected_name:
                        project = path
                        break
                if project is None:
                    console.print(f"[red]Error: Could not find project '{selected_name}'[/red]")
                    raise typer.Exit()
            elif project_choice == "current directory (.)":
                project = Path(".")
            elif project_choice == "parent directory (..)":
                project = Path("..")
            elif project_choice in ["--- Claude Projects ---", "--- Other Locations ---"]:
                # User selected a separator, treat as cancelled
                console.print("[yellow]Operation cancelled[/yellow]")
                raise typer.Exit()
            else:
                project = Path(Prompt.ask("Enter project path", default="."))

        # Show installed extensions
        installed = list_installed(ext_type, project)
        if not installed:
            level = "user" if project is None else "project"
            console.print(f"[yellow]No {ext_type}s installed at {level} level[/yellow]")
            raise typer.Exit()

        console.print(f"\n[bold]Installed {ext_type.capitalize()}s:[/bold]")
        for i, (name, location) in enumerate(installed, 1):
            console.print(f"  {i}. [green]{name}[/green]")

        # Select extension to uninstall using select
        installed_names = [name for name, _ in installed]
        selected = single_select(
            installed_names,
            title="Select extension to uninstall",
            default_index=0
        )
        if not selected:
            console.print("[yellow]Cancelled[/yellow]")
            raise typer.Exit()

        # Confirm using select
        confirm = single_select(
            ["Yes, uninstall", "No, cancel"],
            title=f"Uninstall '{selected}'?",
            default_index=1  # Default to "No" for safety
        )
        if confirm == "Yes, uninstall":
            try:
                uninstall_extension(ext_type, selected, project)
                console.print(f"[green]✅ Successfully uninstalled '{selected}'![/green]")
            except typer.Exit:
                pass  # Error already displayed
        else:
            console.print("[yellow]Uninstall cancelled[/yellow]")

    # Ask if user wants to continue using select
    continue_choice = single_select(
        ["Yes, continue", "No, exit"],
        title="Continue with another operation?",
        default_index=0
    )
    if continue_choice == "Yes, continue":
        interactive()  # Recursive call to continue


# Workflow commands
@workflow_app.command("list")
def workflow_list(
    installed: bool = typer.Option(False, "--installed", "-i", help="Show installed workflows"),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help="Project path"),
):
    """List available workflows."""

    if installed:
        console.print("[yellow]Installed workflows cannot be tracked directly.[/yellow]")
        console.print("[dim]Check installed agents and commands instead.[/dim]")
        return

    workflows = list_available("workflow")
    if not workflows:
        console.print("[yellow]No workflows available[/yellow]")
        return

    table = Table(title="Available Workflows")
    table.add_column("Name", style="green")
    table.add_column("Description", style="dim")

    for name in sorted(workflows):
        workflow_def = load_workflow_definition(name)
        if workflow_def:
            desc = workflow_def.get('description', 'No description')
            table.add_row(name, desc)
        else:
            table.add_row(name, "No description")

    console.print(table)
    console.print("\n[dim]Install with: claude-ext workflow install <name>[/dim]")


@workflow_app.command("install")
def workflow_install(
    name: str = typer.Argument(..., help="Workflow name to install"),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help="Project path (auto-detect from workflow if not specified)"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite existing components"),
):
    """Install a Claude Code workflow (command + agents)."""
    success, components = install_workflow(name, project, force)
    if not success and not components:
        raise typer.Exit(1)


@workflow_app.command("info")
def workflow_info(
    name: str = typer.Argument(..., help="Workflow name to get info about"),
):
    """Show detailed information about a workflow."""
    workflow_def = load_workflow_definition(name)
    if not workflow_def:
        console.print(f"[red]❌ Workflow '{name}' not found[/red]")
        raise typer.Exit(1)

    console.print(f"\n[bold cyan]Workflow: {name}[/bold cyan]")
    console.print(f"[dim]{workflow_def.get('description', 'No description')}[/dim]\n")

    console.print(f"[bold]Level:[/bold] {workflow_def.get('level', 'project')}")
    console.print(f"[bold]Complexity:[/bold] {workflow_def.get('complexity', 'N/A')}/10\n")

    # Main command
    if 'command' in workflow_def:
        cmd = workflow_def['command']
        console.print(f"[bold]Main Command:[/bold]")
        console.print(f"  • /{cmd['name']} - {cmd.get('description', 'No description')}")
        if 'thinking_level' in cmd:
            console.print(f"    [dim]Thinking: {cmd['thinking_level']}[/dim]")

    # Agents
    if 'agents' in workflow_def:
        console.print(f"\n[bold]Agents ({len(workflow_def['agents'])}):[/bold]")
        for agent in workflow_def['agents']:
            console.print(f"  • @{agent['name']} - {agent.get('description', 'No description')}")
            if 'thinking_level' in agent:
                console.print(f"    [dim]Thinking: {agent['thinking_level']}[/dim]")

    # Helper commands
    if 'helper_commands' in workflow_def:
        console.print(f"\n[bold]Helper Commands ({len(workflow_def['helper_commands'])}):[/bold]")
        for cmd in workflow_def['helper_commands']:
            console.print(f"  • /{cmd['name']} - {cmd.get('description', 'No description')}")
            if 'thinking_level' in cmd:
                console.print(f"    [dim]Thinking: {cmd['thinking_level']}[/dim]")


def single_select(
    items: List[str],
    title: str = "Select an option",
    default_index: int = 0
) -> str:
    """Interactive single-select using questionary for better arrow key support."""
    try:
        # Use questionary for better terminal compatibility
        result = questionary.select(
            title,
            choices=items,
            default=items[default_index] if items else None
        ).ask()
        return result if result else ""
    except (KeyboardInterrupt, EOFError):
        return ""
    except:
        # Fallback to numbered selection if questionary fails
        return _single_select_numbered(items, title, default_index)


# Removed _single_select_interactive as we're using questionary now


def _single_select_numbered(
    items: List[str],
    title: str,
    default_index: int = 0
) -> str:
    """Fallback single-select using numbered choices."""
    console.print(f"[bold cyan]{title}[/bold cyan]\n")

    # Display items with numbers
    for i, item in enumerate(items, 1):
        if i - 1 == default_index:
            console.print(f"  {i}. [green]{item} (default)[/green]")
        else:
            console.print(f"  {i}. {item}")

    console.print("\n[dim]Enter number to select, or press ENTER for default[/dim]")

    while True:
        choice = Prompt.ask("Selection", default=str(default_index + 1)).strip()

        if choice.lower() == 'q':  # Quit
            return ""

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(items):
                return items[idx]
            else:
                console.print("[red]Invalid selection[/red]")
        except ValueError:
            console.print("[red]Please enter a number[/red]")


def multi_select(
    items: List[str],
    title: str = "Select items",
    instructions: str = "Use arrow keys to navigate, space to select"
) -> List[str]:
    """Interactive multi-select using questionary for better arrow key support."""
    try:
        # Use questionary for better terminal compatibility
        result = questionary.checkbox(
            title,
            choices=items
        ).ask()
        return result if result else []
    except (KeyboardInterrupt, EOFError):
        return []
    except:
        # Fallback to numbered selection if questionary fails
        return _multi_select_numbered(items, title)


# Removed _multi_select_interactive as we're using questionary now


def _multi_select_numbered(
    items: List[str],
    title: str
) -> List[str]:
    """Fallback multi-select using numbered choices."""
    selected = set()

    while True:
        console.clear()
        console.print(f"[bold cyan]{title}[/bold cyan]\n")

        # Display items with numbers
        for i, item in enumerate(items, 1):
            prefix = "[✓]" if item in selected else "[ ]"
            if item in selected:
                console.print(f"  {i:2}. [green]{prefix}[/green] {item}")
            else:
                console.print(f"  {i:2}. {prefix} {item}")

        # Display selected count
        if selected:
            console.print(f"\n[green]Selected: {len(selected)} item(s)[/green]")

        console.print("\n[dim]Enter numbers (space-separated) to toggle, 'a' for all, 'n' for none, 'c' to confirm, 'q' to quit[/dim]")

        choice = Prompt.ask("Selection").strip().lower()

        if choice == 'c':  # Confirm
            break
        elif choice == 'q':  # Quit
            selected = set()
            break
        elif choice == 'a':  # Select all
            selected = set(items)
        elif choice == 'n':  # Select none
            selected.clear()
        else:
            # Parse numbers
            try:
                numbers = [int(x) for x in choice.split()]
                for num in numbers:
                    if 1 <= num <= len(items):
                        item = items[num - 1]
                        if item in selected:
                            selected.remove(item)
                        else:
                            selected.add(item)
            except (ValueError, IndexError):
                pass  # Ignore invalid input

    return list(selected)


def load_workflow_definition(workflow_name: str) -> Dict[str, Any]:
    """Load workflow definition from YAML file."""
    extensions_dir = get_extensions_dir()

    # Try both .yaml and .yml extensions
    for ext in ['.yaml', '.yml']:
        workflow_file = extensions_dir / "workflows" / f"{workflow_name}{ext}"
        if workflow_file.exists():
            with open(workflow_file, 'r') as f:
                return yaml.safe_load(f)

    return None


def install_workflow(
    name: str,
    project_path: Optional[Path] = None,
    force: bool = False
) -> Tuple[bool, List[str]]:
    """Install a workflow (command + agents).

    Returns:
        Tuple of (success, list_of_installed_components)
    """
    # Load workflow definition
    workflow_def = load_workflow_definition(name)
    if not workflow_def:
        console.print(f"[red]❌ Workflow '{name}' not found[/red]")
        return False, []

    # Determine installation level
    if workflow_def.get('level') == 'user':
        # User-level workflow
        target_path = None
        level_str = "user"
    else:
        # Project-level workflow
        target_path = project_path
        level_str = "project"

    installed_components = []
    all_success = True

    console.print(f"\n[bold cyan]Installing '{name}' workflow ({level_str} level)...[/bold cyan]")
    console.print(f"[dim]{workflow_def.get('description', 'No description')}[/dim]\n")

    # Install main command
    if 'command' in workflow_def:
        cmd = workflow_def['command']
        console.print(f"[bold]Main Command:[/bold]")

        # Check if corresponding .md file exists
        cmd_source = get_extensions_dir() / "commands" / f"{cmd['name']}.md"
        if cmd_source.exists():
            try:
                install_extension("command", cmd['name'], target_path, force)
                installed_components.append(f"command:{cmd['name']}")
            except:
                console.print(f"  [yellow]⚠️  Command '{cmd['name']}' already installed or failed[/yellow]")
                all_success = False
        else:
            console.print(f"  [yellow]⚠️  Command file '{cmd['name']}.md' not found[/yellow]")

    # Install agents
    if 'agents' in workflow_def:
        console.print(f"\n[bold]Agents ({len(workflow_def['agents'])}):[/bold]")
        for agent in workflow_def['agents']:
            # Check if corresponding .md file exists
            agent_source = get_extensions_dir() / "agents" / f"{agent['name']}.md"
            if agent_source.exists():
                try:
                    install_extension("agent", agent['name'], target_path, force)
                    installed_components.append(f"agent:{agent['name']}")
                except:
                    console.print(f"  [yellow]⚠️  Agent '{agent['name']}' already installed or failed[/yellow]")
                    all_success = False
            else:
                console.print(f"  [yellow]⚠️  Agent file '{agent['name']}.md' not found[/yellow]")

    # Install helper commands
    if 'helper_commands' in workflow_def:
        console.print(f"\n[bold]Helper Commands ({len(workflow_def['helper_commands'])}):[/bold]")
        for cmd in workflow_def['helper_commands']:
            # Check if corresponding .md file exists
            cmd_source = get_extensions_dir() / "commands" / f"{cmd['name']}.md"
            if cmd_source.exists():
                try:
                    install_extension("command", cmd['name'], target_path, force)
                    installed_components.append(f"command:{cmd['name']}")
                except:
                    console.print(f"  [yellow]⚠️  Command '{cmd['name']}' already installed or failed[/yellow]")
                    all_success = False
            else:
                console.print(f"  [yellow]⚠️  Command file '{cmd['name']}.md' not found[/yellow]")

    if installed_components:
        console.print(f"\n[green]✅ Workflow '{name}' installation completed[/green]")
        console.print(f"[dim]Installed {len(installed_components)} components[/dim]")
    else:
        console.print(f"\n[red]❌ No components were installed[/red]")
        all_success = False

    return all_success, installed_components


def install_multiple_extensions(
    ext_type: str,
    names: List[str],
    project_path: Optional[Path] = None,
    force: bool = False
) -> Tuple[List[str], List[str]]:
    """Install multiple extensions at once.

    Returns:
        Tuple of (successful_installs, failed_installs)
    """
    successful = []
    failed = []

    console.print(f"\n[bold]Installing {len(names)} {ext_type}(s)...[/bold]\n")

    for name in names:
        try:
            # Source path - look for .md file
            extensions_dir = get_extensions_dir()
            source_file = extensions_dir / f"{ext_type}s" / f"{name}.md"

            if not source_file.exists():
                console.print(f"  [red]❌ {name}: Not found[/red]")
                failed.append(name)
                continue

            # Target path - also .md file
            claude_dir = get_claude_dir(project_path)
            target_file = claude_dir / f"{ext_type}s" / f"{name}.md"

            # Check if already exists
            if target_file.exists() and not force:
                console.print(f"  [yellow]⚠️  {name}: Already installed (use --force to overwrite)[/yellow]")
                failed.append(name)
                continue

            # Create directory structure
            target_file.parent.mkdir(parents=True, exist_ok=True)

            # Copy file
            shutil.copy2(source_file, target_file)

            console.print(f"  [green]✅ {name}: Installed successfully[/green]")
            successful.append(name)

        except Exception as e:
            console.print(f"  [red]❌ {name}: Failed - {str(e)}[/red]")
            failed.append(name)

    return successful, failed


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: bool = typer.Option(False, "--version", "-v", help="Show version"),
    help: bool = typer.Option(False, "--help", "-h", help="Show help"),
):
    """Claude Code Extensions Manager"""
    if version:
        print(f"[cyan]claude-ext[/cyan] version [green]{__version__}[/green]")
        raise typer.Exit()

    if help and ctx.invoked_subcommand is None:
        # Show help if explicitly requested
        print("[cyan]Claude Code Extensions Manager[/cyan]")
        print("\nUsage: claude-ext [workflow|agent|command|interactive] [OPTIONS]")
        print("\nCommands:")
        print("  workflow      Manage Claude Code workflows (command + agents)")
        print("  agent         Manage Claude Code agents")
        print("  command       Manage Claude Code commands")
        print("  interactive   Interactive mode (guided)")
        print("  list-projects List available Claude projects")
        print("\nExamples:")
        print("  claude-ext                                      # Start interactive mode (default)")
        print("  claude-ext interactive                         # Start interactive mode")
        print("  claude-ext list-projects                       # List available Claude projects")
        print("  claude-ext workflow list                       # List available workflows")
        print("  claude-ext workflow info code-review           # Show workflow details")
        print("  claude-ext workflow install project-init       # Install a workflow")
        print("  claude-ext agent list")
        print("  claude-ext agent install security-scanner")
        print("  claude-ext agent install scanner analyzer -f   # Install multiple")
        print("  claude-ext command install -i                  # Interactive multi-select")
        print("  claude-ext command install smart-commit --project ~/my-project")
        print("\nRun 'claude-ext [COMMAND] --help' for more information")
        raise typer.Exit()

    if ctx.invoked_subcommand is None:
        # Default to interactive mode if no command given
        interactive()


if __name__ == "__main__":
    app()