from flask import Flask, request, render_template
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Dummy training data
# X = area in sq ft, y = price in lakhs
X = np.array([[500], [750], [1000], [1250], [1500], [2000]])
y = np.array([25, 35, 45, 60, 70, 90])

# train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        try:
            area = float(request.form["area"])
            price = model.predict([[area]])[0]
            prediction = round(price, 2)
        except:
            prediction = "Invalid input"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
