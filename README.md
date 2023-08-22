
# Doneminder Back

![Doneminder Logo](https://github.com/tandemresistentia/doneminder-front/blob/main/src/assets/Home/logo.png)

**Doneminder Back** is the backend repository for the **Doneminder** project, a task management and reminder application. This repository contains the server-side codebase that powers the Doneminder application, handling user authentication, task management, and communication with the frontend.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Doneminder is designed to help users keep track of tasks, set reminders, and manage their daily schedule effectively. The backend repository, **Doneminder Back**, is built using the Django web framework and interacts with a PostgreSQL database. It provides RESTful API endpoints for communication with the frontend.

## Features

- User registration and authentication
- Create, update, and delete tasks
- Set task due dates and reminders
- Mark tasks as complete
- Get a list of tasks based on different criteria
- User-friendly error handling and validation
- Secure authentication using JSON Web Tokens (JWT)

## Installation

To set up the Doneminder Back project locally, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/tandemresistentia/doneminder-back.git
   ```

2. Navigate to the project directory:

   ```bash
   cd doneminder-back
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Rename `.env.example` to `.env` and configure the environment variables, including your database connection details and any other required settings.

6. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

The server will start running at `http://localhost:8000`.

## Usage

After setting up the project, you can use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to interact with the API endpoints. The frontend of Doneminder can be connected to this backend to provide a complete task management experience.

## API Endpoints

The Doneminder Back API offers the following endpoints:

- `POST /api/register`: Register a new user.
- `POST /api/login`: Authenticate a user and get an access token.
- `GET /api/tasks`: Get a list of tasks for the authenticated user.
- `POST /api/tasks`: Create a new task for the authenticated user.
- `PUT /api/tasks/:taskId`: Update a task's details.
- `DELETE /api/tasks/:taskId`: Delete a task.
- ... (more endpoints based on project features)

For more details on each endpoint, refer to the API documentation in the codebase.

## Database

Doneminder Back uses a PostgreSQL database to store user and task information. The database schema is managed by Django's migrations. You can find information about the database schema within the project's `models.py` files.

## Contributing

Contributions to Doneminder Back are welcome! If you'd like to contribute, please follow the guidelines outlined in the `CONTRIBUTING.md` file.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

For any questions or support, please contact the project maintainers at [contact@doneminder.com](mailto:luismvg41@gmail.com). We hope you find Doneminder Back useful for your task management needs!
