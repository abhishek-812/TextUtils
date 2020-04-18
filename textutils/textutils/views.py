#I have created this file-Abhishek

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  return render(request,'index.html')

#def about(request):
#    return HttpResponse("About")

def analyze(request):
    djtext=request.POST.get('text','default')

    #check checkbox values
    remove=request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newlineremover', 'off')
    space =request.POST.get('extraspaceremover','off')

    if remove=='on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        parse={'purpose':'removed punctuation','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',parse)
    if(fullcap=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        parse = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', parse)

    if(newline=='on'):
        analyzed = ""
        for char in djtext:
            if char !='\n' and char!="\r":
                 analyzed = analyzed + char
        parse = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', parse)

    if(space=='on'):
        analyzed = ""
        for index,char in enumerate(djtext):
           # if djtext[index]== ' ' and djtext[index+1]==" ":
            #   pass
           # else:
               # analyzed = analyzed + char
           #the above code can be written  without using 'pass' function

            if not(djtext[index]== ' ' and djtext[index+1]==" "):
                analyzed = analyzed + char
        parse = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}


    if(remove != 'on' and space!='on'and newline!='on'and fullcap!='on'):
           return HttpResponse("Error")

    return render(request, 'analyze.html', parse)



#def capfirst(request):
 #   return HttpResponse("Capital")

#def spaceremove(request):
 #   return HttpResponse("Space remover <a href='/'>Back</a>")

#def charcount(request):
#    return HttpResponse("Character counter"