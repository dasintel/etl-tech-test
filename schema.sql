CREATE TABLE public.generic_geometry (
    id        SERIAL PRIMARY KEY,
    geometry  GEOMETRY,
    rep_point GEOMETRY,
    centroid  GEOMETRY,
    area      FLOAT
);

CREATE TABLE public.name (
    id   SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE public.rainfall_records (
    id                              SERIAL PRIMARY KEY,
    geometry_id                     BIGSERIAL REFERENCES public.generic_geometry NOT NULL,
    name                            INTEGER REFERENCES public.name NOT NULL UNIQUE,
    rainfall                        DECIMAL,
    elevation                       JSONB
);
