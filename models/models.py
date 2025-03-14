from datetime import datetime

from sqlalchemy import (DECIMAL, Column, DateTime, Float, ForeignKey, Integer,
                        String, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    hash_password = Column(String, nullable=False)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)
    role = Column(String)
    invoices = relationship("Invoice", back_populates="employee")

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    hash_password = Column(String, nullable=False)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)
    invoices = relationship("Invoice", back_populates="customer")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True, unique=True)
    description = Column(Text)
    price = Column(DECIMAL(10, 2))
    discount = Column(DECIMAL(5, 2), default=0.0)
    stock = Column(Integer)
    color = Column(String(50), nullable=True)
    category = Column(String(100), nullable=True)
    product_type = Column(String(100), nullable=True)
    fragrance = Column(String(100), nullable=True)
    size = Column(String(50), nullable=True)
    weight = Column(Integer, nullable=True)
    duration = Column(Integer, nullable=True)
    materials = Column(Text, nullable=True)
    image1 = Column(String, nullable=True)
    image2 = Column(String, nullable=True)
    image3 = Column(String, nullable=True)
    image4 = Column(String, nullable=True)
    image5 = Column(String, nullable=True)
    image6 = Column(String, nullable=True)
    invoice_details = relationship("InvoiceDetail", back_populates="product")

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    last_updated = Column(DateTime, default=datetime.utcnow)
    product = relationship("Product")

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    total = Column(DECIMAL(10, 2), default=0.0)
    date = Column(DateTime, default=datetime.utcnow)
    customer = relationship("Customer", back_populates="invoices")
    employee = relationship("Employee", back_populates="invoices")
    invoice_details = relationship("InvoiceDetail", back_populates="invoice")

class InvoiceDetail(Base):
    __tablename__ = "invoice_details"
    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    subtotal = Column(DECIMAL(10, 2))
    invoice = relationship("Invoice", back_populates="invoice_details")
    product = relationship("Product", back_populates="invoice_details")
