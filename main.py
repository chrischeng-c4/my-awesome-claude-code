#!/usr/bin/env python3
"""
Claude Code Extensions Manager - Simple CLI for managing Claude Code extensions
"""

import os
import shutil
import sys
from pathlib import Path
from typing import Optional, List, Tuple

import typer
import click
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.text import Text

__version__ = "1.0.0"

app = typer.Typer(
    name="claude-ext",
    help="Manage Claude Code extensions",
    add_completion=False,
)
console = Console()

# Create subcommands for agent and command
agent_app = typer.Typer(help="Manage Claude Code agents")
command_app = typer.Typer(help="Manage Claude Code commands")

app.add_typer(agent_app, name="agent")
app.add_typer(command_app, name="command")


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


def list_available(ext_type: str):
    """List available extensions of given type."""
    extensions_dir = get_extensions_dir()
    type_dir = extensions_dir / f"{ext_type}s"

    if not type_dir.exists():
        return []

    results = []
    for item in type_dir.iterdir():
        if item.is_file() and item.suffix == '.md':
            # Remove .md extension from name
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
def interactive():
    """Interactive mode for managing extensions"""
    console.print("[bold cyan]Claude Code Extensions Manager - Interactive Mode[/bold cyan]\n")

    # Choose extension type
    ext_type = Prompt.ask(
        "What would you like to manage?",
        choices=["agent", "command", "quit"],
        default="agent"
    )

    if ext_type == "quit":
        console.print("[yellow]Goodbye![/yellow]")
        raise typer.Exit()

    # Choose action
    action = Prompt.ask(
        f"\nWhat would you like to do with {ext_type}s?",
        choices=["list", "install", "uninstall", "quit"],
        default="list"
    )

    if action == "quit":
        console.print("[yellow]Goodbye![/yellow]")
        raise typer.Exit()

    # Execute action
    if action == "list":
        # Ask if listing available or installed
        list_type = Prompt.ask(
            "\nList which extensions?",
            choices=["available", "installed"],
            default="available"
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
            # Ask for level
            if Confirm.ask("\nList user-level extensions?", default=False):
                project = None
            else:
                project = Path(Prompt.ask("Project path", default="."))

            installed = list_installed(ext_type, project)
            if not installed:
                level = "user" if project is None else "project"
                console.print(f"[yellow]No {ext_type}s installed at {level} level[/yellow]")
            else:
                console.print(f"\n[bold]Installed {ext_type.capitalize()}s:[/bold]")
                for name, location in installed:
                    console.print(f"  • [green]{name}[/green] ({location})")

    elif action == "install":
        # Show available extensions
        extensions = list_available(ext_type)
        if not extensions:
            console.print(f"[yellow]No {ext_type}s available to install[/yellow]")
            raise typer.Exit()

        # Ask for selection mode
        mode = Prompt.ask(
            "\nSelection mode?",
            choices=["single", "multiple"],
            default="multiple"
        )

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

            if Confirm.ask(f"\nInstall to user level?", default=False):
                project = None
                console.print("[dim]Installing to user level (~/.claude)[/dim]")
            else:
                project = Path(Prompt.ask("Project path", default="."))
                console.print(f"[dim]Installing to project: {project}[/dim]")

            # Confirm and install
            if Confirm.ask(f"\nProceed with installation of {len(selected_items)} {ext_type}(s)?", default=True):
                successful, failed = install_multiple_extensions(ext_type, selected_items, project)

                # Summary
                console.print(f"\n[bold]Installation Summary:[/bold]")
                if successful:
                    console.print(f"[green]✅ Successfully installed: {len(successful)} {ext_type}(s)[/green]")
                if failed:
                    console.print(f"[red]❌ Failed: {len(failed)} {ext_type}(s)[/red]")
            else:
                console.print("[yellow]Installation cancelled[/yellow]")

        else:
            # Single selection mode (original behavior)
            console.print(f"\n[bold]Available {ext_type.capitalize()}s:[/bold]")
            for i, name in enumerate(sorted(extensions), 1):
                console.print(f"  {i}. [green]{name}[/green]")

            # Select extension
            while True:
                choice = Prompt.ask("\nSelect number (or 'q' to quit)")
                if choice.lower() == 'q':
                    console.print("[yellow]Cancelled[/yellow]")
                    raise typer.Exit()

                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(extensions):
                        selected = sorted(extensions)[idx]
                        break
                    else:
                        console.print("[red]Invalid selection[/red]")
                except ValueError:
                    console.print("[red]Please enter a number[/red]")

            # Choose installation level
            if Confirm.ask(f"\nInstall '{selected}' to user level?", default=False):
                project = None
                console.print("[dim]Installing to user level (~/.claude)[/dim]")
            else:
                project = Path(Prompt.ask("Project path", default="."))
                console.print(f"[dim]Installing to project: {project}[/dim]")

            # Confirm and install
            if Confirm.ask(f"\nProceed with installation?", default=True):
                try:
                    install_extension(ext_type, selected, project)
                    console.print(f"[green]✅ Successfully installed '{selected}'![/green]")
                except typer.Exit:
                    pass  # Error already displayed
            else:
                console.print("[yellow]Installation cancelled[/yellow]")

    elif action == "uninstall":
        # Choose level first
        if Confirm.ask("\nUninstall from user level?", default=False):
            project = None
        else:
            project = Path(Prompt.ask("Project path", default="."))

        # Show installed extensions
        installed = list_installed(ext_type, project)
        if not installed:
            level = "user" if project is None else "project"
            console.print(f"[yellow]No {ext_type}s installed at {level} level[/yellow]")
            raise typer.Exit()

        console.print(f"\n[bold]Installed {ext_type.capitalize()}s:[/bold]")
        for i, (name, location) in enumerate(installed, 1):
            console.print(f"  {i}. [green]{name}[/green]")

        # Select extension to uninstall
        while True:
            choice = Prompt.ask("\nSelect number to uninstall (or 'q' to quit)")
            if choice.lower() == 'q':
                console.print("[yellow]Cancelled[/yellow]")
                raise typer.Exit()

            try:
                idx = int(choice) - 1
                if 0 <= idx < len(installed):
                    selected = installed[idx][0]
                    break
                else:
                    console.print("[red]Invalid selection[/red]")
            except ValueError:
                console.print("[red]Please enter a number[/red]")

        # Confirm and uninstall
        if Confirm.ask(f"\nUninstall '{selected}'?", default=False):
            try:
                uninstall_extension(ext_type, selected, project)
                console.print(f"[green]✅ Successfully uninstalled '{selected}'![/green]")
            except typer.Exit:
                pass  # Error already displayed
        else:
            console.print("[yellow]Uninstall cancelled[/yellow]")

    # Ask if user wants to continue
    if Confirm.ask("\n[cyan]Continue with another operation?[/cyan]", default=True):
        interactive()  # Recursive call to continue


def multi_select(
    items: List[str],
    title: str = "Select items",
    instructions: str = "Use numbers to select, 'a' for all, 'n' for none, 'c' to confirm"
) -> List[str]:
    """Interactive multi-select prompt with fallback for non-TTY environments."""
    selected = set()

    # Try to use the interactive mode, fall back to simpler selection if not available
    try:
        # Test if we can use getchar
        if not (hasattr(sys.stdin, 'isatty') and sys.stdin.isatty()):
            raise OSError("Not a TTY")

        # Try the interactive version first
        return _multi_select_interactive(items, title)
    except (OSError, ImportError):
        # Fallback to numbered selection
        return _multi_select_numbered(items, title)


def _multi_select_interactive(
    items: List[str],
    title: str
) -> List[str]:
    """Interactive multi-select with keyboard navigation."""
    selected = set()
    current_idx = 0
    instructions = "↑↓/jk Navigate | SPACE Select | a All | n None | ENTER Confirm | q Quit"

    # Hide cursor and set up terminal
    console.show_cursor(False)

    try:
        while True:
            # Clear screen for refresh
            console.clear()

            # Display title and instructions
            console.print(f"[bold cyan]{title}[/bold cyan]")
            console.print(f"[dim]{instructions}[/dim]\n")

            # Display items with selection status
            for i, item in enumerate(items):
                prefix = "[✓]" if item in selected else "[ ]"
                if i == current_idx:
                    # Highlight current item
                    console.print(f"  [bold reverse]{prefix} {item}[/bold reverse]")
                else:
                    if item in selected:
                        console.print(f"  [green]{prefix}[/green] {item}")
                    else:
                        console.print(f"  {prefix} {item}")

            # Display selected count
            if selected:
                console.print(f"\n[green]Selected: {len(selected)} item(s)[/green]")

            # Get user input (single keystroke)
            key = click.getchar()

            # Handle arrow keys (they come as escape sequences)
            if key == '\x1b':  # ESC sequence
                next_char = click.getchar()
                if next_char == '[':
                    arrow = click.getchar()
                    if arrow == 'A':  # Up arrow
                        current_idx = max(0, current_idx - 1)
                    elif arrow == 'B':  # Down arrow
                        current_idx = min(len(items) - 1, current_idx + 1)
            elif key == 'k':  # k for up
                current_idx = max(0, current_idx - 1)
            elif key == 'j':  # j for down
                current_idx = min(len(items) - 1, current_idx + 1)
            elif key == ' ':  # Space to toggle selection
                if items[current_idx] in selected:
                    selected.remove(items[current_idx])
                else:
                    selected.add(items[current_idx])
            elif key == '\r' or key == '\n':  # Enter to confirm
                break
            elif key.lower() == 'q':  # Quit
                selected = []
                break
            elif key.lower() == 'a':  # Select all
                selected = set(items)
            elif key.lower() == 'n':  # Select none
                selected.clear()
    finally:
        # Show cursor again
        console.show_cursor(True)
        console.clear()

    return list(selected)


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
):
    """Claude Code Extensions Manager"""
    if version:
        print(f"[cyan]claude-ext[/cyan] version [green]{__version__}[/green]")
        raise typer.Exit()

    if ctx.invoked_subcommand is None:
        # Show help if no command given
        print("[cyan]Claude Code Extensions Manager[/cyan]")
        print("\nUsage: claude-ext [agent|command|interactive] [OPTIONS]")
        print("\nCommands:")
        print("  agent        Manage Claude Code agents")
        print("  command      Manage Claude Code commands")
        print("  interactive  Interactive mode (guided)")
        print("\nExamples:")
        print("  claude-ext interactive                        # Start interactive mode")
        print("  claude-ext agent list")
        print("  claude-ext agent install security-scanner")
        print("  claude-ext agent install scanner analyzer -f  # Install multiple")
        print("  claude-ext command install -i                   # Interactive multi-select")
        print("  claude-ext command install smart-commit --project ~/my-project")
        print("\nRun 'claude-ext [COMMAND] --help' for more information")


if __name__ == "__main__":
    app()