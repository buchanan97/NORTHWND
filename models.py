from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = Column("customerid", String, primary_key=True, index=True)
    company_name = Column("companyname", String)
    contact_name = Column("contactname", String)
    city = Column("city", String)