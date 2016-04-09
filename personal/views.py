from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    return render(request, 'personal/home.html')

def diy(request):
    return render(request, 'personal/diy.html')

def about(request):
    return render(request, 'personal/about.html')

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('personal/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "Nowa wiadomość od:",
                content,
                "BLOG LOTKA" +'',
                ['maksym.maksymowicz@op.pl'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact_success.html')

    return render(request, 'personal/contact.html', {
        'form': form_class,
    })

def contact_success(request):
    return render(request, 'personal/contact_success.html')

def cookies(request):
    return render(request, 'personal/cookies.html')
