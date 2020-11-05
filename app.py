# importando bibliotecas necessárias
import numpy as np
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from joblib import load

# instanciando objeto Flask
app = Flask(__name__)

# API
api = Api(app)

# carregar modelo
model = load('model/model.joblib')


class PrecoImoveis(Resource):
    def get(self):
        """
        retorna as informações caracteristicas do modelo
        para gerar o modelo preditivo
        """
        return {'Nome': 'Marcel Bittar'}

    def post(self):
        """
        recebe todos os argumentos que estão sendo enviados para a aplicação
        valor com base no modelo.joblib elaborado
        permitido apenas uma consulta por vez
        var input_values recebe uma matriz reformatada para utilizar no sklearn
        var predict faz a previsão de valor calculado utilizando o modelo criado anteriormente com os valores fornecidos pela input_values retornando apenas o primeiro valor

        retorna um json da previsão de valor do imóvel
        """
        args = request.get_json(force=True)
        input_values = np.asarray(list(args.values())).reshape(1, -1)
        predict = model.predict(input_values)[0]

        return jsonify({'previsao: ', float(predict)})


api.add_resource(PrecoImoveis, '/')

if __name__ == '__main__':
    app.run()