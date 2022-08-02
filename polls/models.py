from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    id = models.CharField(max_length=16, primary_key=True, editable=False)
    name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name.username}'
    
    class Meta:
        verbose_name_plural = 'Profiles'
        ordering = ['name']
    
class Question(models.Model):
    id = models.CharField(max_length=16, primary_key=True, editable=False)
    set_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, editable=False)
    question_text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.question_text}'
    
    class Meta:
        verbose_name_plural = 'Questions'
        ordering = ['question_text']
    
class Choice(models.Model):
    id = models.CharField(max_length=16, primary_key=True, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=300, null=True)
    total_votes = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.option}'
    
    class Meta:
        verbose_name_plural = 'Choices'
        ordering = ['option']