from django.shortcuts import render, redirect, reverse
from .models import *
from django.db.models import Count
from django.contrib import messages
from .helpers import send_forget_password_mail


# Create your views here.

def home(request):
    logo_obj = websitename.objects.all()
    features_obj = features.objects.all()
    media_obj = socialmedia.objects.all()
    name = tutorialssports.objects.all()
    return render(request,'home.html',{'logo_obj':logo_obj,'features_obj':features_obj,'media_obj':media_obj,'name':name})

def tutorial(request):
    logo_obj = websitename.objects.all()
    name = tutorialssports.objects.all()
    media_obj = socialmedia.objects.all()
    position_obj = sportsposition.objects.all()
    return render(request,'tutorial.html',{'logo_obj':logo_obj,'name':name,'media_obj':media_obj,'position_obj':position_obj})

def tutorialvideo(request,sports):
    logo_obj = websitename.objects.filter()
    sports_obj = tutorialssports.objects.filter(name = sports)
    media_obj = socialmedia.objects.all()
    position_obj = (sportsposition.objects
        .filter(name = sports)
        .annotate(dcount=Count('position'))
        .order_by()
    )
    tutorial_obj = (tutorialvideos.objects
        .values('position','tutorial',)
        .annotate(dcount=Count('tutorial'))
        .order_by()
    )
    all = tutorialvideos.objects.filter(name = sports)
    name = tutorialssports.objects.all()

    return render(request,'tutorial-videos.html',{'name':name,'all':all,'logo_obj':logo_obj,'sports_obj':sports_obj,'sports':sports,'position_obj':position_obj,'tutorial_obj':tutorial_obj,'media_obj':media_obj})

def addvideo(request):
    sports_obj = tutorialssports.objects.all()
    position_obj = sportsposition.objects.all()
    if request.method == 'POST':
        sports = request.POST.get('sports')
        icon = request.FILES.get('icon')
        sportsimg = request.FILES.get('sportsimage')
        position = request.POST.get('position')
        positionimg = request.FILES.get('positionimage')
        tutorial = request.POST.get('tutorial')
        videoname = request.POST.get('videoname')
        link = request.POST.get('link')
        return redirect(reverse('adminhome'))
    return render(request,'add-video.html',{'sports_obj':sports_obj,'position_obj':position_obj})

def knowledge(request):
    return render(request,'knowledge.html')

def trainingHome(request):
    return render(request,'trainingHome.html')

def footballOverview(request):
    return render(request,'football-Overview.html')

def football(request):
    return render(request,'football.html')

def footballParticipatingCountiries(request):
    return render(request,'football-participating-countries.html')

def footballPlayingEnvironment(request):
    return render(request,'football-playing-environment.html')

def footballEquipment(request):
    return render(request,'football-equipment.html')

def footballPopularTerms(request):
    return render(request,'football-popular-terms.html')

def footballPlayersAndPositions(request):
    return render(request,'football-players-and-positions.html')

def footballHowToPlay(request):
    return render(request,'football-how-to-play.html')

def cricketOverview(request):
    return render(request,'cricket-overview.html')

def cricketBatAndBall(request):
    return render(request,'cricket-bat-and-ball.html')

def cricketParticipatingCountries(request):
    return render(request,'cricket-participating-countries.html')

def cricketPlayingEnvironment(request):
    return render(request,'cricket-playing-environment.html')

def cricketEquipment(request):
    return render(request,'cricket-equipment.html')
    
def PopularTermsinCricket(request):
    return render(request,'cricket-popular-terms.html')

def howToPlayCricket(request):
    return render(request,'cricket-how-to-play.html')

def cricketFormat(request):
    return render(request,'cricket-format.html')



def videoTutorialHome(request):
    return render(request,'video-tutorial-home.html')

def tutorialHome(request):
    return render(request,'tutorial-home.html')


def login(request):
    if request.method == 'POST':
        mail = request.POST.get('email')
        pas = request.POST.get('password')
        print('HFUAERBGGBYRBV')
        if admindata.objects.filter(email=mail, password=pas).exists():
            print('HFUAERBGGBYRBV')
            return redirect(reverse('adminhome'))
        if register.objects.filter(email=request.POST.get('email')).exists():
            if register.objects.filter(email=request.POST.get('email'),password=request.POST.get('password')).exists():
                return redirect(reverse('adminhome'))
            else:
                messages.error(request,'The password did not match! ')
                return render(request,'login.html')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def registe(request):
    if request.method == 'POST':
        fname = request.POST.get('firstName')
        sname = request.POST.get('secondName')
        mail = request.POST.get('email')
        p = request.POST.get('psw')
        if register.objects.filter(email=request.POST.get('email')).exists():
            messages.error(request,'this email account has been already registered!')
            return render(request,'login.html')
        else:
            reg = register.objects.create(first_name=fname,second_name=sname,email=mail,password=p)
            messages.success(request,'Your account registered successfully')
            return render(request,'login.html')
    else:
        return render(request,'register.html')

