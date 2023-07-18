from flask import Flask
from flask_restful import Api
from resources.imovel import Imoveis, Imovel

app = Flask(__name__)
api = Api(app)
    
api.add_resource(Imoveis, '/imoveis')
api.add_resource(Imoveis, '/imoveis/<string:imovel_id>')

if __name__ == '__main__':
    app.run(debug=True)
    


