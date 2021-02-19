from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', views.index_template, name='index'),
    path('about_me', views.about_me_template, name='about_me'),
    path('category', views.category_template, name='category'),
    path('link', views.link_template, name='link'),
    path('record', views.record_template, name='record'),
    path('AizuOnlineJudge', views.AizuOnlineJudge, name='Aizu'),
    path('NLP100exercise', views.NLP100, name='NLP100'),
    path('ML_math', views.ML_math, name='ML_math'),
    path('blog_202005', views.blog_202005, name='blog_202005'),
    path('blog_202006', views.blog_202006, name='blog_202006'),
    path('blog_202007', views.blog_202007, name='blog_202007'),
    path('blog_202008', views.blog_202008, name='blog_202008'),
    path('blog_202009', views.blog_202009, name='blog_202009'),
    path('blog_202010', views.blog_202010, name='blog_202010'),
    path('blog_202011', views.blog_202011, name='blog_202011'),
    path('blog_202012', views.blog_202012, name='blog_202012'),
    path('blog_202101', views.blog_202101, name='blog_202101'),
    path('blog_202102', views.blog_202102, name='blog_202102'),
]
