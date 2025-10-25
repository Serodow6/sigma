from django.shortcuts import render
from core.models import *
from core.forms import *
from django.views.generic import UpdateView
from django.urls import reverse_lazy

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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.story = Story.objects.get(id=id)
            comment.user = request.user
            comment.save()
    form = CommentForm()
    story = Story.objects.get(id=id)
    categories = Category.objects.all
    tag = Tag.objects.all()
    recent_stories = Story.objects.order_by('-id')[:3]
    context = {
        'data':story,
        'categories':categories,
        'recent_stories':recent_stories,
        'tags':tag,
        'form':form
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
    return render(request,'single_recipe.html',context=context)


def create_story(request):
    if request.method == 'POST':
        form = CreateStoryForm(request.POST,request.FILES)
        if form.is_valid():
            story = form.save()
            story.user = request.user
            story.save()
            return redirect('accounts:user_profile',id=request.user.id)
    form = CreateStoryForm()
    context = {
        'form':form
    }
    return render(request,'create_story.html',context=context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateStoryForm(request.POST,request.FILES)
        if form.is_valid():
            recipe = form.save()
            recipe.user = request.user
            recipe.save()
            return redirect('accounts:user_profile',id=request.user.id)
    form = CreateRecipeForm()
    context = {
        'form':form
    }
    return render(request,'create_recipe.html',context=context)

class EditStory(UpdateView):
    model = Story
    form_class = CreateStoryForm
    template_name = 'create_story.html'
    def get_success_url(self):
        return reverse_lazy('accounts:user_profile',kwargs={'id':self.request.user.id})

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditRecipe(UpdateView):
    model = Recipe
    form_class = CreateRecipeForm
    template_name = 'create_recipe.html'
    def get_success_url(self):
        return reverse_lazy('accounts:user_profile',kwargs={'id':self.request.user.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def delete_story(request,id):
    story = Story.objects.get(id=id)
    story.delete()
    return redirect('accounts:user_profile',id=request.user.id)

def delete_recipe(request,id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('accounts:user_profile',id=request.user.id)