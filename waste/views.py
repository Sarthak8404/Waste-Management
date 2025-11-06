from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import WasteRequest, WasteCategory, CollectionSchedule
from .forms import WasteRequestForm

def home(request):
    categories = WasteCategory.objects.all()
    schedules = CollectionSchedule.objects.all()
    return render(request, 'waste/home.html', {
        'categories': categories,
        'schedules': schedules
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'waste/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'waste/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')

@login_required
def create_request(request):
    if request.method == 'POST':
        form = WasteRequestForm(request.POST)
        if form.is_valid():
            waste_request = form.save(commit=False)
            waste_request.user = request.user
            waste_request.save()
            messages.success(request, 'Waste pickup request submitted successfully!')
            return redirect('my_requests')
    else:
        form = WasteRequestForm()
    return render(request, 'waste/create_request.html', {'form': form})

@login_required
def my_requests(request):
    requests = WasteRequest.objects.filter(user=request.user)
    return render(request, 'waste/my_requests.html', {'requests': requests})

@login_required
def cancel_request(request, pk):
    waste_request = get_object_or_404(WasteRequest, pk=pk, user=request.user)
    if waste_request.status == 'pending':
        waste_request.status = 'cancelled'
        waste_request.save()
        messages.success(request, 'Request cancelled successfully.')
    else:
        messages.error(request, 'Cannot cancel this request.')
    return redirect('my_requests')