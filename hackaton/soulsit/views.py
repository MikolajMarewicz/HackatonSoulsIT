from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import UserRegisterForm
from django.views import View 
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import openai, os
from dotenv import load_dotenv

def home(request):
    return render(request, 'main.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'rgst.html', {'form': form, 'title':'register here'})

def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return redirect('home')
        else:
            messages.info(request, f'account done not exist plz sign in')
            return redirect('register')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

#################chatbot##########
load_dotenv()

api_key = os.getenv('OPENAI_KEY', None)
openai.api_key = api_key

def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        AIuser_input = request.POST.get('AIuser_input')
        prompt = "In your project, based on the description '" + AIuser_input + "', what specialist roles should you have?",
        
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = prompt,
            max_tokens=256,
            stop = None,
            temperature = 0.5
        ) 
        print(response)

        chtextatbot_response = response["choices"][0]["text"]
    return render(request, 'chatbot.html', {"response": chatbot_response})
########################################################################