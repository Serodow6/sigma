from django.db import models
from accounts.models import User

# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category',related_name='stories',on_delete=models.CASCADE,null=True,blank=True)
    tags = models.ManyToManyField('Tag',related_name='stories',null=True,blank=True)
    user = models.ForeignKey(User,related_name='stories',on_delete=models.CASCADE,null=True,blank=True)
    #comments
    def __str__(self):
        return self.title
        
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category',related_name='recipes',on_delete=models.CASCADE,null=True,blank=True)
    tags = models.ManyToManyField('Tag',related_name='recipes',null=True,blank=True)
    user = models.ForeignKey(User,related_name='recipes',on_delete=models.CASCADE,null=True,blank=True)
    #comments
    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
            return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE,null=True,blank=True)
    story = models.ForeignKey(Story,related_name='comments',on_delete=models.CASCADE,null=True,blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.title

class Contact(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    subject = models.CharField(max_length = 100)
    message = models.TextField()

    def __str__(self):
            return self.name

class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
            return self.title


