from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html',)

def players(request):
    data = {
        'players': Player.objects.order_by('-transfer_value'),
    }
    return render(request, 'players.html', data)

def transfers(request):
    data = {
        'transfers': Transfer.objects.all
    }
    return render(request, 'latest-transfers.html', data)

def clubs(request):
    data = {
        'clubs': Club.objects.all
    }
    return render(request, 'clubs.html', data)

def tryouts(request):
    return render(request, 'tryouts.html',)

def about(request):
    return render(request, 'about.html')

def archive(req):
    lst = []
    for i in Transfer.objects.all().values('season').distinct():
        lst.append(i['season'])
    lst.sort()
    data = {
        'seasons': lst,
    }
    # lst = ['2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23']
    # Transfer.objects.all().values('season').distinct() = <QuerySet [{'season': '2022-23'}, {'season': '2021-22'}, {'season': '2020-21'}, {'season': '2017-18'}, {'season': '2018-19'}, {'season': '2019-20'}]>
    return render(req, 'transfer-archive.html', data)

def seasons(req,s):
    data = {
        'transfers': Transfer.objects.filter(season=s),
    }
    return render(req, 'seasons.html', data)

def country(req,s):
    f = Club.objects.filter(country=s)
    
    country = f.values('country')[0]
    country = country['country']
    C = country.upper()

    data = {
        'clubs': f,
        'c': country,
        'C': C,
    }
    
    return render(req, 'country.html', data,)

def countryclubs(req,s):
    data = {
        'players': Player.objects.filter(club__name=s).order_by('-transfer_value'),
        'clubname': s,
    }
    return render(req, 'country-clubs.html', data)

def u20players(req):
    data = {
        'players': Player.objects.filter(age__lte=20).order_by('-transfer_value'),
    }
    return render(req, 'U-20 players.html', data)

def stats(req):
    return render(req, 'stats.html')

def transfer_records(req):
    data = {
        'transfers': Transfer.objects.filter(transfer_fee__gt=50).order_by('-transfer_fee'),
    }
    return render(req, 'stats/transfer-records.html', data)