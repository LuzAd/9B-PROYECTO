from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyGender(enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"

class MyBlood(enum.Enum):
    AP = "A+"
    AN = "A-"
    BP = "B+"
    BN = "B-"
    ABP = "AB+"
    ABN = "AB-"
    OP = "O+"
    ON = "O-"

class Person(Base):
    __tablename__ = "tbb_personas"

    ID = Column(Integer, primary_key=True, index=True)
    Titulo_Cortesia = Column(String(20))
    Nombre = Column(String(255))
    Primer_Apellido = Column(String(255))
    Segundo_Apellido= Column(String(255))
    Fecha_Nacimiento =Column(Date)
    Fotografia= Column(String(255))
    Genero= Column(String(255))
    Tipo_Sangre= Column(Enum(MyBlood))
    Estatus = Column(Enum(MyBlood))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)