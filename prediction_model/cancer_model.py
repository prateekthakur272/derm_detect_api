from keras.models import load_model
import numpy as np
from keras.preprocessing import image

model = load_model('prediction_model/model.h5')

ALLOWED_EXTENSIONS = ['jpeg','png','jpg']

category={
    0:'benign',1:'malignant'
}


def predict_image(filename):
    img_ = image.load_img(filename, target_size=(128, 128))
    img_array = image.img_to_array(img_)
    img_processed = np.expand_dims(img_array, axis=0)
    img_processed /= 255.

    prediction = model.predict(img_processed)
    index = np.argmax(prediction)
    result = category[index]
    return {'result': result, 'accuracy': float(prediction[0][index])}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
