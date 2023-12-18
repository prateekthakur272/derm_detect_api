from pydantic import BaseModel

class LoginSchema(BaseModel):
    
    email:str
    password:str
    
    class Config:
        json_schema_extra = {
            'example':{
                'email':'your_email@gmail.com',
                'password':'your_password'
            }
        }