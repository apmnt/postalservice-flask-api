# import asyncio
from flask import Flask
from flask import request
import postalservice as ps

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

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

# @app.route('/fril')
# def fril():
#     fril = ps.FrilService()
#     keyword = request.args.get('keyword', '')
#     size = request.args.get('size', '')
#     result = asyncio.run(fril.get_search_results_async({'keyword': keyword, 'size': size}))
#     return result.to_json()

