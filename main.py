from fastapi import FastAPI
import uvicorn

description = 'API for Derm-Detect cancer detection application'
title = 'Derm-Detect'
api_route = '/api'

app = FastAPI(
    description=description,
    title=title
)

@app.get(f'{api_route}/index')
def index():
    return {
        'title':title,
        'description':description
    }
    
@app.post(f'{api_route}/auth/login')
def login():
    pass

if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)