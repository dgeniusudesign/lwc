from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from .forms import EmailForm, JoinForm
from .models import Join

def get_ip(request):
  try:
    x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forward:
      ip = x_forward.split(",")[0]
    else:
      ip = request.META.get("REMOTE_ADDR")
  except:
    ip = ""
  return ip

# str(user_id)[:11].replace('-','').lower()

import uuid

def get_ref_id():
  ref_id = str(uuid.uuid4())[:11].replace('-','').lower()
  try:
    id_exists = Join.objects.get(ref_id=ref_id)
    get_ref_id()
  except:
    return ref_id

def share(request, ref_id):
  context = {"ref_id": ref_id}
  template = "share.html"
  return render(request, template, context)

def home(request):
  # print request.META.get("REMOTE_ADDR")
  # print request.META.get("HTTP_X_FORWARDED_FOR")
  # # This is using regular Django forms
  # form = EmailForm(request.POST or None)
  # if form.is_valid():
  #   email = form.cleaned_data['email']
  #   new_join, created = Join.objects.get_or_create(email=email)

  # # This is using ModelForm

  try:
    join_id = request.session['join_id_ref']
    obj = Join.objects.get(id = join_id)
  except:
    obj = None

  form = JoinForm(request.POST or None)
  if form.is_valid():
    new_join = form.save(commit=False)
    # There could be manipulations here. And hence the saving is delayed
    email = form.cleaned_data['email']
    new_join_old, created = Join.objects.get_or_create(email=email)
    if created:
      new_join_old.ref_id = get_ref_id()
      if not obj == None:
        new_join_old.friend = obj
      new_join_old.ip_address = get_ip(request)
      new_join_old.save()
    # new_join.ip_address = get_ip(request)
    # new_join.save()
    # Print all those email IDs those were referred by the main sharer
    print Join.objects.filter(friend=obj).count()
    print obj.referral.all()

    return HttpResponseRedirect("/%s" %(new_join_old.ref_id))

  context = {"form": form}
  template = "home.html"
  return render(request, template, context)