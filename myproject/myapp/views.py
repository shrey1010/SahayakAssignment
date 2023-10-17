from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import jwt

from .models import Teacher, Student, Certificate


def generate_certificate(request, teacher_id, student_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        student = Student.objects.get(pk=student_id)

        certificate_text = f"This is to certify that {student.name} has completed the course with {teacher.name}."

        certificate = Certificate(
            teacher=teacher, student=student, certificate_text=certificate_text)
        certificate.save()

        token = jwt.encode(
            {'teacher_id': teacher_id, 'student_id': student_id}, 'SECRET_KEY', algorithm='HS256')

        return JsonResponse({'certificate_generated': True, 'token': token})
    except Exception as e:
        return JsonResponse({'error': str(e)})


def verify_certificate(request, token):
    try:
        decoded_token = jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])
        teacher_id = decoded_token['teacher_id']
        student_id = decoded_token['student_id']

        certificate_exists = Certificate.objects.filter(
            teacher_id=teacher_id, student_id=student_id).exists()

        if certificate_exists:
            return JsonResponse({'valid_certificate': True})
        else:
            return JsonResponse({'valid_certificate': False, 'error': 'Certificate not found'})
    except jwt.ExpiredSignatureError:
        return JsonResponse({'valid_certificate': False, 'error': 'Token expired'})
    except jwt.DecodeError:
        return JsonResponse({'valid_certificate': False, 'error': 'Invalid token'})
    except Exception as e:
        return JsonResponse({'valid_certificate': False, 'error': str(e)})
