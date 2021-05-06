import json
import geopandas
from django.http import HttpRequest, JsonResponse, HttpResponse


from utils.vector_subset import get_subset
from utils.vector_analysis import do_analysis
from utils.transform import main as transform_main
from server.settings import INPUT_FILE


def index(request: HttpRequest):
    return HttpResponse('''
        <html>
        <head><title>Function Index</title>
        <body>
        <h1>Example Endpoints</h1>
        <p><a href="/analyse">/analyse</a></p>
        <p><a href="/subset/SoilOrder/Gley Soils">/subset/SoilOrder/Gley Soils</a></p>
        <p><a href="/transform">/transform</a></p>
        </body>
        </html>
    ''')


def subset(request: HttpRequest, column: str, value: str):
    df = geopandas.read_file(INPUT_FILE)
    subset = get_subset(df, column_name=column, match_value=value)
    return JsonResponse(json.loads(subset.to_json()))


def analyse(request: HttpRequest):
    return JsonResponse(do_analysis(INPUT_FILE))


def transform(request: HttpRequest):
    df = transform_main(INPUT_FILE)
    df['geometry'] = df.geometry.apply(lambda x: x.wkt)
    return JsonResponse({'data': df.to_dict(orient='records')})
