"""Tests for config parsing."""

import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from awsui.config import parse_profiles


def test_parse_sso_profile():
    """Test parsing SSO profile from config."""
    config_content = """[sso-session corp]
sso_start_url = https://example.awsapps.com/start
sso_region = ap-northeast-1

[profile test-sso]
sso_session = corp
sso_account_id = 111111111111
sso_role_name = AdministratorAccess
region = ap-northeast-1
output = json
"""

    with NamedTemporaryFile(mode='w', suffix='.config', delete=False) as f:
        f.write(config_content)
        config_path = f.name

    try:
        # Set environment variable to use test config
        original_config = os.environ.get("AWS_CONFIG_FILE")
        os.environ["AWS_CONFIG_FILE"] = config_path

        profiles = parse_profiles()

        assert len(profiles) >= 1
        sso_profile = next((p for p in profiles if p["name"] == "test-sso"), None)
        assert sso_profile is not None
        assert sso_profile["kind"] == "sso"
        assert sso_profile["account"] == "111111111111"
        assert sso_profile["role"] == "AdministratorAccess"
        assert sso_profile["region"] == "ap-northeast-1"
        assert sso_profile["session"] == "corp"

    finally:
        # Restore environment
        if original_config:
            os.environ["AWS_CONFIG_FILE"] = original_config
        elif "AWS_CONFIG_FILE" in os.environ:
            del os.environ["AWS_CONFIG_FILE"]

        # Clean up temp file
        Path(config_path).unlink(missing_ok=True)


def test_parse_assume_role_profile():
    """Test parsing assume role profile."""
    config_content = """[profile base]
region = us-east-1

[profile test-assume]
source_profile = base
role_arn = arn:aws:iam::222222222222:role/MyRole
region = us-west-2
"""

    with NamedTemporaryFile(mode='w', suffix='.config', delete=False) as f:
        f.write(config_content)
        config_path = f.name

    try:
        original_config = os.environ.get("AWS_CONFIG_FILE")
        os.environ["AWS_CONFIG_FILE"] = config_path

        profiles = parse_profiles()

        assume_profile = next((p for p in profiles if p["name"] == "test-assume"), None)
        assert assume_profile is not None
        assert assume_profile["kind"] == "assume"
        assert assume_profile["account"] == "222222222222"
        assert assume_profile["role"] == "MyRole"
        assert assume_profile["region"] == "us-west-2"

    finally:
        if original_config:
            os.environ["AWS_CONFIG_FILE"] = original_config
        elif "AWS_CONFIG_FILE" in os.environ:
            del os.environ["AWS_CONFIG_FILE"]

        Path(config_path).unlink(missing_ok=True)


def test_parse_empty_config():
    """Test parsing empty config file."""
    with NamedTemporaryFile(mode='w', suffix='.config', delete=False) as f:
        f.write("")
        config_path = f.name

    try:
        original_config = os.environ.get("AWS_CONFIG_FILE")
        os.environ["AWS_CONFIG_FILE"] = config_path

        profiles = parse_profiles()
        # Should return empty list or only profiles from credentials file
        assert isinstance(profiles, list)

    finally:
        if original_config:
            os.environ["AWS_CONFIG_FILE"] = original_config
        elif "AWS_CONFIG_FILE" in os.environ:
            del os.environ["AWS_CONFIG_FILE"]

        Path(config_path).unlink(missing_ok=True)