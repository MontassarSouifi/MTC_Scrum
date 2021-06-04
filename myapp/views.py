import datetime

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.template import Context, loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from myapp.UserVerif import UserVerif

@login_required
def dashboard(request):
    backlogs = ProductBacklog.objects.all()
    teams = Team.objects.all()
    IDteams = [Team.objects.all()]
    nbTeams = len(teams)
    users = User.objects.all()
    nbUsers = len(users)
    projects = Project.objects.all()
    nbProjects = len(projects)
    stories = UserStory.objects.all()    
    nbStory = len(stories)
    
    UserName = request.user.get_full_name()
    role = request.user

    return render(None,'dashboard.html', {'backlogs': backlogs, 
    'teams': teams,
    'IDteams':IDteams,
    'nbTeams':nbTeams,
    'nbUsers':nbUsers,
    'nbProjects':nbProjects,
    'nbStory':nbStory,
    'UserName':UserName,
    'Role':role})

@login_required
def liste(request):
    teams = Team.objects.all()
    nbTeams = len(teams)
    projects = Project.objects.filter()
    sprints = Sprint.objects.all()
    UserName = request.user.get_full_name()
    role = request.user
    return render(request,'liste.html', {'teams': teams,
    'nbTeams':nbTeams,
    'UserName':UserName,
    'Role':role,
    'sprints':sprints,
    'projects':projects
    })

@login_required
def forms(request):
    backlogs = ProductBacklog.objects.all()
    UserName = request.user.get_full_name()
    teams = Team.objects.all()
    nbTeams = len(teams)
    role = request.user
    stories = UserStory.objects.all()
    nbBlog= len(backlogs)
    return render(None,'forms.html', {'backlogs': backlogs,
    'stories':stories,
    'nbTeams':nbTeams,
    'UserName':UserName,
    'Role':role,
    'nbBlog':nbBlog,
    })

@login_required
def backlog(request, backlog_id):
    backlog = get_object_or_404(ProductBacklog, pk=backlog_id)
    stories = UserStory.objects.filter(product_backlog=backlog)
    return render(None,'backlog.html', {'backlog': backlog, 'stories': stories})

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def maps(request):
    teams = Team.objects.all()
    nbTeams = len(teams)
    template = loader.get_template('maps.html')
    UserName = request.user.get_full_name()
    role = request.user
    return render(None,'maps.html', {
    'UserName':UserName,
    'nbTeams':nbTeams,
    'Role':role,
    })

def calendar(request):
    teams = Team.objects.all()
    nbTeams = len(teams)
    template = loader.get_template('calendar.html')
    UserName = request.user.get_full_name()
    role = request.user
    return render(None,'calendar.html', {
    'UserName':UserName,
    'nbTeams':nbTeams,
    'Role':role,
    })
