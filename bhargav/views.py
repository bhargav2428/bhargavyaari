import mysql
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from flask import request, redirect
from pyexpat.errors import messages

from . import urls, models
from django.views.decorators.csrf import csrf_exempt

import mysql.connector as sql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yaswanth",
  database="sys"
)
id=1
def index(request):
    return render(request, 'index.html') 
def login(request):
    if request=='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        return render(request, 'home.html')
    return render(request,'login.html')

def about(request):
  return render(request,'about.html')
def contect(request):
    return render(request,'contact.html')
def  foot(request):
    return render(request,'footer.html')
def  footer(request):
    return render (request,'footer1.html')
def gallery(request):
    return render(request,'gallery.html')
@csrf_exempt
def home(request):
    return render(request,'home.html')
def  nav(request):
    return render(request,'nav0.html')
def nav2(request):
    return render(request,'nav2.html')
def settings(request):
    return  render (request,'setting.html')
@csrf_exempt
def signup(request):
    if(1>0):
        uname = request.POST.get('username','')
        email = request.POST.get('email','')
        pswd = request.POST.get('password','')
        cpswd = request.POST.get('password2','')
        mycursor = mydb.cursor()

        sql = "INSERT INTO regd (username, email,pswd,cpswd) VALUES (%s, %s,%s,%s)"
        val = (uname, email, pswd, cpswd)
        mycursor.execute(sql, val)
        mydb.commit()

    return render (request,'signup.html')
def team(request):
    return render (request,'team.html')
def beach(request):
    return render(request,'beaches.html')
def agra(request):
    return request(request,'Agra.html')
def delhi(request):
    return  render(request,'Delhi.html')
def haridwar(request):
    return  render(request,'Haridwar.html')
def hill(request):
    return  render(request,'hill-station.html')
def history(request):
    return  render(request,'historical.html')
def  honey(request):
    return render (request,'honeymoon.html')
def india(request):
    return render (request,'india.html')

def jaipur(request):
    return render(request,'Jaipur.html')
def mathura(request):
    return render(request,"Mathura.html")
def parks(request):
    return render(request,'parks.html')
def religious(request):
    return render(request,'religious.html')
def  varanasi(request):
    return render(request,'Varanasi.html')
def vrind(request):
    return render(request,'Vrindawan.html')


