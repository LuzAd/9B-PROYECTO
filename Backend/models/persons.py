from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyGenero(enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"

class MySangre(enum.Enum):
    AP = "A+"
    AN = "A-"
    BP = "B+"
    BN = "B-"
    ABP = "AB+"
    ABN = "AB-"
    OP = "O+"
    ON = "O-"

class Person(Base):
    __tablename__ = 'tbb_personas'

    ID = Column(Integer, primary_key=True, index=True)
    Titulo_Cortesia = Column(String(20))
    Nombre = Column(String(80))
    Primer_Apellido = Column(String(80))
    Segundo_Apellido = Column(String(80))
    Fecha_Nacimiento =Column(DateTime)
    Fotografia = Column(String(100))
    Genero = Column(Enum(MyGenero))
    Tipo_Sangre = Column(Enum(MySangre))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro =Column(DateTime)
    Fecha_Actualizacion =Column(DateTime)
   