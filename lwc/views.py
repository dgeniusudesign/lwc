from django.shortcuts import render

def testhome(request):
  context = {}
  template = "temp.html"
  return render(request, template, context)