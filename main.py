# Prateek Thakur 2023 Derm Detect

# import packages
from io import BytesIO
from fastapi import FastAPI
import uvicorn
import firebase_admin
from firebase_admin import credentials, auth
import pyrebase
from firebase_config import firebaseConfig
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from keras.models import load_model
from fastapi import UploadFile
# import models
from models.login_schema import LoginSchema
from models.register_schema import RegisterSchema

# prediction model
from prediction_model.cancer_model import predict_image, allowed_file, ALLOWED_EXTENSIONS

description = 'API for Derm-Detect cancer detection application'
title = 'Derm-Detect'
api_route = '/api'

app = FastAPI(
    description=description,
    title=title
)

if not firebase_admin._apps:
    cred = credentials.Certificate("service_firebase.json")
    firebase_admin.initialize_app(cred)
    
firebase = pyrebase.initialize_app(firebaseConfig)

predictor = load_model('prediction_model/model.h5')

@app.get(f'{api_route}/index')
def index():
    return {
        'title':title,
        'description':description
    }
    
@app.post(f'{api_route}/auth/login')
def create_access_token(user_credentials:LoginSchema):
    email = user_credentials.email
    password = user_credentials.password
    
    try:
        user = firebase.auth().sign_in_with_email_and_password(
            email= email,
            password= password
        )
        
        token = user['idToken']
        return JSONResponse(content={
            'token': token
        },status_code=200)
        
    except:
        raise HTTPException(status_code=400, detail= 'invalid credentials')

@app.post(f'{api_route}/auth/register')
def create_account(user_credentials:RegisterSchema):
    email = user_credentials.email
    password = user_credentials.password
    
    try:
        user = auth.create_user(email=email, password=password)
        return JSONResponse(content={
        'message': f'account created successfuly for {email} uid: {user.uid}',
        },status_code=201)
    except auth.EmailAlreadyExistsError:
        raise HTTPException(status_code=400, detail= f'account already exist with email {email}')
    

@app.post(f'{api_route}/auth/ping')
def validate_token(request:Request):
    header = request.headers
    jwt = header.get('authorization')
    user = auth.verify_id_token(jwt)
    return {'uid':user['uid']}

@app.post(f'{api_route}/auth/predict')
def predict(file: UploadFile):
    print(file.filename)
    if allowed_file(file.filename):
        contents = file.file.read()
        bytes_io_object = BytesIO(contents)
        result = predict_image(bytes_io_object)
        return result
    else:
        raise HTTPException(status_code=400, detail= f'only {ALLOWED_EXTENSIONS} are supported')


if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)