import uuid 
def forgetPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not register.objects.filter(email=email).first():
            messages.success(request,'No user found with this email id')
            return render(request, 'forget-password.html')

        register_obj = register.objects.get(email = email)
        token  = str(uuid.uuid4()) 
        register_obj.password=token
        register_obj.save()
        reg_email = register_obj.email
        send_forget_password_mail(reg_email, token)
        messages.success(request,'An email is sent')
        # print(reg_email)
        return render(request, 'forget-password.html')

    return render(request, 'forget-password.html')

def changepassword(request, token):
    context = {}
    register_obj = register.objects.get(password = token)
    context = { 'user_id' : register_obj.id }
    print(register_obj.email)

    if request.method == 'POST':
        pas = request.POST.get('password')
        uid = request.POST.get('user_id')
        if uid is None:
            messages.success(request,'User not found')
            return render(request,'change-Password.html',context)
        register_obj.password = pas
        register_obj.save()
        messages.success(request,'Password changed successfully')
        return render(request,'login.html')


    return render(request,'change-Password.html',context)

def updatelogo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        logo = request.FILES.get('logo')
        upd_obj = websitename.objects.get()
        upd_obj.name = name
        upd_obj.logo = logo
        upd_obj.save()
        messages.success(request,"The logo is updated successfully!")
        return render(request, 'admin-home.html')
    return render(request,'update-logo.html')

def adminhome(request):
    return render(request, 'admin-home.html')

def addfeatures(request):
    if request.method == 'POST':
        feature = request.POST.get('features')
        if features.objects.filter(featurename = feature).exists():
            messages.error(request,'This Feature already exists!')
            return render(request,'add-features.html')
        image = request.FILES.get('image')
        desc = request.POST.get('description')
        features.objects.create(featurename=feature,image=image,description=desc)
        messages.success(request,"A new feature added successfully!")
        return redirect(reverse('adminhome'))
    return render(request,'add-features.html')


def updatefeatures(request):
    features_obj = features.objects.all()
    if request.method=="POST":
        feature = request.POST.get('features')
        image = request.FILES.get('image')
        desc = request.POST.get('description')
        print(feature)
        if features.objects.filter(featurename = feature).exists():
            selected_obj = features.objects.get(featurename = feature)
            selected_obj.image = image
            selected_obj.description = desc
            selected_obj.save()
            messages.success(request,"Selected feature's datas are updated")
            return redirect(reverse('adminhome'))
        messages.error(request,"Selected feature doesn't exist!")
    return render(request,'update-features.html',{'features_obj':features_obj})


def deletefeatures(request):
    features_obj = features.objects.all()
    if request.method=="POST":
        feature = request.POST.get('features')
        if features.objects.filter(featurename = feature).exists():
            selected_obj = features.objects.get(featurename = feature)
            selected_obj.delete()
            messages.success(request,"selected feature deleted successfully")
            return redirect(reverse('adminhome'))
        messages.error(request,"Selected feature doesn't exist!")
    return render(request,'delete-features.html',{'features_obj':features_obj})


def deletesocialmedia(request):
    media_obj = socialmedia.objects.all()
    if request.method=="POST":
        name = request.POST.get('socialmedia')
        if socialmedia.objects.filter(name = name).exists():
            selected_obj = socialmedia.objects.get(name = name)
            selected_obj.delete()
            messages.success(request,"selected socialmedia deleted successfully")
            return redirect(reverse('adminhome'))
        messages.error(request,"Selected socialmedia doesn't exist!")
    return render(request,'delete-socialmedia.html',{'media_obj':media_obj})


def addsocialmedia(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if socialmedia.objects.filter(name = name).exists():
            messages.error(request,'This social media already included!')
            return render(request,'add-socialmedia.html')
        icon = request.FILES.get('icon')
        link = request.POST.get('link')
        socialmedia.objects.create(name=name,icon=icon,link=link)
        messages.success(request,"A new social media added successfully!")
        return redirect(reverse('adminhome'))
    return render(request,'add-socialmedia.html')

def updatesocialmedia(request):
    media_obj = socialmedia.objects.all()
    if request.method=="POST":
        name = request.POST.get('name')
        icon = request.FILES.get('icon')
        link = request.POST.get('link')
        if socialmedia.objects.filter(name = name).exists():
            media_obj = socialmedia.objects.get(name = name)
            media_obj.icon = icon
            media_obj.link = link
            media_obj.save()
            messages.success(request,"Selected social media datas are updated")
            return redirect(reverse('adminhome'))
        messages.error(request,"Selected socialmedia doesn't exist!")
    return render(request,'update-socialmedia.html',{'media_obj':media_obj})


def edit(request):
    return render(request,'edit.html')