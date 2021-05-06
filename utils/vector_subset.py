import geopandas
from geopandas.geodataframe import GeoDataFrame
from server.settings import BASE_DIR

WANTED_SOIL_TYPE = 'Recent Soils'
INPUT_FILE = BASE_DIR / 'input.gpkg'


def get_subset(dataframe, column_name, match_value) -> GeoDataFrame:
    """
    Return a subset of the dataframe where the value of 'column' equals 'match_value'
    """
    subset = []
    for idx, row in dataframe.iterrows():
        if row[column_name] == match_value:
            subset.append(row)
    return GeoDataFrame(subset, crs=dataframe.crs)



df = geopandas.read_file(INPUT_FILE)

# Extract all Gley Soils records
WANTED_SOIL_TYPE = 'Gley Soils'
subset = get_subset(df, 'SoilOrder', WANTED_SOIL_TYPE)

# Calculate area
subset['area'] = subset.area * 10000

# Decrease the shape size by 5 meters
subset = subset.buffer(5)

# Write the subset
subset.to_file('subset.geojson', driver='GeoJSON')
