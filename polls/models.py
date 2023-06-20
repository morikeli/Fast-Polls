from accounts.models import User
from django.db import models


class Questions(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    quiz = models.TextField(blank=False)
    category = models.CharField(max_length=7, blank=False, default='Public')
    close_voting = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}'
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Questions'

class Choices(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, editable=False)
    choice = models.CharField(max_length=100, blank=False)
    total_votes = models.PositiveIntegerField(default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.choice}'
    
    class Meta:
        ordering = ['total_votes']
        verbose_name_plural = 'Choices'

class VotersDetails(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    polls = models.ForeignKey(Choices, on_delete=models.CASCADE, editable=False)
    selected_choice = models.CharField(max_length=100, editable=False)
    voted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.polls}'
    
    class Meta:
        ordering = ['polls']
        verbose_name_plural = 'Voters Logs'
    