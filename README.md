# Workout Tracker API

## Overview

Workout Tracker API is a Flask-based backend application designed for personal trainers and fitness enthusiasts to manage workouts and exercises.

The application allows users to:

* Create and manage workouts
* Create reusable exercises
* Associate exercises with workouts
* Track sets, reps, and duration for each exercise
* Store and retrieve workout information through a RESTful API

This project demonstrates the use of Flask, SQLAlchemy, Marshmallow, and relational database design principles.

---

## Features

### Workout Management

* Create workouts
* View all workouts
* View a single workout
* Update workout details
* Delete workouts

### Exercise Management

* Create exercises
* View all exercises
* View a single exercise
* Update exercise details
* Delete exercises

### Workout Exercise Tracking

* Assign exercises to workouts
* Track:

  * Sets
  * Reps
  * Duration
* Reuse exercises across multiple workouts

---

## Database Structure

### Workout

| Column | Type    |
| ------ | ------- |
| id     | Integer |
| title  | String  |
| date   | String  |

### Exercise

| Column   | Type    |
| -------- | ------- |
| id       | Integer |
| name     | String  |
| category | String  |

### WorkoutExercise

| Column      | Type    |
| ----------- | ------- |
| id          | Integer |
| workout_id  | Integer |
| exercise_id | Integer |
| sets        | Integer |
| reps        | Integer |
| duration    | Integer |

### Relationships

* A Workout has many WorkoutExercises
* An Exercise has many WorkoutExercises
* A Workout has many Exercises through WorkoutExercises
* An Exercise has many Workouts through WorkoutExercises

---

## Technologies Used

* Python
* Flask
* Flask SQLAlchemy
* Flask Migrate
* Marshmallow
* SQLite
* SQLAlchemy ORM

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Workout_API
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Database Setup

Initialize migrations:

```bash
flask --app app db init
```

Create migration:

```bash
flask --app app db migrate -m "initial migration"
```

Apply migration:

```bash
flask --app app db upgrade
```

Seed the database:

```bash
python seed.py
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The API will be available at:

```txt
http://127.0.0.1:5555
```

---

## API Endpoints

### Workouts

| Method | Endpoint       |
| ------ | -------------- |
| GET    | /workouts      |
| GET    | /workouts/<id> |
| POST   | /workouts      |
| PATCH  | /workouts/<id> |
| DELETE | /workouts/<id> |

### Exercises

| Method | Endpoint        |
| ------ | --------------- |
| GET    | /exercises      |
| GET    | /exercises/<id> |
| POST   | /exercises      |
| PATCH  | /exercises/<id> |
| DELETE | /exercises/<id> |

### Workout Exercises

| Method | Endpoint                |
| ------ | ----------------------- |
| POST   | /workout_exercises      |
| PATCH  | /workout_exercises/<id> |
| DELETE | /workout_exercises/<id> |

---

## Validations

### Workout

* Title is required
* Date is required

### Exercise

* Name is required
* Name must be unique
* Category is required

### WorkoutExercise

* Workout ID is required
* Exercise ID is required
* Sets, reps, and duration must be positive values

---

## Future Improvements

* User authentication
* Trainer profiles
* Workout templates
* Exercise history tracking
* Frontend React integration
* Progress analytics and reporting

---

## Author

Charles Ngatia

Flatiron School Software Engineering Program
