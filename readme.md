# Student Management API

This is a FastAPI application for managing students.

## Features

- Create a new student
- Get a list of students

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/yourrepository.git
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

Create the cofig.ini.
```
[DATABASE]
DB_USERNAME = DB_USERNAME1
DB_PASSWORD = DB_PASSWORD1
```


## Usage

1. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

2. Open your browser and visit http://localhost:8000.

## API Endpoints

- `POST /students/`: Create a new student. The request body should be a JSON object with the student details.

- `GET /students/`: Get a list of students. You can filter the students by country and age, and paginate the results.
