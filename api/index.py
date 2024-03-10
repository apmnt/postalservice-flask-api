import asyncio
from flask import Flask
from flask import request
from flask_cors import CORS
import postalservice as ps

app = Flask(__name__)
CORS(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
    return response

@app.route('/')
def home():
    if request.args.get('site', '') == 'mercari':

        mercari = ps.MercariService()
        keyword = request.args.get('keyword', '')
        size = request.args.get('size', '')
        result = mercari.get_search_results({'keyword': keyword, 'size': size})
        return result.to_json()

    if request.args.get('site', '') == 'fril':

        fril = ps.FrilService()
        keyword = request.args.get('keyword', '')
        size = request.args.get('size', '')
        result = asyncio.run(fril.get_search_results_async({'keyword': keyword, 'size': size}))
        return result.to_json()
        
    return 'Hello, World! Hello, API!'

@app.route('/about')
def about():
    return 'About'

@app.route('/mercari')
def mercari():
    mercari = ps.MercariService()
    keyword = request.args.get('keyword', '')
    size = request.args.get('size', '')
    result = mercari.get_search_results({'keyword': keyword, 'size': size})
    return result.to_json()

@app.route('/fril')
def fril():
    fril = ps.FrilService()
    keyword = request.args.get('keyword', '')
    size = request.args.get('size', '')
    result = asyncio.run(fril.get_search_results_async({'keyword': keyword, 'size': size}))
    return result.to_json()

