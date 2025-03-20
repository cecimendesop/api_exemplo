from flask import Flask

app = Flask(__name__)

# Rota para soma de dois números
@app.route('/soma', methods=['GET'])
def soma():
    try:
        numero1 = float(request.args.get('numero1'))
        numero2 = float(request.args.get('numero2'))
        return f"Resultado: {numero1 + numero2}", 200
    except:
        return "Erro: Parâmetros inválidos", 400

# Rota para subtração de dois números
@app.route('/subtracao', methods=['GET'])
def subtracao():
    try:
        numero1 = float(request.args.get('numero1'))
        numero2 = float(request.args.get('numero2'))
        return f"Resultado: {numero1 - numero2}", 200
    except:
        return "Erro: Parâmetros inválidos", 400

# Rota para multiplicação de dois números
@app.route('/multiplicacao', methods=['GET'])
def multiplicacao():
    try:
        numero1 = float(request.args.get('numero1'))
        numero2 = float(request.args.get('numero2'))
        return f"Resultado: {numero1 * numero2}", 200
    except:
        return "Erro: Parâmetros inválidos", 400

# Rota para divisão de dois números
@app.route('/divisao', methods=['GET'])
def divisao():
    try:
        numero1 = float(request.args.get('numero1'))
        numero2 = float(request.args.get('numero2'))
        if numero2 == 0:
            return "Erro: Divisão por zero não permitida", 400
        return f"Resultado: {numero1 / numero2}", 200
    except:
        return "Erro: Parâmetros inválidos", 400

# Rota para verificar se o número é par ou ímpar
@app.route('/par_ou_impar', methods=['GET'])
def par_ou_impar():
    try:
        numero = int(request.args.get('numero'))
        resultado = "par" if numero % 2 == 0 else "ímpar"
        return f"Resultado: {resultado}", 200
    except:
        return "Erro: Parâmetro inválido", 400

if __name__ == '__main__':
    app.run(debug=True)
