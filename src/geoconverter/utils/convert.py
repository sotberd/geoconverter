import logging
import os

import geopandas as gpd

# from src.geoconverter.logger import get_logger

logger = logging.getLogger(__name__)

# Set environment variable to restore the .shx file
os.environ["SHAPE_RESTORE_SHX"] = "YES"


# Define allowed extensions for each file type
ALLOWED_EXTENSIONS = {
    "shp": ".shp",
    "dbf": ".dbf",
    "shx": ".shx",
    "prj": ".prj",
    "cpg": ".cpg",
}


def validate_file_extension(filename: str, expected_extension: str) -> bool:
    """Check if the file has the correct extension."""
    return filename.lower().endswith(expected_extension)


def convert_shp_to_geojson(
    input_dir: str, output_dir: str, crs: str | None = None
) -> str | Exception:
    """
    Search for .shp files in a directory, convert each to GeoJSON format,
    and save in the output directory with the same name but .geojson extension.

    Parameters
    ----------
    input_dir : str
        The directory to search for .shp files.
    output_dir : str
        The directory to save the output GeoJSON files.
    crs : str, optional
        The CRS to convert the shapefile to (default is None).
    """
    logger.info(f"Converting files in {input_dir} to GeoJSON format...")
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Loop over all files in the input directory
        for file_name in os.listdir(input_dir):
            # Process only .shp files
            if file_name.endswith(".shp"):
                # Construct full file path
                input_path = os.path.join(input_dir, file_name)

                # Read the shapefile
                gdf = gpd.read_file(input_path)

                # If CRS is provided, convert to the specified CRS
                if crs:
                    gdf = gdf.to_crs(crs)

                # Create the output file path by replacing the .shp extension with .geojson
                base_name = os.path.splitext(file_name)[0]
                output_path = os.path.join(output_dir, f"{base_name}.geojson")

                # Save as GeoJSON
                gdf.to_file(output_path, driver="GeoJSON")
                logger.info(f"Converted {input_path} to {output_path}")

        logger.info(f"GeoJSON saved to {output_dir} directory")
        return output_path

    except Exception as e:
        logger.error(f"{e}")
        return e
