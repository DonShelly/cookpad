from flask import Flask, request, jsonify
import numpy as np
from app.model.load_model import load_model, predict

app = Flask(__name__)

model = load_model()


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    data = request.get_json()
    input_data = np.array([[data['feature1'], data['feature2'], data['feature3'], data['feature4']]])
    predictions = predict(model, input_data)
    return jsonify(predictions)


if __name__ == '__main__':
    app.run(debug=True)
