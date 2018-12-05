from django.conf.urls import url
from . import views
urlpatterns = [
url('/news',views.news_f,name="news_f")
]
