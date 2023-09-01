"""Module for gcli, click.testing."""
from gcli import search
from click.testing import CliRunner



# search(path, ftype):


def test_search():
    """search for file type"""
    runner = CliRunner()
    result = runner.invoke(search, ["--path", ".", "--ftype", "py"])
    assert result.exit_code == 0
    assert ".py" in result.output
