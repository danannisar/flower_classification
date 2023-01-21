from keras_image_helper import create_preprocessor
#import tensorflow.lite as tflite
#change tensorflow with tflite_runtime
import tflite_runtime.interpreter as tflite

interpreter = tflite.Interpreter(model_path='flowers_model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

preprocessor = create_preprocessor('xception', target_size = (299,299))
classes = [
    'daisy',
    'dandelion',
    'rose',
    'sunflower',
    'tulip'
]


url = 'https://www.thespruce.com/thmb/V9sZh_5_x4UwS1BRGmo3TjH7n-c=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/daisy-types-for-gardens-1316051-04-e0f4e84f081d452885752e84bc7886ed.jpg'

# also can use preprocessor.from_path

def predict(url):
    X = preprocessor.from_url(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions =  preds[0].tolist()

    return dict(zip(classes, float_predictions))


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result