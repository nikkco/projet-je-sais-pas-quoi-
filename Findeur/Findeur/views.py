from django.shortcuts import render, redirect 
from Findeur.models import User, Like, Match
from math import sin, cos, sqrt, atan2, radians

def register_view(request): 
    if 'username' in request.GET and 'password' in request.GET and 'password_check' in request.GET and 'gender' in request.GET and 'interest' in request.GET and 'latitude' in request.GET and 'longitude' in request.GET : 
        print('1')
        username = request.GET['username']
        password = request.GET['password']
        password_check = request.GET['password_check']
        gender = request.GET['gender']
        interest = request.GET['interest']
        latitude = request.GET['latitude']
        longitude = request.GET['longitude']
        if password == password_check:
            print('4')
            user = User.objects.filter(username=username)
            if len(user) > 0:
                print("2")
                template_value = {'error_message': 'An user already exists with this username.'} 
                return render(request,'register.html',template_value)
            else:
                print("3")
                new_user = User(username=username, 
                    password=password,
                    gender = gender,
                    interest = interest,
                    longitude = longitude,
                    latitude = latitude,
                    )
                new_user.save()
                return redirect('/login')
        else:    
            template_value = {'error_message': 'The two passwords do not match.'}
            return render(request,'register.html',template_value)
    else:
        return render(request,'register.html')


def login_view(request):
    if 'username' in request.GET and 'password' in request.GET:
        entered_username = request.GET['username']
        entered_password = request.GET['password']
        user = User.objects.filter(username=entered_username).filter(password =entered_password)
        if len(user) == 1:
            request.session['id_user'] = user[0].id 
            return redirect('/welcome')
        else:
            template_value = {'error_message': 'Wrong Username or Password'}
            return render(request, 'login.html', template_value)
    else:
        return render(request, 'login.html')        


def welcome_view(request):
    nom = request.session['id_user']
    user = User.objects.get(pk=nom)
    tutu = User.objects.filter()

    return render(request, 'welcome.html', {'users': tutu,"username":user})


def match_view(request):
    return request
