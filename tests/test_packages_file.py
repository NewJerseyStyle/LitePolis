import importlib.metadata
from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner

from litepolis.core import cli


def _read_lines(path):
    return [line.rstrip("\n") for line in path.read_text().splitlines() if line.strip()]


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def packages_file(tmp_path):
    return tmp_path / "packages.txt"


@pytest.fixture(autouse=True)
def stub_subprocess():
    """Prevent any real `uv pip install/list` calls during tests."""
    with patch("litepolis.core.subprocess.run") as m:
        m.return_value = MagicMock(returncode=0, stdout="", stderr="")
        yield m


def _invoke(runner, packages_file, *args):
    return runner.invoke(
        cli,
        ["deploy", "--packages-file", str(packages_file), *args],
        catch_exceptions=False,
    )


def test_add_deps_writes_pinned_entry_when_version_detected(runner, packages_file):
    with patch("importlib.metadata.version", return_value="1.2.3"):
        result = _invoke(runner, packages_file, "add-deps", "litepolis-router-foo")
    assert result.exit_code == 0, result.output
    assert _read_lines(packages_file) == ["litepolis-router-foo==1.2.3"]


def test_add_deps_falls_back_to_bare_name_when_version_unknown(runner, packages_file):
    with patch(
        "importlib.metadata.version",
        side_effect=importlib.metadata.PackageNotFoundError,
    ):
        result = _invoke(runner, packages_file, "add-deps", "litepolis-router-foo")
    assert result.exit_code == 0, result.output
    assert _read_lines(packages_file) == ["litepolis-router-foo"]


def test_add_deps_does_not_duplicate_bare_name_entries(runner, packages_file):
    """Regression for #41: re-adding a bare-name package must not append a duplicate."""
    packages_file.write_text("litepolis-ui-particiapp\n")
    with patch(
        "importlib.metadata.version",
        side_effect=importlib.metadata.PackageNotFoundError,
    ):
        result = _invoke(runner, packages_file, "add-deps", "litepolis-ui-particiapp")
    assert result.exit_code == 0, result.output
    assert _read_lines(packages_file) == ["litepolis-ui-particiapp"]


def test_add_deps_collapses_pre_existing_duplicates(runner, packages_file):
    """Regression for #41: leftover duplicate lines must be pruned on next write."""
    packages_file.write_text(
        "litepolis-ui-particiapp\nlitepolis-ui-particiapp\nlitepolis-ui-particiapp\n"
    )
    result = _invoke(
        runner, packages_file, "add-deps", "litepolis-ui-particiapp==2.0.0"
    )
    assert result.exit_code == 0, result.output
    assert _read_lines(packages_file) == ["litepolis-ui-particiapp==2.0.0"]


def test_add_deps_updates_existing_pinned_entry_in_place(runner, packages_file):
    packages_file.write_text(
        "litepolis-router-foo==1.0.0\nlitepolis-router-bar==1.0.0\n"
    )
    result = _invoke(
        runner, packages_file, "add-deps", "litepolis-router-foo==2.0.0"
    )
    assert result.exit_code == 0, result.output
    assert _read_lines(packages_file) == [
        "litepolis-router-foo==2.0.0",
        "litepolis-router-bar==1.0.0",
    ]


def test_add_deps_preserves_comments_and_blank_lines(runner, packages_file):
    packages_file.write_text(
        "# header\n\nlitepolis-router-foo==1.0.0\n# trailing\n"
    )
    result = _invoke(
        runner, packages_file, "add-deps", "litepolis-router-bar==1.0.0"
    )
    assert result.exit_code == 0, result.output
    contents = packages_file.read_text()
    assert "# header" in contents
    assert "# trailing" in contents
    assert "litepolis-router-foo==1.0.0" in contents
    assert "litepolis-router-bar==1.0.0" in contents


def test_add_deps_handles_packages_file_without_directory_component(runner, tmp_path):
    """Regression: --packages-file 'packages.txt' (no dir) must not crash on dirname=''."""
    with runner.isolated_filesystem(temp_dir=tmp_path):
        with patch("importlib.metadata.version", return_value="1.0.0"):
            result = runner.invoke(
                cli,
                ["deploy", "--packages-file", "packages.txt",
                 "add-deps", "litepolis-router-foo"],
                catch_exceptions=False,
            )
        assert result.exit_code == 0, result.output


def test_add_deps_normalizes_underscore_and_hyphen(runner, packages_file):
    """Adding 'litepolis_router_foo' should match an existing 'litepolis-router-foo'."""
    packages_file.write_text("litepolis-router-foo==1.0.0\n")
    result = _invoke(
        runner, packages_file, "add-deps", "litepolis_router_foo==2.0.0"
    )
    assert result.exit_code == 0, result.output
    assert _read_lines(packages_file) == ["litepolis_router_foo==2.0.0"]


def test_remove_deps_removes_pinned_entry(runner, packages_file):
    packages_file.write_text(
        "litepolis-router-foo==1.0.0\nlitepolis-router-bar==2.0.0\n"
    )
    result = _invoke(runner, packages_file, "remove-deps", "litepolis-router-foo")
    assert result.exit_code == 0, result.output
    assert _read_lines(packages_file) == ["litepolis-router-bar==2.0.0"]


def test_remove_deps_removes_bare_name_entry(runner, packages_file):
    """Regression: remove-deps must also work when the line has no '==<version>'."""
    packages_file.write_text(
        "litepolis-ui-particiapp\nlitepolis-router-foo==1.0.0\n"
    )
    result = _invoke(runner, packages_file, "remove-deps", "litepolis-ui-particiapp")
    assert result.exit_code == 0, result.output
    assert _read_lines(packages_file) == ["litepolis-router-foo==1.0.0"]


def test_remove_deps_reports_when_package_missing(runner, packages_file):
    packages_file.write_text("litepolis-router-foo==1.0.0\n")
    result = _invoke(runner, packages_file, "remove-deps", "litepolis-router-bar")
    assert result.exit_code == 0
    assert "not found" in result.output.lower()


def test_sync_deps_installs_pinned_and_bare_name(runner, packages_file, stub_subprocess):
    """Regression: sync-deps used to silently skip bare-name lines."""
    packages_file.write_text(
        "litepolis-router-foo==1.0.0\nlitepolis-ui-particiapp\n"
    )
    result = _invoke(runner, packages_file, "sync-deps")
    assert result.exit_code == 0, result.output
    install_specs = [
        call.args[0][-1]
        for call in stub_subprocess.call_args_list
        if list(call.args[0][:3]) == ["uv", "pip", "install"]
    ]
    assert "litepolis-router-foo==1.0.0" in install_specs
    assert "litepolis-ui-particiapp" in install_specs


def test_list_deps_reports_bare_name_as_unpinned(runner, packages_file):
    """Regression: list-deps used to drop bare-name entries from the report."""
    packages_file.write_text("litepolis-ui-particiapp\n")
    result = _invoke(runner, packages_file, "list-deps")
    assert result.exit_code == 0, result.output
    assert "litepolis-ui-particiapp" in result.output
    assert "(unpinned)" in result.output
