import os
from flask import Flask
from flask import render_template
from mailbox import Message
import smtplib
from email.message import EmailMessage
from services.CourseService import CourseService
from services.StudentService import StudentService

# __name__ is a special variable in Python that is used to determine whether the script is being run on its own or being imported
app = Flask(__name__)

courseService = CourseService()
studentService = StudentService()

@app.route("/")
def show_course_catalogue():
    courses = courseService.get_courses()
    return render_template('course_catalogue.html', courses=courses)

@app.route("/students")
def show_students():
    students = studentService.get_students()
    return render_template('students.html', students=students)

@app.route("/enrollments/<int:course_id>")
def show_enrollments(course_id):
    # With this id get course and students
    
    emailMessage = EmailMessage()
    
    # Cuerpo del correo
    html_content = ""
    with open('templates/email.html', 'r', -1, 'UTF-8') as file:
        html_content = file.read()
        
    emailMessage.add_alternative(html_content, subtype='html')
    emailMessage['Subject'] = 'Inscripción exitosa'
    emailMessage['From'] = os.getenv('EMAIL_SENDER')
    emailMessage['To'] = ''

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv('EMAIL_SENDER'), os.getenv('PASSWORD_SENDER')) 
        smtp.send_message(emailMessage)
    
    print(course_id)
    courses = courseService.get_courses()
    return render_template('enrollments.html', courses=courses)