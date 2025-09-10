"""schema untuk input dan output."""
# TODO Later refactor and move to corresponding service folder

from enum import StrEnum

from pydantic import BaseModel


class ResponseType(StrEnum):
    json = "json"
    html = "html"


class ResponseBase(BaseModel):
    model_config = {"populate_by_name": True, "from_attributes": True}
