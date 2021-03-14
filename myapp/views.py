from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index_template(request):
    return render(request, 'index.html')

def about_me_template(request):
    return render(request, 'about_me.html')

def category_template(request):
    return render(request, 'category.html')

def link_template(request):
    return render(request, 'link.html')

def record_template(request):
    return render(request, 'record.html')

def AizuOnlineJudge(request):
    return render(request, 'AizuOnlineJudge/AizuOnlineJudge.html')

def NLP100(request):
    return render(request, 'NLP100/NLP100exercise.html')

def ML_math(request):
    return render(request, 'ML_math/ML_math.html')

def blog_202005(request):
    return render(request, 'blog/2020/202005.html')

def blog_202006(request):
    return render(request, 'blog/2020/202006.html')

def blog_202007(request):
    return render(request, 'blog/2020/202007.html')

def blog_202008(request):
    return render(request, 'blog/2020/202008.html')

def blog_202009(request):
    return render(request, 'blog/2020/202009.html')

def blog_202010(request):
    return render(request, 'blog/2020/202010.html')

def blog_202011(request):
    return render(request, 'blog/2020/202011.html')

def blog_202012(request):
    return render(request, 'blog/2020/202012.html')

def blog_202101(request):
    return render(request, 'blog/2021/202101.html')

def blog_202102(request):
    return render(request, 'blog/2021/202102.html')

def blog_202103(request):
    return render(request, 'blog/2021/202103.html')
