import os
from flask import Flask
from flask import render_template
from mailbox import Message
import smtplib
import requests
from flask import Flask, render_template, request, redirect, url_for
from email.message import EmailMessage
from services.CourseService import CourseService
from services.StudentService import StudentService
from services.EnrollmentService import EnrollmentService


# __name__ is a special variable in Python that is used to determine whether the script is being run on its own or being imported
app = Flask(__name__)

courseService = CourseService()
studentService = StudentService()
EnrollmentService = EnrollmentService()

@app.route("/")
def show_course_catalogue():
    courses = courseService.get_courses()
    return render_template('course_catalogue.html', courses=courses)

@app.route("/students")
def show_students():
    students = studentService.get_students()
    return render_template('students.html', students=students)


@app.route('/students-courses')
def students_courses():
    students_courses = studentService.get_students_courses()
    if students_courses:
        return render_template('students_courses.html', students_courses=students_courses)
    else:
        return "No se pudo obtener la información", 500
    
    
#----------------------------------------------------
@app.route("/students/create", methods=['GET', 'POST'])
def create_student():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        
        student_data = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email
        }
        
        # Asumiendo que add_student acepta un diccionario
        studentService.add_student(student_data)
        
        return redirect(url_for('show_students'))
    
    return render_template('create_student.html')
#----------------------------------------------------

@app.route("/enrollments/<int:course_id>", methods=['GET', 'POST'])
def show_enrollments(course_id):
    if request.method == 'POST':
        student_id = request.form['student_id']
        
        # Llamar a la función correcta de EnrollmentService
        result = EnrollmentService.enroll_student(course_id, student_id)
        
        if result:
            # Enviar correo electrónico si la inscripción es exitosa
            emailMessage = EmailMessage()
            html_content = ""
            with open('templates/email.html', 'r', -1, 'UTF-8') as file:
                html_content = file.read()
                
            emailMessage.add_alternative(html_content, subtype='html')
            emailMessage['Subject'] = 'Inscripción exitosa'
            emailMessage['From'] = os.getenv('EMAIL_SENDER')
            emailMessage['To'] = 'destinatario@example.com'  # Cambia esto según sea necesario
            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(os.getenv('EMAIL_SENDER'), os.getenv('PASSWORD_SENDER')) 
                smtp.send_message(emailMessage)
            
            return redirect(url_for('show_course_catalogue'))
        else:
            return "Error al inscribir al estudiante", 500
    
    # Obtener la lista de estudiantes para mostrar en el formulario
    students = studentService.get_students()
    return render_template('enrollments.html', course_id=course_id, students=students)