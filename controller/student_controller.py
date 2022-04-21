from flask import Blueprint, Response,json
from service.student_service import StudentService
from util.util import MyEncoder

app_student = Blueprint('app_student',__name__)
studentService= StudentService()

@app_student.route('/student')
def getAllStudents():
    return Response(response=json.dumps(studentService.getAllStudents(),
                                        cls=MyEncoder),
                    status=200,
                    mimetype='application/json')
@app_student.route('/student/percentagebygender/<gender>')
def get_percentage_by_gender(gender):
    return str(studentService.get_percentage_by_gender(gender))

@app_student.route('/student/<gender>/<salary>')
def get_students_by_gender_and_salary(gender, salary):
    return Response(response=json.dumps(
        studentService.get_students_by_gender_and_salary(gender, int(salary)), cls=MyEncoder),
                    status=200, mimetype='application/json')
@app_student.route('/between/<min_salary>/<max_salary>')
def get_students_between_salaries(min_salary,max_salary):
    return Response(response=json.dumps(
        studentService.get_students_between_salaries(min_salary,max_salary), cls=MyEncoder),
        status=200, mimetype='application/json')
@app_student.route('/student/<gender>')
def get_mayor_salaries(gender):
    return Response(response=json.dumps(
        studentService.get_mayor_salaries(gender),cls=MyEncoder),
        status=200, minetype='application/jason')





