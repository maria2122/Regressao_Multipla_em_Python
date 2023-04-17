from flask import Flask, render_template, request, redirect, jsonify
import pickle

modelo = pickle.load(open('./static/dados/modelo.sav', 'rb'))
colunas = ['TamanhoM',
           'PesoC',
           'Potencia',
           'Comprimento',
           'Altura',
           'TipoR',
           'cilindros',
           'consumoR',
           'consumoC']

app = Flask('meu_app')


@app.route('/')
def index():
    return render_template('index.html', titulo='Regressão')


@app.route('/classifica', methods=['POST'])
def classifica():
    dados = request.form
    dados_input = [float(dados[col]) for col in colunas]
    valor = modelo.predict([dados_input])

    response = round(valor[0], 2)

    return jsonify({'resultado': response})


if __name__ == "__main__":
    app.run(debug=True)
