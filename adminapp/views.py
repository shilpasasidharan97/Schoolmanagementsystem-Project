from django.shortcuts import render

from adminapp.models import TeacherBasic



# Create your views here.


def home(request):
    return render(request, 'home.html')


def add_teacher(request):
    msg=""
    if request.method=='POST':
        profile=request.FILES['profile']
        name=request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        age=request.POST['age']
        religion=request.POST['religion']
        cast=request.POST['cast']
        place=request.POST['place']
        dist=request.POST['dist']
        nationality=request.POST['nationality']
        adddhar=request.POST['aadhar']
        email=request.POST['email']
        phone_number=request.POST['phn']
        handling_class=request.POST['class']
        subject=request.POST['sub']
        qualification=request.POST['qualification']
        college_name=request.POST['cname']
        quali_certificate=request.FILES['doc1']
        institution_name=request.POST['iname']
        year_of_experience=request.POST['exp']
        exp_certificate=request.FILES['doc2']

        email_exists = TeacherBasic.objects.filter(email_id=email).exists()


        if not email_exists:
            new_teacher=TeacherBasic(t_name=name,gender=gender,dob=dob,age=age,religion=religion,cast=cast,place=place,district=dist,nationality=nationality,aadhar_num=adddhar,email_id=email,phone_number=phone_number,handling_class=handling_class,subject=subject,qualification=qualification,college_name=college_name,quali_certificate=quali_certificate,instituation_name=institution_name,year_of_experience=year_of_experience,experience_certificate= exp_certificate,t_profile=profile)
            new_teacher.save()
            msg = "New teacher added Successfully"
        else:
            msg = "Email already exists"

    return render(request, 'add_teacher.html',{'msg':msg})


def manage_teacher(request):
    return render(request, 'manage_teacher.html')


def add_student(request):
    return render(request, 'add_student.html')


def manage_student(request):
    return render(request, 'manage_student.html')


def add_parents(request):
    return render(request, 'add_parents.html')


def manage_parents(request):
    return render(request, 'manage_parents.html')


def add_class(request):
    return render(request, 'add_class.html')


def class_list(request):
    return render(request, 'class_list.html')
