"""Shell integration for environment export and subshell launching."""

import sys
import os
import subprocess


def detect_shell() -> str:
    """Detect the current shell type."""
    if sys.platform == "win32":
        return "powershell"

    shell = os.environ.get("SHELL", "/bin/sh")
    return shell


def print_env_commands(profile: str, region: str | None = None) -> None:
    """
    Print environment variable commands to STDOUT.

    Uses POSIX export for Unix shells, Set-Item for PowerShell.
    """
    shell = detect_shell()

    if shell == "powershell":
        # PowerShell syntax
        print(f'Set-Item Env:AWS_PROFILE "{profile}"')
        if region:
            print(f'Set-Item Env:AWS_DEFAULT_REGION "{region}"')
    else:
        # POSIX syntax
        print(f'export AWS_PROFILE="{profile}"')
        if region:
            print(f'export AWS_DEFAULT_REGION="{region}"')


def launch_subshell(profile: str, region: str | None = None) -> int:
    """
    Launch a subshell with AWS profile environment set.

    Returns the exit code of the subshell.
    """
    env = os.environ.copy()
    env["AWS_PROFILE"] = profile
    if region:
        env["AWS_DEFAULT_REGION"] = region

    shell = detect_shell()

    try:
        if sys.platform == "win32":
            result = subprocess.run(["powershell"], env=env)
        else:
            result = subprocess.run([shell], env=env)
        return result.returncode
    except subprocess.SubprocessError:
        return 1