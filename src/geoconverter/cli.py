import logging
import os
from typing import Annotated

import typer
from rich import print

from . import __version__
from .exceptions import CLIException
from .logger import get_rich_toolkit, setup_logging
from .utils.convert import convert_shp_to_geojson

app = typer.Typer(rich_markup_mode="rich")

logger = logging.getLogger(__name__)


def version_callback(value: bool) -> None:
    if value:
        print(f"GeoConverter CLI version: [green]{__version__}[/green]")
        raise typer.Exit()


@app.callback()
def callback(
    _: Annotated[
        bool | None,
        typer.Option(
            "--version", help="Show the version and exit.", callback=version_callback
        ),
    ] = None,
    verbose: bool = typer.Option(False, help="Enable verbose output"),
) -> None:
    """
    [bold]GeoConverter CLI 🚀[/bold] - A tool to convert geospatial data formats.

    Read more in: [link=https://github.com/sotberd/geoconverter]GitHub.
    """
    log_level = logging.DEBUG if verbose else logging.INFO
    setup_logging(level=log_level)


@app.command(
    name="shp2geojson",
    help="Convert Shapefile to GeoJSON",
)
def shp2geojson(
    input_path: Annotated[
        str, typer.Option(prompt=True, help="The path to the input shapefile.")
    ],
    output_path: Annotated[
        str, typer.Option(prompt=True, help="The path to save the output GeoJSON file.")
    ],
    crs: Annotated[
        str | None,
        typer.Option(
            help="The CRS to convert the GeoJSON to specified CRS. Default is the original CRS."
        ),
    ] = None,
) -> None:
    with get_rich_toolkit() as toolkit:
        toolkit.print_title(
            f"Starting conversion of Shapefile {input_path} to GeoJSON {output_path}",
            tag="GeoConverter CLI",
        )
        toolkit.print_line()

        if not os.listdir(input_path):
            logger.error("The input folder is empty.")
            raise typer.Abort()
        try:
            convert_shp_to_geojson(input_path, output_path, crs=crs)
        except CLIException as e:
            toolkit.print(f"[selected]{e}")


def main() -> None:
    app()
