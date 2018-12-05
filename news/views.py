from django.shortcuts import render


def news_f(request):
    return render(request,"templates/news/News_temp.html")
