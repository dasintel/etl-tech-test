def tile_vectors(gdf: GeoDataFrame, grid_shape=(10, 10))
    minx, miny, maxx, maxy = gdf.total_bounds
    width = maxx - minx
    height = maxy - miny
    cell_width = width / grid_shape[1]
    cell_height = height / grid_shape[0]
    x_edges = [minx + (cell_width * x) for x in range(grid_shape[1])]
    y_edges = [miny + (cell_height * x) for x in range(grid_shape[0])]

    x_overlap = abs(cell_width) / 20
    y_overlap = abs(cell_height) / 20

    tiles = [
        box(x, y, x + cell_width + x_overlap, y + cell_height + y_overlap)
        for x in x_edges for y in y_edges
    ]

    for idx, tile in enumerate(tiles):
        subset = gdf.iloc[list(gdf.sindex.intersection(tile.bounds))].copy()
        subset.geometry = subset.geometry.apply(lambda g: g.intersection(tile))
        yield subset, tile
