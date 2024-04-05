from pydantic import BaseModel


class Address(BaseModel):
    """
    Represents an address with city and country information.
    """

    city: str
    country: str
