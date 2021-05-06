from datetime import datetime
from typing import List, Set, Dict
import fiona


def find_soil_orders(filename: str) -> Set[str]:
    orders = set()
    with fiona.open(filename) as dataset:
        for record in dataset:
            properties = record['properties']
            if properties['SoilOrder'] not in orders:
                orders.add(properties['SoilOrder'])
    return orders


def count_soil_order(filename: str, soil_order: str):
    """Count the number of records where the Soil Order matches soil_order"""
    count = 0
    with fiona.open(filename) as dataset:
        for record in dataset:
            if record['properties']['SoilOrder'] == soil_order:
                count += 1


def find_soil_families(filename: str, families: list = []):
    with fiona.open(filename) as dataset:
        for record in dataset:
            family = record['properties']['FamilyName']
            if family not in families:
                families.append(family)
    return families



def count_duplicates(filename: str) -> int:
    dupes = 0
    seen = list()
    with fiona.open(filename) as dataset:
        for record in dataset:
            if record['id'] in seen:
                dupes += 1
            else:
                seen.append(record['id'])
    return dupes


def do_analysis(filename: str) -> Dict:
    return {
        'soils': list(find_soil_orders(filename)),
        'soil_order_counts': {
            soil_order: count_soil_order(filename, soil_order)
            for soil_order in find_soil_orders(filename)
        },
        'duplicates': count_duplicates(filename)
    }


if __name__ == '__main__':
    soils = find_soil_orders('input.gpkg')
    for soil in soils:
        soil_count = count_soil_order('input.gpkg', soil)
        print(f'File has {soil_count} records of soil type {soil}.')
    print(f'There are {find_soil_families("input.gpkg")} unique soil families')
    print(f'There were {count_duplicates("input.gpkg")} Duplicate records')
