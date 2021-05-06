# Example ETL code for DAS

This project contains some code for use as a short technical test for ETL developers.


## Overview

There are few things in this project which are intentionally done in suboptimal, inefficient, or incorrect ways.
Your task with this project is to:

- Provide feedback on the following scripts:
  - `utils/vector_subset.py`
  - `utils/vector_analysis.py`
  - `utils/transform.py`
- Give a short summary of how the following function works and where it could be used:
  - `utils/tile_vectors.py`
- Provide feedback on the database schema
  - `schema.sql`
 


## Setup

- Install Python (tested using v3.9)
- Install the requirements listed in `requirements.txt`



## Web Server

There is a Django-based web server included in the repository. You are not expected to review these files (_i.e._ anything in the `server` folder).
The web server is included only to provide a trigger for the util scripts (`vector_subset.py` and `vector_analyis.py`) if needed.

To start the server:

```
cd server
python manage.py runserver
```
Then navigate to one of the following URLs to trigger the relevant script:

Run `vector_analysis.py` and return a JSON object:
[http://localhost:8000/analyse/](http://localhost:8000/analyse/)


Run `vector_subset.py` and return the records where "SoilOrder" equals "Gley Soils", as per URL parameters:
[http://localhost:8000/subset/SoilOrder/Gley%20Soils](http://localhost:8000/subset/SoilOrder/Gley%20Soils)



## Review Considerations
Some things to consider while reading these files:
- Does the script/database design make sense?
- Is it efficient?
- Is it clear what the code does?
- Could we improve anything?
- Any other feedback
  


## Notes

- We are only expecting a short review of the files specified above
- The web server (all files in the `server` folder) does __not__ need to be reviewed
- The Python scripts make use of these libraries:
  - `geopandas` - This is a wrapper around `Pandas` which adds some geospatial functions
  - `fiona` - This a library to iteratively read features from a geospatial vector datase
    
  