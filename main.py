from fastapi import FastAPI
import uvicorn
import firebase_admin
from firebase_admin import credentials
import pyrebase
from firebase_config import firebaseConfig
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

@app.get(f'{api_route}/index')
def index():
    return {
        'title':title,
        'description':description
    }
    
@app.post(f'{api_route}/auth/login')
def login():
    pass

@app.post(f'{api_route}/auth/register')
def register():
    pass

@app.post(f'{api_route}/auth/ping')
def ping():
    pass


if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)