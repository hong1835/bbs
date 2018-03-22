from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=254)
    category = models.ForeignKey('Category')
    content = models.TextField(max_length=100000)
    author = models.ForeignKey('UserProfile')
    summary = models.TextField(max_length=500)
    #thumb_ups = models.ForeignKey("ThumpUp",blank=True)
    #comments = models.ManyToManyField("Comment",blank=True)
    head_img = models.ImageField(upload_to="statics/imgs/upload")
    publish_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(unique=True,max_length=64)
    admins = models.ManyToManyField("UserProfile")
    def __unicode__(self):
        return self.name

class ThumpUp(models.Model):
    article = models.ForeignKey("Article")
    user = models.ForeignKey("UserProfile")
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.article.title

class Comment(models.Model):
    article = models.ForeignKey("Article")
    user = models.ForeignKey("UserProfile")
    parent_comment = models.ForeignKey("Comment",blank=True,null=True,related_name='pid')
    comment = models.TextField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.comment

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    user_groups = models.ManyToManyField("UserGroup")
    friends = models.ManyToManyField('self',blank=True,related_name='my_friends')
    def __unicode__(self):
        return self.name

class UserGroup(models.Model):
    name = models.CharField(max_length=32,unique=True)
    def __unicode__(self):
        return self.name

