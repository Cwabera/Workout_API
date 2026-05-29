from flask import Flask
from config import db, migrate
from models import Workout, Exercise, WorkoutExercise

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///workout.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)

@app.route("/")
def home():
    return {"message": "Welcome to the Workout API"}

if __name__ == "__main__":
    app.run(port=5555, debug=True)