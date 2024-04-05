from typing import Optional

import shortuuid
from fastapi import APIRouter, Body, HTTPException
from pymongo import ReturnDocument

from database import get_database
from models.student import Student

router = APIRouter()
db = get_database()


@router.post("/students/", status_code=201)
async def create_student(student: Student):
    """
    Create a new student.

    Args:
        student (Student): The student object containing the student details.

    Returns:
        dict: A dictionary containing the ID of the created student.

    """
    student.id = shortuuid.uuid()  # Generate a new short UUID
    student_id = await db.students.insert_one(student.dict())
    return {"student": student.id}


@router.get("/students/")
async def get_students(
    country: Optional[str] = None,
    age: Optional[int] = None,
    page: Optional[int] = 1,
    page_size: Optional[int] = 10,
):
    """
    Retrieve a list of students based on optional filters.

    Parameters:
    - country (Optional[str]): Filter students by country.
    - age (Optional[int]): Filter students by age.
    - page (Optional[int]): Page number for pagination (default: 1).
    - page_size (Optional[int]): Number of students per page (default: 10).

    Returns:
    - dict: A dictionary containing the list of students matching the filters.

    Example:
    {
        "data": [
            {"name": "John", "age": 20},
            {"name": "Jane", "age": 22},
            ...
        ]
    }
    """
    filter_params = {}
    if country:
        filter_params["address.country"] = country
    if age:
        filter_params["age"] = {"$gte": age}

    skip = (page - 1) * page_size
    limit = page_size
    students = (
        await db.students.find(filter_params, {"name": 1, "age": 1, "_id": 0})
        .skip(skip)
        .limit(limit)
        .to_list(limit)
    )
    return {"data": students}


@router.get("/students/{id}")
async def get_student(id: str):
    """
    Retrieve a student by their ID.

    Args:
        id (str): The ID of the student to retrieve.

    Returns:
        dict: A dictionary containing the student object.

    Raises:
        HTTPException: If the student with the given ID is not found.
    """
    student = await db.students.find_one({"id": id})
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    student_obj = Student(**student)
    return {"student": student_obj}


@router.patch("/students/{id}")
async def update_student(id: str, student: dict = Body(...)):
    """
    Update a student record in the database.

    Args:
        id (str): The ID of the student to update.
        student (dict): The updated student data.

    Returns:
        dict: A dictionary containing the updated student object.

    Raises:
        HTTPException: If the student with the given ID is not found.
    """
    updated_student = await db.students.find_one_and_update(
        {"id": id}, {"$set": student}, return_document=ReturnDocument.AFTER
    )
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    student_obj = Student(**updated_student)
    return {"student": student_obj}


@router.delete("/students/{id}")
async def delete_student(id: str):
    """
    Delete a student by their ID.

    Args:
        id (str): The ID of the student to be deleted.

    Returns:
        dict: A dictionary containing a message indicating the success of the deletion.

    Raises:
        HTTPException: If the student with the given ID is not found.
    """
    delete_result = await db.students.delete_one({"id": id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
