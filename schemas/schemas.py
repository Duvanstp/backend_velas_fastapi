from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional

from pydantic import BaseModel, EmailStr, condecimal


# Employee Schemas
class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    role: Optional[str] = None

class EmployeeCreate(EmployeeBase):
    hash_password: str

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int
    class Config:
        from_attributes = True

# Customer Schemas
class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None

class CustomerCreate(CustomerBase):
    hash_password: str

class CustomerUpdate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    class Config:
        from_attributes = True

# Product Schemas
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Annotated[Decimal, condecimal(max_digits=10, decimal_places=2)] = 0.0
    discount: Optional[Annotated[Decimal, condecimal(max_digits=5, decimal_places=2)]] = 0.0
    stock: int
    color: Optional[str] = None
    category: Optional[str] = None
    product_type: Optional[str] = None
    fragrance: Optional[str] = None
    size: Optional[str] = None
    weight: Optional[int] = None
    duration: Optional[int] = None
    materials: Optional[str] = None
    image1: Optional[str] = None
    image2: Optional[str] = None
    image3: Optional[str] = None
    image4: Optional[str] = None
    image5: Optional[str] = None
    image6: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    class Config:
        from_attributes = True

# Inventory Schemas
class InventoryBase(BaseModel):
    product_id: int
    quantity: int
    last_updated: Optional[datetime] = None

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(InventoryBase):
    pass

class InventoryResponse(InventoryBase):
    id: int
    class Config:
        from_attributes = True

# Invoice Schemas
class InvoiceBase(BaseModel):
    customer_id: int
    employee_id: int
    total: Annotated[Decimal, condecimal(max_digits=10, decimal_places=2)] = 0.0
    date: Optional[datetime] = None

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(InvoiceBase):
    pass

class InvoiceResponse(InvoiceBase):
    id: int
    class Config:
        from_attributes = True

# InvoiceDetail Schemas
class InvoiceDetailBase(BaseModel):
    invoice_id: int
    product_id: int
    quantity: int
    subtotal: Annotated[Decimal, condecimal(max_digits=10, decimal_places=2)] = 0.0

class InvoiceDetailCreate(InvoiceDetailBase):
    pass

class InvoiceDetailUpdate(InvoiceDetailBase):
    pass

class InvoiceDetailResponse(InvoiceDetailBase):
    id: int
    class Config:
        from_attributes = True
