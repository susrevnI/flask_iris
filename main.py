from flask import Flask, jsonify, render_template, request
import os
import predictions

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        dados = request.form

        y_pred = predictions.predict(dados['larg_sepala'],dados['comp_sepala'],dados['larg_petala'],dados['comp_petala'])

        return jsonify(y_pred)
    else:
        return jsonify({"Mensagem":"Utilize o formulario"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
