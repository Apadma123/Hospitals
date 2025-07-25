from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, primary_key=True, index=True)
    provider_id = Column(String, index=True, unique=True)
    provider_name = Column(String)
    provider_city = Column(String)
    provider_state = Column(String)
    provider_zip_code = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

class Procedure(Base):
    __tablename__ = "procedures"

    id = Column(Integer, primary_key=True)
    provider_id = Column(String, ForeignKey("providers.provider_id"))
    ms_drg_definition = Column(String, index=True)
    total_discharges = Column(Integer)
    average_covered_charges = Column(Float)
    average_total_payments = Column(Float)
    average_medicare_payments = Column(Float)

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    provider_id = Column(String, ForeignKey("providers.provider_id"))
    rating = Column(Float)
