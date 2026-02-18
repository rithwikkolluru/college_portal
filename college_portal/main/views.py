from django.shortcuts import render, redirect
from .models import Faculty, Course, Placement
from .forms import RegistrationForm

def home(request):
    faculty = Faculty.objects.all()[:3]
    courses = Course.objects.all()[:3]
    placements = Placement.objects.all()
    return render(request, 'home.html', {
        'faculty': faculty,
        'courses': courses,
        'placements': placements
    })


def faculty_page(request):
    faculty = Faculty.objects.all()
    return render(request, 'faculty.html', {'faculty': faculty})


def courses_page(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def placements_page(request):
    placements = Placement.objects.all()
    return render(request, 'placements.html', {'placements': placements})


def contact_page(request):
    faculty = Faculty.objects.all()
    return render(request, 'contact.html', {'faculty': faculty})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
