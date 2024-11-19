from django.shortcuts import render,redirect
from . models import movie_info
# Create your views here.
from . forms import MovieForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        frm=MovieForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('list')
    else:
        frm=MovieForm()     

    return render(request,'create.html',{'frm':frm})

@login_required(login_url='login')
def edit(request,pk):
    edt=movie_info.objects.get(pk=pk)
    if request.POST:
        frm=MovieForm(request.POST,request.FILES,instance=edt)
        if frm.is_valid():
            edt.save()
    else:
        recent_visits=request.session.get('recent_visits', [])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits
        frm=MovieForm(instance=edt)
    return render(request,'create.html',{'frm':frm})

@login_required(login_url='login')
def list(request):
    recent_visits = request.session.get('recent_visits', [])
    count=request.session.get('count',0)
    count=int(count)
    count=count+1
    request.session['count']=count
    recent_movie_set=movie_info.objects.filter(pk__in=recent_visits)
    movie_set = movie_info.objects.all() # Fetching all movie data from the database
    print(movie_set)  # Printing the data for debugging
    reSponse=render(request,'list.html',{
                     'recent_movie':recent_movie_set,
                      'movies': movie_set, 'visits':count})
    return reSponse  # Rendering the template with the data

@login_required(login_url='login')
def delete_movie(request, pk):
    instance=movie_info.objects.get(pk=pk)
    instance.delete()
    movie_set = movie_info.objects.all()
    return render(request,'list.html',{'movies':movie_set})

