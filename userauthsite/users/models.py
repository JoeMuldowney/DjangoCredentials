
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MemberProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    profile_description = models.TextField(max_length=225,null=True)
    fav_book = models.CharField(max_length=45,null=True)
    cur_book = models.CharField(max_length=45,null=True)
    fav_author = models.CharField(max_length=45,null=True)
    fav_genres = models.CharField(max_length=45,null=True)
    public = models.BooleanField(default=False)



    class Meta:
        app_label = 'users'
