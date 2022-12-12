from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c32f3313a89942c7b86a089006950722"
    top_headlines = requests.get(url).json()
    art = top_headlines['articles']
    title = desc = img = []
    for i in range(len(art)):
        f = art[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(title,desc,img)
    context = {'mylist':mylist}
    return render(request,'index.html',context)