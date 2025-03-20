from flask import Flask, request

app = Flask(__name__)

# Rota para soma de dois números
# noinspection PyBroadException
@app.route('/soma/<numero1>+<numero2>', methods=['GET'])
def soma(numero1, numero2):
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        return f"Resultado: {numero1 + numero2}", 200
    except:
        return "Erro: Parâmetros inválidos", 400

# Rota para subtração de dois números
# noinspection PyBroadException
@app.route('/subtracao/<numero1>-<numero2>', methods=['GET'])
def subtracao(numero1, numero2):
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        return f"Resultado: {numero1 - numero2}", 200
    except:
        return "Erro: Parâmetros inválidos", 400

# Rota para multiplicação de dois números
# noinspection PyBroadException
@app.route('/multiplicacao/<numero1>*<numero2>', methods=['GET'])
def multiplicacao(numero1, numero2):
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        return f"Resultado: {numero1 * numero2}", 200
    except:
            return "Erro: Parâmetros inválidos", 400


@app.route('/divisao/<numero1>/<numero2>', methods=['GET'])
def divisao(numero1, numero2):
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        return f"Resultado: {numero1 / numero2}", 200
    except TypeError:
        return "Erro: Parâmetros inválidos", 400
    except ZeroDivisionError:
        return "Divisão por zero não permitida", 400


@app.route('/par_ou_impar/<numero>', methods=['GET'])
def par_ou_impar(numero):
    try:
        numero = int(numero)
        resultado = "par" if numero % 2 == 0 else "ímpar"
        return f"Resultado: {resultado}", 200
    except TypeError:
        return "Erro: Parâmetro inválido", 400

if __name__ == '__main__':
    app.run(debug=True)