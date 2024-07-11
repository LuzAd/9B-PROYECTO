from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    Persona_ID = int
    Nombre_Usuario = str
    Correo_Electronico = str 
    Contrasena = str
    Numero_Telefonico_Movil = str 
    Estatus = str
    Fecha_Registro = datetime
    Fecha_Actualizacion = datetime

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    Id: int
    Persona_ID = int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    Nombre_Usuario = str
    Correo_Electronico = str 
    Contrasena = str
    Numero_Telefonico_Movil = str 
