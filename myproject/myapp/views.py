from django.shortcuts import render
from . models import *
# Create your views here.


def generate_certificate(request, teacher_id, student_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    student = Student.objects.get(pk=student_id)

    certificate_text = f"This is to certify that {student.name} has completed the course with {teacher.name}."

    certificate = Certificate(
        teacher=teacher, student=student, certificate_text=certificate_text)
    certificate.save()

    # Add logic to render a response or redirect to a page.
