from django.shortcuts import render
from core.models import *
from core.forms import *
# Create your views here.

def home(request):
    stories = Story.objects.order_by('-id')[:4]
    recent_story = stories.first()
    categories = Category.objects.all()
    holiday_stories = Story.objects.filter(category__title='Holiday')
    context = {
        'stories' : stories,
        'recent_story' : recent_story,
        'categories':categories,
        'holiday_stories':holiday_stories
    }
    return render(request, 'index.html',context=context)

def stories(request):
    search = request.GET.get('search')
    tag = request.GET.get('tag')
    cate = request.GET.get('cate')
    stories = Story.objects.all()
    if search:
        stories = Story.objects.filter(title__contains=search)
    if cate:
        stories = Story.objects.filter(category__title=cate)
    if tag:
        stories = Story.objects.filter(tags__title=tag)
    categories = Category.objects.all()
    context = {
        'stories' : stories,
        'categories':categories,
    }
    return render(request, 'stories.html',context=context)

def recipes(request):
    search = request.GET.get('search')
    cate = request.GET.get('cate')
    recipe = Recipe.objects.all()
    if search:
        recipe = Recipe.objects.filter(title__contains=search)
    if cate:
        recipe = Recipe.objects.filter(category__title=cate)
    categories = Category.objects.all()
    context = {
        'recipes' : recipe,
        'categories': categories
    }
    return render(request, 'recipes.html',context=context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'contact.html',context=context)


def about(request):
    context = {
        'about' : about,
    }
    return render(request,'about.html',context=context)

def user_profile(request):
    context = {
        'user_profile' : user_profile,
    }
    return render(request,'user-profile.html',context=context)

def story_detail(request,id):
    story = Story.objects.get(id=id)
    categories = Category.objects.all
    tag = Tag.objects.all()
    recent_stories = Story.objects.order_by('-id')[:3]
    context = {
        'data':story,
        'categories':categories,
        'recent_stories':recent_stories,
        'tags':tag
    }
    return render(request,'single.html',context=context) 


def recipe_detail(request,id):
    recipe = Recipe.objects.get(id=id)
    categories = Category.objects.all
    tag = Tag.objects.all()
    recent_stories = Story.objects.order_by('-id')[:3]
    context = {
        'data':recipe,
        'categories':categories,
        'recent_stories':recent_stories,
        'tags':tag
    }
    return render(request,'single.html',context=context)
