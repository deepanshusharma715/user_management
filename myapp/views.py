from django.shortcuts import render, redirect
from django.contrib.auth import login
from myapp.models import Doctor, Patient
from .forms import UserCreationForm

# Create a view to handle the signup process
def signup(request):
    # If the request is a POST, create a form with the request data
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        # If the form is valid, save the user and log them in
        if form.is_valid():
            user = form.save()
            # Check if the user is a patient or a doctor and create the corresponding object
            if request.POST.get('user_type') == 'patient':
                patient = Patient(user=user)
                patient.save()
            elif request.POST.get('user_type') == 'doctor':
                doctor = Doctor(user=user)
                doctor.save()
            login(request, user)
            # Redirect the user to their respective dashboard based on their type
            if user.patient:
                return redirect('patient_dashboard')
            elif user.doctor:
                return redirect('doctor_dashboard')
    # If the request is not a POST, create an empty form
    else:
        form = UserCreationForm()
    # Render the signup template with the form
    return render(request, 'signup.html', {'form': form})








# Create a view to display the patient dashboard
def patient_dashboard(request):
    # Get the current user and their patient object
    user = request.user
    patient = user.patient
    # Render the patient dashboard template with the user and patient details
    return render(request, 'patient_dashboard.html', {'user': user, 'patient': patient})

# Create a view to display the doctor dashboard
def doctor_dashboard(request):
    # Get the current user and their doctor object
    user = request.user
    doctor = user.doctor
    # Render the doctor dashboard template with the user and doctor details
    return render(request, 'doctor_dashboard.html', {'user': user, 'doctor': doctor})


