from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'app/index.html', context)

def detail(request, id):
    context = {}
    return render(request, 'app/detail.html', context)

def create(request):
    context = {}
    return render(request, 'app/create.html', context)

def update(request, id):
    context = {}
    return render(request, 'app/update.html', context)

def delete(request, id):
    context = {}
    return render(request, 'app/delete.html', context)

def load(request):
    # 🧀🥞🥪🌮🥗
    new = Recipe.objects.create()
    
# def signup(request, id):
#     context = {}
#     return render(request, 'app/delete.html', context)