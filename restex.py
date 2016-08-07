from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources=r'/*') # to allow external resources to fetch data 
api = Api(app)

gpios = {"A0": { 'value': 0}, 
         "A1": { 'value': 0},
         "B0": { 'value': 0} }

@api.resource("/")
class url_index( Resource ):
    def get( self ):
       returnMessage = {"message": "Yes, it works" }
       return returnMessage

@api.resource("/gpio")
class url_gpio( Resource ):
    def get( self ):
        returnMessage = gpios.keys()
        return returnMessage

@api.resource("/gpio/<gpio_name>")
class url_gpio_name( Resource ):
    def get( self, gpio_name ):
        try:
            return gpios[ gpio_name ]
        except KeyError, ex:
            return { "message": "key error '%s' is not a GPIO name"%(gpio_name,) }, 400

    def put( self, gpio_name ):
        try:
            gpios[ gpio_name ]['value'] = request.json['data']
            return "", 204
        except KeyError, ex:
            return { "message": "key error: Either '%s' is not a GPIO name or data is undefined (received: '%s')"%(gpio_name, str(request.form)) }, 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

