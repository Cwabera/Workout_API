from config import db
from sqlalchemy.orm import validates


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)

    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    @validates("title")
    def validate_title(self, key, title):
        if not title or not title.strip():
            raise ValueError("Workout title is required")
        return title

    @validates("date")
    def validate_date(self, key, date):
        if not date or not date.strip():
            raise ValueError("Workout date is required")
        return date


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    category = db.Column(db.String, nullable=False)

    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )

    @validates("name")
    def validate_name(self, key, name):
        if not name or not name.strip():
            raise ValueError("Exercise name is required")
        return name

    @validates("category")
    def validate_category(self, key, category):
        if not category or not category.strip():
            raise ValueError("Exercise category is required")
        return category


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)

    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    duration = db.Column(db.Integer)

    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")

    @validates("sets", "reps", "duration")
    def validate_positive_numbers(self, key, value):
        if value is not None and value <= 0:
            raise ValueError(f"{key} must be a positive number")
        return value