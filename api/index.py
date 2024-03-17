import asyncio
from flask import Flask
from flask import request
from flask_cors import CORS
import postalservice as ps

app = Flask(__name__)
CORS(app)


@app.after_request
def add_no_cache_headers(response):
    response.headers.add(
        "Cache-Control",
        "no-store, no-cache, must-revalidate, post-check=0, pre-check=0",
    )
    response.headers.add("Pragma", "no-cache")
    return response


@app.route("/")
def home():
    if request.args.get("site", "") == "mercari":

        mercari = ps.MercariService()
        keyword = request.args.get("keyword", "")
        size = request.args.get("size", "")
        page = int(request.args.get("page", ""))
        if page == "":
            page = 1
        result = mercari.get_search_results(
            {"keyword": keyword, "size": size, "page": page}
        )
        return result.to_json()

    if request.args.get("site", "") == "fril":

        fril = ps.FrilService()
        keyword = request.args.get("keyword", "")
        size = request.args.get("size", "")
        page = int(request.args.get("page", ""))
        if page == "":
            page = 1
        result = asyncio.run(
            fril.get_search_results_async(
                {"keyword": keyword, "size": size, "page": page}
            )
        )
        return result.to_json()

    return "Hello, World! Hello, API!"


@app.route("/about")
def about():
    return "About"


@app.route("/mercari")
def mercari():
    mercari = ps.MercariService()
    keyword = request.args.get("keyword", "")
    size = request.args.get("size", "")
    result = mercari.get_search_results({"keyword": keyword, "size": size})
    return result.to_json()


@app.route("/fril")
def fril():
    fril = ps.FrilService()
    keyword = request.args.get("keyword", "")
    size = request.args.get("size", "")
    result = asyncio.run(
        fril.get_search_results_async({"keyword": keyword, "size": size})
    )
    return result.to_json()
