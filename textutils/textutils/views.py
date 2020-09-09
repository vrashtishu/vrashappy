from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get("text",'none')
    removepunc=request.POST.get("removepunc",'off')
    fullcaps=request.POST.get("fullcaps",'off')
    newlineremove=request.POST.get("newlineremove",'off')
    extraspaceremove=request.POST.get("extraspaceremove",'off')
    charcount=request.POST.get("charcount",'off')

    if removepunc=="on":
        analyzed_text=""
        punc='''!()-[]{};:'",<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punc:
                analyzed_text=analyzed_text+char

        params={'purpose':'Remove Punctuation','analyzed_text':analyzed_text}
        djtext=analyzed_text
       
    if fullcaps=="on":
        analyzed_text=""
        for char in djtext:
            analyzed_text=analyzed_text+char.upper()

        params={'purpose':'UPPER CASE','analyzed_text':analyzed_text}
        djtext=analyzed_text
    
    if newlineremove=="on":
        analyzed_text=""
        for char in djtext:
            if char!="\n" and char!='\r':
                analyzed_text=analyzed_text+char

        params={'purpose':'New Line Remove','analyzed_text':analyzed_text}
        djtext=analyzed_text
 
    if extraspaceremove=="on":
        analyzed_text=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed_text=analyzed_text+char

        params={'purpose':'Extra Space Remove','analyzed_text':analyzed_text}
        djtext=analyzed_text
 
    if charcount=="on":
        l=len(djtext)
        params={'purpose':'Character Count','analyzed_text':l}
        
    if(charcount!="on" and extraspaceremove!="on" and newlineremove!="on" and removepunc!="on" and fullcaps!="on"):
        return HttpResponse("Error ! please Select any checkbox")

    return render(request, 'analyze.html',params)
