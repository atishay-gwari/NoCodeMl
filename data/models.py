from django.db import models
from django import forms
from django.forms import widgets
from django.contrib.auth.models import User



class Dataset(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    file = models.FileField()
    public=models.BooleanField(default=False)

    def __str__(self):
        return self.file.name +" UPLOADED BY " + str(self.user_name)