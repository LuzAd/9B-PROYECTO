from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_-6qDMubGmO3jCgSwQW-@mysql-3b6a263a-apigymdec6.l.aivencloud.com:15406/defaultdb"
#"mysql+pymysql://root:1234@localhost:3306/test"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()