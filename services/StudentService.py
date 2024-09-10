import requests

class StudentService:
    BASE_URL = 'https://api-seminario-production.up.railway.app/api'
    
    def get_student(self, student_id):
        response = requests.get(f"{self.BASE_URL}/students/{student_id}")
        return response.json()

    def get_students(self):
        response = requests.get(f"{self.BASE_URL}/students")
        return response.json()

    def add_student(self, student):
        response = requests.post(f"{self.BASE_URL}/students", json=student)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

    def update_student(self, student_id, student):
        response = requests.put(f"{self.BASE_URL}/students/{student_id}", json=student)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

    def delete_student(self, student_id):
        response = requests.delete(f"{self.BASE_URL}/students/{student_id}")
        if response.status_code == 204:
            return True
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return False

    def get_students_not_in_course(self, course_id):
        try:
            response = requests.get(f"{self.BASE_URL}/courses/{course_id}/available-students")
            response.raise_for_status()  # Verifica si hubo un error en la solicitud
            # Intentar decodificar el JSON
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Error occurred: {req_err}")
        except ValueError as json_err:
            print(f"JSON decode error: {json_err}")
        return []  # Devuelve una lista vacía en caso de error
    
    
    def get_students_courses(self):
        response = requests.get(f"{self.BASE_URL}/allstudents/courseslist")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

