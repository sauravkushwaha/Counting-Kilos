from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):

    if  request.method == 'POST':
        first_name = request.POST.get['first_name', "default value"]
        last_name = request.POST.get['last_name']
        username = request.POST.get['username']
        email = request.POST.get['email']
        password1 = request.POST.get['password1']
        password2 = request.POST.get['password2']

        if password1==password2:
            if User.objects.filter(username=username).exist():
                print('username taken')
            elif User.objects.filter(email=email).exist():
                print('email taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
        else:
            return redirect('/')

    else:
        return render(request, 'register.html')