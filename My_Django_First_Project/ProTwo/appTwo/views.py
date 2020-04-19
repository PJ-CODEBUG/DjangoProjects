from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(requestForHelp):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(requestForHelp, 'appTwo/help.html', context=helpdict)
