import tensorflow as tf

MODEL_PATH = './app/model/tomato_model.h5'
class_names = ['Plum', 'Cherry', 'BeefSteak']


def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


def predict(model, input_data):
    predictions = model(input_data)
    results = []
    for logits in predictions:
        class_idx = tf.argmax(logits).numpy()
        p = tf.nn.softmax(logits)[class_idx]
        name = class_names[class_idx]
        results.append({"class": name, "confidence": float(p)})
    return results
