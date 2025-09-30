"""Tests for shell integration."""

import sys
from io import StringIO
from awsui.shellout import print_env_commands, detect_shell


def test_print_env_posix(monkeypatch):
    """Test POSIX shell environment output."""
    # Mock platform to be non-Windows
    monkeypatch.setattr(sys, "platform", "linux")

    # Capture stdout
    captured_output = StringIO()
    monkeypatch.setattr(sys, "stdout", captured_output)

    print_env_commands("test-profile", "us-east-1")

    output = captured_output.getvalue()
    assert 'export AWS_PROFILE="test-profile"' in output
    assert 'export AWS_DEFAULT_REGION="us-east-1"' in output


def test_print_env_powershell(monkeypatch):
    """Test PowerShell environment output."""
    # Mock platform to be Windows
    monkeypatch.setattr(sys, "platform", "win32")

    # Capture stdout
    captured_output = StringIO()
    monkeypatch.setattr(sys, "stdout", captured_output)

    print_env_commands("test-profile", "eu-west-1")

    output = captured_output.getvalue()
    assert 'Set-Item Env:AWS_PROFILE "test-profile"' in output
    assert 'Set-Item Env:AWS_DEFAULT_REGION "eu-west-1"' in output


def test_print_env_without_region(monkeypatch):
    """Test environment output without region."""
    monkeypatch.setattr(sys, "platform", "linux")

    captured_output = StringIO()
    monkeypatch.setattr(sys, "stdout", captured_output)

    print_env_commands("test-profile")

    output = captured_output.getvalue()
    assert 'export AWS_PROFILE="test-profile"' in output
    assert "AWS_DEFAULT_REGION" not in output


def test_detect_shell_unix(monkeypatch):
    """Test shell detection on Unix."""
    monkeypatch.setattr(sys, "platform", "linux")
    monkeypatch.setenv("SHELL", "/bin/bash")

    shell = detect_shell()
    assert shell == "/bin/bash"


def test_detect_shell_windows(monkeypatch):
    """Test shell detection on Windows."""
    monkeypatch.setattr(sys, "platform", "win32")

    shell = detect_shell()
    assert shell == "powershell"