from flask import Flask, render_template, request, jsonify
import pickle

modelo = pickle.load(open('modelo.sav', 'rb'))
colunas = ['comprimentoS','larguraS','comprimentoP', 'larguraP']

app = Flask('meu_app')

@app.route('/')
def index():
    return render_template('index.html', titulo='Classificacao')

@app.route('/classifica/', methods=['POST'])
def classifica():
    dados = request.form
    dados_input = [float(dados[col]) for col in colunas]
    classe = modelo.predict([dados_input])
    if classe == 0:
        classe='Iris-setosa'
    elif classe == 1:
        classe='Iris-versicolor'
    else:
        classe='Iris-virginica'
    return classe



if __name__ == "__main__":
    app.run(debug=True)