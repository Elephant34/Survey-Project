from random import randint
from django.shortcuts import render, redirect
from .forms import Response
from .forms import Consent
from .forms import Interview
from .forms import Interview_q
from .forms import Gallery


def landing_page(request):
    if request.method == 'POST':
        form = Consent(request.POST)
        if form.is_valid():
            landing_page = form.save(commit=False)
            landing_page.save()
            if randint(0, 1) == 1:
                return redirect('questionnaire')
            else:
                return redirect('gallery')
    else:
        form = Consent()
    return render(request,'questionnaire/landing_page.html', {'form': form})

def response_form(request):
    #form = ResponseForm()
    if request.method == "POST":
        form = Response(request.POST)
        if form.is_valid():
            questionnaire = form.save(commit=False)
            questionnaire.save()
            return redirect('thankyou')
          
    else:
        form = Response()
    return render(request, 'questionnaire/response_form.html', {'form': form})

#def building(request):
 #   if request.method == "POST":
  #      form = Building(request.POST)
   #     if form.is_valid():
    #        building = form.save(commit=False)
     #       building.save()
      #      return redirect('ty_form_complete')
#    else:
 #       form = Building()
  #  return render(request, 'questionnaire/building.html', {'form':form})

def ty_form_complete(request):
    return render(request,'questionnaire/ty_form_complete.html', {})

def interview(request):
    if request.method == 'POST':
        form = Interview(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.save()
            return redirect('thankyou')
    else:
        form = Interview()
    return render(request,'questionnaire/interview.html', {'form': form})

   # return render(request,'questionnaire/interview.html', {})
# Create your views here.

def interview_q(request):
    if request.method == 'POST':
        form = Interview_q(request.POST)
        if form.is_valid():
            interview_q = form.save(commit=False)
            interview_q.save()
            return redirect('thankyou')
    else:
        form = Interview_q()
    return render(request,'questionnaire/interview_q.html', {'form': form})


def gallery(request):
    if request.method == 'POST':
        form = Gallery(request.POST)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.save()
            return redirect('thankyou')
    else:
        form = Gallery()
    return render(request,'questionnaire/gallery.html', {'form': form})