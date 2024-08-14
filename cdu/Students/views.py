from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import json
import bcrypt
from . import models
import datetime

# Create your views here.
@csrf_exempt
def register_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            address = data.get('address')
            college_id = data.get('college_id')
            password = data.get('password')

            if not all([name, email, phone, address, college_id, password]):
                return JsonResponse({'error': 'All fields are required.'}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            student = models.Student.objects.create(
                name=name, email=email, phone=phone, address=address, college_id=college_id, password=hashed_password
            )
            student.save()

            return JsonResponse({'message': 'Student registered successfully!'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)



@csrf_exempt
def get_all_students(request):
    if request.method == 'GET':
        students = models.Student.objects.all()
        students_list = []
        for student in students:
            students_list.append({
                'name': student.name,
                'email': student.email,
                'phone': student.phone,
                'address': student.address,
                'college_id': student.college_id,
                'created_at': student.created_at,
                'updated_at': student.updated_at
            })
        return JsonResponse({'students': students_list}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    
@csrf_exempt
def update_student(request, college_id):
    if request.method == "PATCH" or request.method == "PUT":
        try:
            data = json.loads(request.body)

            try:
                student = models.Student.objects.get(college_id=college_id)
            except models.Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found.'}, status=404)

            # Update the student fields if provided in the request
            student.name = data.get('name', student.name)
            student.email = data.get('email', student.email)
            student.phone = data.get('phone', student.phone)
            student.address = data.get('address', student.address)

            student.save()  # Save the updated student to the database

            return JsonResponse({'message': 'Student updated successfully!'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)


@csrf_exempt
def delete_account(request, college_id):
    if request.method == "DELETE":
        try:
            # Find the student by college_id
            try:
                student = models.Student.objects.get(college_id=college_id)
            except models.Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found.'}, status=404)

            # Delete the student
            student.delete()

            return JsonResponse({'message': 'Student account deleted successfully!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    
@csrf_exempt
def login_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if not all([email, password]):
                return JsonResponse({'error': 'Email and password are required.'}, status=400)

            # Authenticate user
            student = models.Student.objects.filter(email=email).first()
            if student and bcrypt.checkpw(password.encode('utf-8'), student.password.encode('utf-8')):
                request.session['student_id'] = student.id
                return JsonResponse({'message': 'Login successful!'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid email or password.'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    

@csrf_exempt
def logout_student(request):
    if request.method == 'POST':
        try:
            if 'student_id' in request.session:
                del request.session['student_id']
                return JsonResponse({'message': 'Logout successful!'}, status=200)
            else:
                return JsonResponse({'error': 'You are not logged in.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    return Response({
        'name': user.name,
        'email': user.email,
        'phone': user.phone,
    })