import os

import tensorflow as tf

dir_path = os.path.dirname(os.path.realpath(__file__))
MODEL_PATH = os.path.join(dir_path, 'tomato_model.h5')
class_names = ['Plum', 'Cherry', 'BeefSteak']


def load_model():
    return tf.keras.models.load_model(MODEL_PATH, compile=False)


def predict(model, input_data):
    predictions = model(input_data)
    results = []
    for logits in predictions:
        class_idx = tf.argmax(logits).numpy()
        p = tf.nn.softmax(logits)[class_idx]
        name = class_names[class_idx]
        results.append({"class": name, "confidence": float(p)})
    return results
