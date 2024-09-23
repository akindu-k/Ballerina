from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('task_assignment_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    task_data = request.json
    task_df = pd.DataFrame([task_data])  # Create DataFrame from input JSON
    assigned_employee = model.predict(task_df)  # Predict the employee assignment
    return jsonify({"assigned_employee": int(assigned_employee[0])})

if __name__ == '__main__':
    app.run(debug=True)
