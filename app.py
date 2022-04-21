from flask import Flask, json, Response
from controller.student_controller import app_student
from controller.list_se_controller import app_listse



app = Flask(__name__)
app.register_blueprint(app_student)
app.register_blueprint(app_listse)

if __name__ == '__main__':
    app.run()
