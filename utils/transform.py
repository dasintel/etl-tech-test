import geopandas
from shapely import wkt

input = "../input.gpkg"
output = "../output.gpkg"
box = wkt.loads('POLYGON ((174.267 -39.422, 174.2688 -39.422, 174.2688 -39.4204, 174.267 -39.4204, 174.267 -39.422))')


def convert_to_centroids(df):
    for idx, row in df.iterrows():
        row.geometry = row.geometry.centroid


def process(df):
    convert_to_centroids(df)
    df = df[~df.intersects(box)]
    df = df.to_crs('EPSG')
    return df


def main(filename):
    x = geopandas.read_file(filename)
    process(x)
    x.to_file(output, driver='GTiff')
    return x


if __name__ == '__main__':
    main(input)
