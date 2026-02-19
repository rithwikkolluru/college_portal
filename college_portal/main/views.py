from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Faculty, Course, Placement
from .forms import StudentSignupForm
from .models import StudentRegistration



# PUBLIC PAGES

def home(request):
    faculty = Faculty.objects.all()[:3]
    courses = Course.objects.all()[:3]
    placements = Placement.objects.all()[:3]

    return render(request, 'home.html', {
        'faculty': faculty,
        'courses': courses,
        'placements': placements
    })

@login_required
def faculty_page(request):
    faculty = Faculty.objects.all()
    return render(request, 'faculty.html', {'faculty': faculty})

@login_required
def courses_page(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

@login_required
def placements_page(request):
    placements = Placement.objects.all()
    return render(request, 'placements.html', {'placements': placements})


def contact_page(request):
    return render(request, 'contact.html')


# AUTHENTICATION

def signup_view(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentSignupForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def base(request):
    return render(request, 'base.html',{'base': base})


@login_required
def dashboard_view(request):
    placements = Placement.objects.all()
    return render(request, 'dashboard.html', {'placements': placements})

@login_required
def register_student(request):
    courses = Course.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        course_id = request.POST.get('course')

        if name and email and course_id:
            course = Course.objects.get(id=course_id)

            StudentRegistration.objects.create(
                name=name,
                email=email,
                course=course
            )

            return redirect('dashboard')

    return render(request, 'register.html', {'courses': courses})