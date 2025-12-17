from django.http import HttpResponse
from django.shortcuts import render, redirect
from contactApp.models import Contactform

def HomePage(request):
  # show recent contacts on index page
  recent = Contactform.objects.order_by('-created_at')[:6]
  return render(request,"index.html", {'recent_contacts': recent})

def aboutPage(req):
  return render(req,"about.html")

def servicePage(req):
  return render(req, 'service.html')

def projectPage(req):
  return render(req, 'project.html')

def blogPage(req):
  return render(req, 'blog.html')

def pricePage(req):
  return render(req,'price.html')

def teamPage(req):
  return render(req,'team.html')

def testimonialPage(req):
  return render(req, 'testimonial.html')



def contactPage(req):
  if req.method == 'POST':
    fullname = req.POST.get('fullname')
    email = req.POST.get('email')
    phone = req.POST.get('phone')
    message = req.POST.get('message')
    image = None
    attachment = None
    if 'image' in req.FILES:
      image = req.FILES['image']
    if 'attachment' in req.FILES:
      attachment = req.FILES['attachment']
    if fullname and email and message:
      Contactform.objects.create(fullname=fullname, email=email, phone=phone, message=message, image=image, attachment=attachment)
      return render(req, 'contact.html', {'success': True})
  return render(req, 'contact.html')
