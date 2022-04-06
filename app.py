from flask import Flask, json, Response
from controller.student_controller import app_student


app = Flask(__name__)
app.register_blueprint(app_student)

if __name__ == '__main__':
    app.run()
