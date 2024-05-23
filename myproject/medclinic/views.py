from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from .forms import CustomUserCreationForm, AppointmentForm
from .models import Client, Doctor
from django.contrib import messages


def index(request):
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Ваш запрос на встречу успешно отправлен. Спасибо за вашу запись. Мы свяжемся с вами в ближайшее время для подтверждения вашей встречи.')
        else:
            messages.error(request, 'Произошла ошибка при отправке формы. Пожалуйста, попробуйте снова.')
        # Создание новой пустой формы
        form = AppointmentForm()
    else:
        form = AppointmentForm()

    context = {
        'form': form,
        'doctors': doctors,
    }
    return render(request, 'index.html', context)


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'user-register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        return render(request, 'user-register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'user-login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        return render(request, 'user-login.html', {'form': form})



def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные из формы в базу данных
            return redirect('appointment_success')  # Перенаправление на страницу успешной записи
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')
