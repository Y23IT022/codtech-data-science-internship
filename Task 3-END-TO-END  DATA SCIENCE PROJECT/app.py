from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("house_price_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    features = [
        float(request.form['MedInc']),
        float(request.form['HouseAge']),
        float(request.form['AveRooms']),
        float(request.form['AveBedrms']),
        float(request.form['Population']),
        float(request.form['AveOccup']),
        float(request.form['Latitude']),
        float(request.form['Longitude'])
    ]

    prediction = model.predict([features])[0]

    return render_template(
        "index.html",
        prediction_text=f"Predicted House Price: {prediction:.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)
