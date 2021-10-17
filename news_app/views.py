from django.shortcuts import render
import requests
import json



# Create your views here.

def home(request):

 

  return render(request,'news_app/home.html',context)
  
url =f'https://newsapi.org/v2/top-headlines?country=us&apiKey=da6d944cfb2548339440bd132bfc5c57'
response=requests.get(url)

data=response.json()

articles= data['articles']





context ={

    'articles' : articles
}

