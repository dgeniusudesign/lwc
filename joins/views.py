from django.shortcuts import render

# Create your views here.
from .forms import EmailForm, JoinForm
from .models import Join

def home(request):
  # This is using regular Django forms
  form = EmailForm(request.POST or None)
  if form.is_valid():
    email = form.cleaned_data['email']
    new_join, created = Join.objects.get_or_create(email=email)

  # # This is using ModelForm

  # form = JoinForm(request.POST or None)
  # if form.is_valid():
  #   new_join = form.save(commit=False)
  #   # There could be manipulations here. And hence the saving is delayed
  #   new_join.save()

  context = {"form": form}
  template = "home.html"
  return render(request, template, context)