import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

from typer.testing import CliRunner

from geoconverter.cli import app
from geoconverter.exceptions import CLIException


def test_version_command():
    runner = CliRunner()
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "GeoConverter CLI version" in result.output


def test_convert_shp_to_geojson():
    runner = CliRunner()

    # Mock the conversion function
    with patch("geoconverter.cli.convert_shp_to_geojson") as mock_convert:
        mock_convert.return_value = None  # Assume it runs successfully
        result = runner.invoke(
            app,
            [
                "shp2geojson",
                "--input-path",
                "data/shp",
                "--output-path",
                "data/x",
            ],
        )
        assert result.exit_code == 0
        assert "Conversion completed!" in result.output


def test_empty_input_directory():
    runner = CliRunner()

    # Simulate an empty directory
    with patch("os.listdir", return_value=[]):
        result = runner.invoke(
            app,
            [
                "shp2geojson",
                "--input-path",
                "empty_dir",
                "--output-path",
                "output.geojson",
            ],
        )
        assert result.exit_code == 1
        assert "The input folder is empty." in result.output


def test_convert_with_crs():
    runner = CliRunner()

    # Mock the conversion function
    with patch("geoconverter.cli.convert_shp_to_geojson") as mock_convert:
        mock_convert.return_value = None  # Assume it runs successfully
        result = runner.invoke(
            app,
            [
                "shp2geojson",
                "--input-path",
                "data/shp",
                "--output-path",
                "data/x",
                "--crs",
                "EPSG:4326",
            ],
        )
        assert result.exit_code == 0
        # Check if the correct CRS is passed
        mock_convert.assert_called_with("data/shp", "data/x", crs="EPSG:4326")


def test_cli_exception_handling():
    runner = CliRunner()

    # Simulate a CLIException being raised during conversion
    with patch("geoconverter.cli.convert_shp_to_geojson") as mock_convert:
        mock_convert.side_effect = CLIException("Custom error occurred")
        result = runner.invoke(
            app,
            [
                "shp2geojson",
                "--input-path",
                "data/shp",
                "--output-path",
                "data/x",
            ],
        )

        assert "Custom error occurred" in result.output


#  runner = CliRunner()
#     result = runner.invoke(app, ["--version"])
#     assert result.exit_code == 0
#     assert "GeoConverter CLI version" in result.output
