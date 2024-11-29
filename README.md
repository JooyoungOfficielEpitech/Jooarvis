# Task Manager App

A complete Task Manager application with FastAPI backend and a simple HTML/JS frontend.

## Features

- Full CRUD operations for tasks.
- RESTful API with proper validation and error handling.
- Simple frontend for user interaction.

## Backend Setup

1. Install dependencies:
   ```
   pip install fastapi uvicorn
   ```

2. Run the server:
   ```
   uvicorn app.main:app --reload
   ```

3. Run tests:
   ```
   pytest
   ```

## Frontend Setup

1. Open `index.html` in your browser to interact with the API.

## Notes

- Make sure the backend is running before testing the frontend.
