from flask import Flask, request, jsonify
import pymongo
from processing import Processing

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

if __name__ == '__main__':
    app.run(host='0.0.0.0')