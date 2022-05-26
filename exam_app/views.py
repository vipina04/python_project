from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from exam_app.forms import LoginRegister, StudentRegister,Exam_add,Exams
from exam_app.models import Student


# Create your views here.
def home(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_student:
                return redirect('student_home')
        else:
            messages.info(request, 'INVALID CREDENTIALS')

    return render(request, 'login.html')

def student_register(request):
    user_form = LoginRegister()
    student_form = StudentRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        student_form = StudentRegister(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.is_student = True
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, 'student Register Successful')
            return redirect('login')
    return render(request, 'student_register.html', {'user_form': user_form, 'student_form': student_form})

def exam_view(request):
    data = Exams.objects.all()
    context = {
        'data': data
    }
    return render(request, 'exam_view.html',context)




def student_exam_view(request):
    data = Exams.objects.all()
    context = {
        'data': data
    }
    return render(request, 'student_exam_view.html',context)

def my_profile_view(request,id):
    obj = Student.objects.get(id=id)
    form =StudentRegister(request.POST or None,instance= obj)
    if form.is_valid():
        form.save()
        return redirect('student_home')
    return render (request,'student_view',{'form':form})

def attend(request):
    return render('exam_questions.html')




def student_view(request):
    data = Student.objects.all()
    context = {
        'data':data
    }
    return render(request,'student_view.html',context)

def exam_add(request):
    form = Exan_add()
    a = request.user
    if request.method == 'POST':
        form = Notification_add(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = a
            obj.save()
            messages.info(request,"Exam added successfully")
            return redirect('exam_add')
        else:
            form = Notification_add()
    return render(request, 'exam_add.html', {'form': form})

def admin_home(request):
    return render(request, 'admin_home.html')

def student_home(request):
    return render(request, 'student_home.html')


def exam_add(request):
    form = Exam_add()
    a = request.user
    if request.method == 'POST':
        form = Exam_add(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = a
            obj.save()
            messages.info(request,"exam added successfully")
            return redirect('exam_add')
        else:
            form = Exam_add()
    return render(request, 'exam_add.html', {'form': form})