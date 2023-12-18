# Derm Detect API

## Overview

This repository contains a FastAPI-based API integrated with Firebase for seamless dermatology-related image analysis. The API predicts cancer in images using machine learning algorithms.

## Features

- **FastAPI Framework:** Utilizes the FastAPI framework for building modern, fast, and high-performance APIs with Python.
- **Firebase Integration:** Leverages Firebase services for authentication, database, and storage to enhance functionality and data management.
- **Secure Authentication:** Implements secure user authentication using Firebase Authentication services.
- **RESTful Endpoints:** Provides a set of RESTful endpoints for dermatology image analysis, including cancer prediction.
- **Error Handling:** Includes comprehensive error handling to ensure smooth user experiences and easy debugging.

## Getting Started

### Prerequisites

- Python 3.7 or later
- Firebase credentials
- Install dependencies:

```bash
git clone https://github.com/yourusername/derm-detect.git
cd derm-detect
pipenv install
```

### Run API
```bash
uvicorn main:app --reload
or
python main.py
```

## Documentation
To view api documentation click on [Documentation](http://127.0.0.1:8000/docs)


## Endpoints

### Register
Create user account to use application
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register -H "Content-Type: application/json" -d '{"email": "your_email@example.com", "password": "your_password"}'
```

### Login
Login user with email and password returns jwt
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login -H "Content-Type: application/json" -d '{"email": "your_email@example.com", "password": "your_password"}'
```

### Ping
Login user with email and password returns jwt
```bash
curl -X POST http://127.0.0.1:8000/api/auth/ping -H "Content-Type: application/json" -H "Authorization: your_access_token"
```

