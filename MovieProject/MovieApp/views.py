from django.shortcuts import render
from MovieApp.forms import MoviesForm
from MovieApp.models import Movies

# Create your views here.
def index_view(req):
    return render(req,'MovieApp/index.html')

def add_movie_view(request):
    formObj=MoviesForm()
    if request.method=="POST":
        formObj=MoviesForm(request.POST)
        if formObj.is_valid():
            print(formObj.cleaned_data['releasedate'])
            print(formObj.cleaned_data['moviename'])
            print(formObj.cleaned_data['actor'])
            print(formObj.cleaned_data['actress'])
            print(formObj.cleaned_data['rating'])
            formObj.save()	#auto-commit
            return index_view(request)
    return render(request, 'MovieApp/addmovie.html',{'form1':formObj})

def list_movie_view(request):
    movies_list=Movies.objects.all().order_by('-rating') #(-)desc-order
    return render(request,'MovieApp/listmovie.html',{'movies_list':movies_list})

def demo3(req):
    return  render(req,'MovieApp/demo3.html')
def thankyou(req):
    return render(req,'MovieApp/thankyou.html')

def thankyou2(request,v1,v2):
    dict1={"v1":v1,"v2":v2}
    return render(request,'MovieApp/thankyou.html',context=dict1);
