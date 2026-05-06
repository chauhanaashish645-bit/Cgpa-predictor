from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Dummy data
np.random.seed(42)
cgpa = np.random.uniform(5, 10, 200)
package = 2 * cgpa + np.random.normal(0, 1, 200)

# Train model
model = LinearRegression()
model.fit(cgpa.reshape(-1,1), package)
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        pkg = float(request.form['package'])
        cgpa_pred = (pkg - model.intercept_) / model.coef_[0]
        prediction = round(cgpa_pred, 2)

    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

