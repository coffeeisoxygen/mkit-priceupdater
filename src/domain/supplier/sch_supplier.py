"""schemas for domain supplier."""

from enum import StrEnum

from pydantic import BaseModel


class ResponseType(StrEnum):
    json = "json"
    html = "html"


class SupplierBase(BaseModel):
    model_config = {"populate_by_name": True, "from_attributes": True}


class SupplierCreate(SupplierBase):
    name: str
    url: str
    response_type: ResponseType
    timeout: int = 10
    retry: int = 3
    is_active: bool = False
    product_mapping: dict[str, str] = {}
    status_mapping: dict[str, str] = {}
