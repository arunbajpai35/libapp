from typing import Optional

from pydantic import BaseModel

from models.address import Address


class Student(BaseModel):
    """
    Represents a student in the library app.

    Attributes:
        id (Optional[str]): The unique identifier of the student.
        name (str): The name of the student.
        age (int): The age of the student.
        address (Address): The address of the student.
    """

    id: Optional[str] = None
    name: str
    age: int
    address: Address
