from django.shortcuts import render, redirect
from .models import BachatGatRegistration, MemberRegistration
import datetime
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request, 'index.html')


def registration(request):
    current_year = datetime.datetime.now().year
    year_range = range(2000, current_year + 1)
    return render(request, 'registration.html', {'year_range': year_range})


def loan_distribution(request):
    return render(request, 'loan-distribution.html')


def loan_management(request):
    return render(request, 'loan-management.html')


def member_registration(request):
    current_year = datetime.datetime.now().year
    year_range = range(2000, current_year + 1)
    return render(request, 'member-registration.html', {'year_range': year_range})


def login(request):
    return render(request, 'login.html')


def loan_deposit(request):
    return render(request, 'loan-deposit.html')

def rules(request):
    return render(request, 'rules.html')

def success_page(request):
    return render(request, 'success.html')




def bachatgat_registration(request):
    current_year = datetime.datetime.now().year
    year_range = range(2000, current_year + 1)
    if request.method == 'POST':
        # Get the data from the form
        bachatgat_name = request.POST.get('bachatgat-name')
        start_month = request.POST.get('start-month')
        start_year = request.POST.get('start-year')
        chairperson_title = request.POST.get('chairperson-title')
        chairperson_name = request.POST.get('chairperson-name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Save the data to the database
        registration = BachatGatRegistration(
            bachatgat_name=bachatgat_name,
            start_month=start_month,
            start_year=start_year,
            chairperson_title=chairperson_title,
            chairperson_name=chairperson_name,
            mobile=mobile,
            email=email,
            password=password
        )
        registration.save()

        # Redirect to a success page or render success message
        return redirect('success_page')  # Change 'success_page' to your actual success page

    return render(request, 'registration.html')





# View for displaying and handling the member registration form
def register_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        entry_month = request.POST.get('entryMonth')
        entry_year = request.POST.get('entryYear')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Save the data into the database
        i=MemberRegistration.objects.create(
            name=name,
            role=role,
            entry_month=entry_month,
            entry_year=entry_year,
            mobile=mobile,
            email=email,
            password=password
        )
        i.save()
        return redirect('/register-member/')  # Redirect to the same page after saving

    # If it's a GET request, display the form with the registered members
    year_range = range(2000, 2025)  # Change this to the range you want for years
    members = MemberRegistration.objects.all()

    return render(request, 'member-registration.html', {'year_range': year_range, 'members': members})




def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Check if the user exists in the MemberRegistration table
        try:
            member = MemberRegistration.objects.get(
                email=email,
                password=password
            )
            # If found, show success message
            messages.success(request, 'Login Successful!')
            return redirect('home')  # Redirect to homepage or dashboard
        except MemberRegistration.DoesNotExist:
            # If no record is found, show invalid message
            messages.error(request, 'Invalid Bachatgat Code, Name, or Password!')
            return redirect('login')  # Reload the login page

    return render(request, 'login.html')

