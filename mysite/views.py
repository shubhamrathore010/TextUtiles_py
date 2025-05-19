from django.http import HttpResponse
from django.shortcuts import render


def anaylze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('anaylze', 'default')
    upper = request.POST.get('upper', 'off')
    NewLine = request.POST.get('NewLineRemove', 'off')
    ExtraSpace = request.POST.get('ExtraSpace', 'off')
    CountChar = request.POST.get('CountChar', 'off')

    if removepunc == "on":
       punchuations = '''!()-[]{}:;`'"\,<>./?@#$%^&_~/'''
       analiazed  = ""
       for char in djtext:
           if char not in punchuations:
              analiazed = analiazed + char

       params = {'purpose': 'REmoves Puctuation', 'analaized_text': analiazed}
       djtext = analiazed

    if(upper == "on"):
        analiazed = ""
        for char in djtext:
            analiazed = analiazed + char.upper()
        params = {'purpose': 'Upper THe CAse', 'analaized_text': analiazed}
        djtext = analiazed
        
    if(NewLine == 'on'):
        analiazed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analiazed = analiazed + char
        params = {'purpose': 'NewLine Remove Texted', 'analaized_text': analiazed}
        djtext = analiazed

    if(ExtraSpace == 'on'):
        analiazed = ""
        for  index, char in enumerate(djtext):
            if not (djtext[index] ==     " " and djtext[index+ 1] == " "):
                analiazed = analiazed + char
        params = {'purpose': 'Extra Space Removed', 'analaized_text': analiazed}
        djtext = analiazed

    if(CountChar == 'on'):
        analiazed = 0
        for char in djtext:
            if char != " ":
               analiazed = analiazed + 1
        params = {'purpose': 'Count of String', 'analaized_text':analiazed}
        djtext = analiazed
    if (upper != "on" and removepunc != "on" and NewLine != 'on' and CountChar != 'on' and ExtraSpace != 'on') :
        return HttpResponse ("Select at least any one operation")

    return render(request, 'analyze.html', params)
def index(request):
    return render(request, 'index.html')

