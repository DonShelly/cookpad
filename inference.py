import tensorflow as tf

# Names of Iris categories in correct order for model predictions
class_names = ['Plum', 'Cherry', 'BeefSteak']

MODEL_PATH = './model/tomato_model.h5'


def inference(input):
    model = tf.keras.models.load_model(MODEL_PATH)

    return model(input)


#
# Examples

predict_dataset = tf.convert_to_tensor([
    [5.1, 3.3, 1.7, 0.5, ],
    [5.9, 3.0, 4.2, 1.5, ],
    [6.9, 3.1, 5.4, 2.1]
])

predictions = inference(predict_dataset)

for i, logits in enumerate(predictions):
    class_idx = tf.argmax(logits).numpy()
    p = tf.nn.softmax(logits)[class_idx]
    name = class_names[class_idx]
    print(f'Example {i} prediction: {name} {100*p:.2f}%)')
