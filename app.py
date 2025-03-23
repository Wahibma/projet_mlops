from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Charger le modèle
model = pickle.load(open("Models/model.pkl", "rb"))

def model_pred(features):
    """
    Prédit l'éligibilité d'un prêt en fonction des caractéristiques d'entrée.

    Paramètres :
    features (list): Une liste de caractéristiques d'entrée pour le modèle.

    Retourne :
    int: Le résultat de la prédiction (0 ou 1).
    """
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])

@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        features = [
            int(request.form["credit_lines_outstanding"]),
            float(request.form["loan_amt_outstanding"]),
            float(request.form["total_debt_outstanding"]),
            float(request.form["income"]),
            int(request.form["years_employed"]),
            int(request.form["fico_score"])
        ]
        prediction = model_pred(features)

        if prediction == 1:
            prediction_text = "Accorder un prêt à ce client est trop risqué !"
        else:
            prediction_text = "Le client est éligible pour le prêt."

        return render_template("index.html", prediction_text=prediction_text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
