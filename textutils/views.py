# I have created this file - Deepak
import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


# Code for video 6
# def index(request):
#     # f = open('1.txt')
#     # text = f.read()
#     # f.close()
#     # return HttpResponse(text)
#     return HttpResponse('''<a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index"> Django Playlist </a>''')
#     # file_ = open(os.path.join(settings.BASE_DIR, '1.txt'))
#     # with open('1.txt', 'r+') as file:
#     #     content = file.read()
#     # return HttpResponse(file_)
#     # return HttpResponse("<h1>Hello Deepak Learning Django</h1>")

# def about(request):
#     return HttpResponse("This is about page of Django")

def index(request):
    # params = {'name': 'deepak', 'place': 'Khatima'}
    # return render(request, 'index.html', params)
    return render(request, 'index.html')
    # return HttpResponse("Home")

# def removepunc(request):
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     return HttpResponse('''<a href="/">remove punc</a>''')

def capitalizefirst(request):
    return HttpResponse("capitalize first")

# def newlineremove(request):
#     return  HttpResponse("the text will be newlineremove/n <a href='http://127.0.0.1:8000/'>HOME</a>")

def newlineremove(request):
    return HttpResponse('''<a href="/">newline remove first</a>''')

def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount")


###########################################################################################################
###########################################################################################################

def ex1(request):
    # s = ''' Navigation Bar <br> </h2>
    #     <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    #     <a href="https://www.facebook.com/"> Facebook </a> <br>
    #     <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    #     <a href="https://www.hindustantimes.com/"> News </a> <br>
    #     <a href="https://www.google.com/"> Google </a> <br>'''
    # return HttpResponse(s)
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    flag = True if "on" in [removepunc, fullcaps, newlineremover, extraspaceremover, charcounter] else False
    purpose=""
    tempstr=djtext
    if removepunc=="on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in tempstr:
            if char not in punctuations:
                analyzed+=char
        print('analyzed:', analyzed)
        tempstr = analyzed
        purpose += "| Remove Punctuations |"

    if(fullcaps=="on"):
        analyzed=""
        for char in tempstr:
            analyzed+=char.upper()
        tempstr = analyzed
        purpose += "| Change to Uppercase |"

    if(newlineremover=="on"):
        analyzed = ""
        for char in tempstr:
            if char!="\n" and char!="\r":
                analyzed += char
        tempstr = analyzed
        purpose+="| Remove NewLine |"

    if (charcounter == "on"):
        # analyzed=('No. of characters given in the text are : '+str(len(analyzed)))
        analyzed=""
        purpose += "| Character Counter |"
        analyzed+=' No. of characters given in the text are : '+str(len(tempstr))
        tempstr+=analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(tempstr):
            if not (tempstr[index] == " " and tempstr[index + 1] == " "):
                analyzed = analyzed + char
        tempstr = analyzed

    params = {'purpose': purpose, 'analyzed_text': tempstr}
    if flag:
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
