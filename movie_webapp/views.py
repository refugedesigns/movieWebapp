from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
# def home(request):
#     movie = Movie.objects.all()    
#     return render(request, 'movie_webapp/home.html', {'movies':movie})

def home(request):
    user_query = str(request.GET.get('query', ''))
    search_result = Movie.objects.filter(name__icontains=user_query)
    context = {'search_result': search_result}    
    return render(request, 'movie_webapp/home.html', context)

def create(request):
    if request.method == "POST":

        name = request.POST['name']
        picture = request.POST['picture']
        released_year = request.POST['released_year']
        rating = request.POST['rating']
        notes = request.POST['notes']

        response = Movie.objects.create(
            name=name,
            picture=picture,
            released_year=released_year,
            rating=rating,
            notes=notes,
        )
        response.save()
        return redirect('/')

def update(request, movie_id): 
    if request.method == "POST":
        
        data = {
        'name':request.POST.get('name'),
        'picture':request.POST.get('picture'),
        'released_year':request.POST.get('released_year'),
        'rating':request.POST.get('rating'),
        'notes':request.POST.get('notes'),
        }
        try:
            edit_movie = Movie.objects.get(id=movie_id)
            edit_movie.name = data.get('name')
            edit_movie.picture = data.get('picture')
            edit_movie.rating = data.get('rating')
            edit_movie.released_year = data.get('released_year')
            edit_movie.notes = data.get('notes')
            edit_movie.save()
        except Exception as e:
            pass

        return redirect('/') 

def delete(request, pk):
    if request.method == "POST":
        delete_movie = Movie.objects.get(id=pk)
        delete_movie.delete()
        return redirect('/')

        
