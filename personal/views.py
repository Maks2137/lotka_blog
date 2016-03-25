from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def diy(request):
    return render(request, 'personal/diy.html')

def about(request):
    return render(request, 'personal/about.html')

def contact(request):
    form_class = ContactForm
    return render(request, 'personal/contact.html', {'form': form_class})
