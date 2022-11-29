from fastapi import FastAPI, UploadFile
import uvicorn
import tensorflow as tf
import numpy as np
import io
from tensorflow.keras.preprocessing import image


MODEL = tf.keras.models.load_model('autistic_model/')

app = FastAPI()

@app.get('/')
async def index():
    return {"Message": "This is Index"}

@app.post('/autistic')
async def predic(file: UploadFile) -> str:
    upload = await file.read()
    content = io.BytesIO(upload)


    img = image.load_img(content, target_size=(150,150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    classes = MODEL.predict(images)

    if classes==0:
        return "Autistic Child"
    else:
        return "Non-Autistic Child"