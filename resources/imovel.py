from flask_restful import Resource, reqparse
from models.imovel import ImovelModel


imoveis = {}

class Imoveis(Resource):
    
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('tipo', type=str)
    argumentos.add_argument('preco', type=float)
    argumentos.add_argument('m2', type=int)
    argumentos.add_argument('quatos', type=int)
    argumentos.add_argument('banheiros', type=int)
    argumentos.add_argument('vagas', type=int)
    argumentos.add_argument('condominio', type=float)
    argumentos.add_argument('iptu', type=float)
    argumentos.add_argument('bairro', type=float)
    argumentos.add_argument('rua', type=float)

    def get(self):
        return {'imoveis': imoveis}

    def post(self, imovel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('tipo')
        argumentos.add_argument('preco')
        argumentos.add_argument('m2')
        argumentos.add_argument('quatos')
        argumentos.add_argument('banheiros')
        argumentos.add_argument('vagas')
        argumentos.add_argument('condominio')
        argumentos.add_argument('iptu')
        argumentos.add_argument('bairro')
        argumentos.add_argument('rua')

        dados = argumentos.parse_args()

        novo_imovel = {
            'imovel_id': imovel_id,
            'tipo': dados['tipo'],
            'preco': dados['preco'],
            'quatos': dados['quatos'],
            'banheiros': dados['banheiros'],
            'vagas': dados['vagas'],
            'condominio': dados['condominio'],
            'iptu': dados['iptu'],
            'bairro': dados['bairro'],
            'rua': dados['rua']
        }

        imoveis.append(novo_imovel)
        return novo_imovel, 200

    def put(self):
        dados = Imoveis.argumentos.parse_args()
        apartamento_objeto = ImovelModel(**dados)
        #novo_apartamento = apartamento_objeto.json
        imoveis.append(apartamento_objeto)
            
    def get(sel, tipo):
        
        apartamentos = [imovel for imovel in imoveis if imovel['tipo'] == tipo]
        return apartamentos



class Imovel(Resource):
    def get(self, imovel_id):
        for imovel in imoveis:
            if imovel['imovel_id'] == imovel_id:
                return imovel, 200
        return {'message': 'Imovel não encontrado'}, 404

    def post(self, imovel_id):
        pass

    def put(self, imovel_id):
        pass
    
    def delete(self, imovel_id):
        pass
