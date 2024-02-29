from django.shortcuts import render

# Create your views here.

def index(resquest):
    return render(resquest, 'movies/index.html', {'movie':'gladiator'})


def about(request):
    return render(request, 'movies/about.html', {})


#app/templates/app/index.html
#moveis/templates/movies/index.html