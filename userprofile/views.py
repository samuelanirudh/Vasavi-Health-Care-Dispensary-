from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import PatientDetailsForm
from .models import PatientDetails
from allauth.socialaccount.models import SocialAccount


# Create your views here.

def home(request):
    return render(request, 'homepage.html', None)

def index(request):
    print(request.user)
    return HttpResponse('welcome, %s' % request.user)

def create(request):
    template = 'index.html'
    form = PatientDetailsForm(request.POST)
    form.first_name = request.POST.get('first_name')
    user_details = SocialAccount.objects.get(user=request.user).extra_data

    if form.is_valid():
        print('valid form')
        form.first_name = form.cleaned_data['first_name']
        form.last_name = form.cleaned_data['last_name']
        form.gender = form.cleaned_data['gender']
        form.date = form.cleaned_data['date']
        form.month = form.cleaned_data['month']
        form.year = form.cleaned_data['year']
        form.email = form.cleaned_data['email']
        form.height = form.cleaned_data['height']
        form.weight = form.cleaned_data['weight']
        form.reason = form.cleaned_data['reason']
        form.prescribed_tablets = form.cleaned_data['prescribed_tablets']
        form.drug_allergies = form.cleaned_data['drug_allergies']
        form.other_illnesses = form.cleaned_data['other_illnesses']
        form.operations = form.cleaned_data['operations']
        form.current_medications = form.cleaned_data['current_medications']

        form.save()

    else:
        print(form.is_valid())
        print(form.errors)

    return render(request, template, {'form': form, 'user_details': user_details})

class PatientDetailsView(TemplateView):
    template = 'patient_details.html'
    #get email from request

    def get(self, request):
        print('this is a GET request')
        print(request.user)

        form = PatientDetailsForm()

        patient_emails = PatientDetails.objects.all().values('email')

        user_details = SocialAccount.objects.get(user=request.user).extra_data
        is_existing_user = False
        patient = {}

        for email in patient_emails:
            if email.get('email') == user_details.get('email'):
                print('request mail = ', email.get('email'), ' user_details mail = ', user_details.get('email'))
                is_existing_user = True
                break

        if is_existing_user:
            print('user exists')
            patient = get_object_or_404(PatientDetails, pk=request.user.email)
            patient.illnesses = str(patient.illnesses).split(',')
            print(patient.illnesses)
        else:
            print('user does not exists')
            return redirect('userprofile:create')

        return render(request, self.template, {'form': form, 'user_details': user_details, 'patient': patient})

    def post(self, request):
        print('this is a POST request')
        form = PatientDetailsForm(request.POST)
        form.first_name = request.POST.get('first_name')
        user_details = SocialAccount.objects.get(user=request.user).extra_data

        if form.is_valid():
            print('valid form')
            form.first_name = form.cleaned_data['first_name']
            form.last_name = form.cleaned_data['last_name']
            form.gender = form.cleaned_data['gender']
            form.date = form.cleaned_data['date']
            form.month = form.cleaned_data['month']
            form.year = form.cleaned_data['year']
            form.email = form.cleaned_data['email']
            form.height = form.cleaned_data['height']
            form.weight = form.cleaned_data['weight']
            form.reason = form.cleaned_data['reason']
            form.prescribed_tablets = form.cleaned_data['prescribed_tablets']
            form.drug_allergies = form.cleaned_data['drug_allergies']
            form.other_illnesses = form.cleaned_data['other_illnesses']
            form.operations = form.cleaned_data['operations']
            form.current_medications = form.cleaned_data['current_medications']

            form.save()

        else:
            print(form.is_valid())
            print(form.errors)

        return render(request, self.template, {'form': form, 'user_details': user_details})