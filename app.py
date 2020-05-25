from flask import Flask, request, jsonify
import pymongo
from processing import Processing
import os

app = Flask(__name__)
app.debug = True

# from flask_restful import Resource, Api
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
# api.add_resource(HelloWorld, '/')

@app.route('/') #methods=['GET', 'POST']
def index():
    # request.json
    # return jsonsify({'key': 'value'})
    # Convert
    p = Processing('./DeepFloorplan/demo/45719584.jpg')
    result = p.process_json_array()
    return jsonify({'data': result})

@app.route('/health')
def health():
    return 'running'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))