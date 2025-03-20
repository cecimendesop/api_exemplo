from flask import Flask

app = Flask(__name__)

# Rota para soma de dois números
@app.route('/soma/<numero1>+<numero2>', methods=['GET'])
def soma(numero1, numero2):
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        return f"Resultado: {numero1 + numero2}", 200
    except ValueError:
        return "Erro: Parâmetros inválidos", 400

# Rota para subtração de dois números
@app.route('/subtracao/<numero1>-<numero2>', methods=['GET'])
def subtracao(numero1, numero2):
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        return f"Resultado: {numero1 - numero2}", 200
    except ValueError:
        return "Erro: Parâmetros inválidos", 400

# Rota para multiplicação de dois números
@app.route('/multiplicacao/<numero1>*<numero2>', methods=['GET'])
def multiplicacao(numero1, numero2):
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        return f"Resultado: {numero1 * numero2}", 200
    except ValueError:
        return "Erro: Parâmetros inválidos", 400

# Rota para divisão de dois números
@app.route('/divisao/<numero1>/<numero2>', methods=['GET'])
def divisao(numero1, numero2):
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        if numero2 == 0:
            return "Erro: Divisão por zero não permitida", 400
        return f"Resultado: {numero1 / numero2}", 200
    except ValueError:
        return "Erro: Parâmetros inválidos", 400

# Rota para verificar se o número é par ou ímpar
@app.route('/par_ou_impar/<numero>', methods=['GET'])
def par_ou_impar(numero):
    try:
        numero = int(numero)
        resultado = "par" if numero % 2 == 0 else "ímpar"
        return f"Resultado: {resultado}", 200
    except ValueError:
        return "Erro: Parâmetro inválido", 400

if __name__ == '__main__':
    app.run(debug=True)