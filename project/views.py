from django.shortcuts import render 
from django.contrib import messages
from .forms import ContactForm
from django.shortcuts import redirect
from django.urls import reverse

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request , 'Your message is sent')
            return redirect(reverse('home'))
    return render(request , 'index.html')