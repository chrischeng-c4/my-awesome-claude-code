#!/usr/bin/env python3
"""
Claude Code Extensions Manager - Simple CLI for managing Claude Code extensions
"""

import shutil
from pathlib import Path
from typing import Optional

import typer
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm

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
    name: str = typer.Argument(..., help="Agent name to install"),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help="Project path (if not specified, installs to user level)"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite if exists"),
):
    """Install a Claude Code agent."""
    install_extension("agent", name, project, force)


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
    name: str = typer.Argument(..., help="Command name to install"),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help="Project path (if not specified, installs to user level)"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite if exists"),
):
    """Install a Claude Code command."""
    install_extension("command", name, project, force)


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
        print("  claude-ext command install smart-commit --project ~/my-project")
        print("\nRun 'claude-ext [COMMAND] --help' for more information")


if __name__ == "__main__":
    app()