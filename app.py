from flask import Flask, request
from fetcher import *

app = Flask(__name__)
app.config['DEBUG'] = True

#* API ROUTES 

@app.route('/api/getDaily/', methods=['GET'])
def getDaily():
    if request.method == 'GET':
        return fetchDaily(search(request.args.get('stock'))['bestMatches'][0]['1. symbol']), 200
    else:
        return {'error': 'Invalid request method'}, 400

@app.route('/api/getIntraDay/', methods=['GET'])
def getIntraDay():
    if request.method == 'GET':
        return fetchIntraDay(search(request.args.get('stock'))['bestMatches'][0]['1. symbol']), 200
    else:
        return {'error': 'Invalid request method'}, 400

@app.route('/api/getCompanyDetails/', methods=['GET'])
def getCompanyDetails():
    if request.method == 'GET':
        return company_details(search(request.args.get('stock'))['bestMatches'][0]['1. symbol']), 200
    else:
        return {'error': 'Invalid request method'}, 400

@app.route('/api/getPrediction/', methods=['GET'])
def getPrediction():
    if request.method == 'GET':
        #* This sends the user defined stock name to the searcher then gets the prices and then predicts the n'th day high.
        return predict_high((fetchDaily(search(request.args.get('stock'))['bestMatches'][0]['1. symbol'])), int(request.args.get('duration'))), 200
    else:
        return {'error': 'Invalid request method'}, 400

if __name__ == '__main__':
    app.run()