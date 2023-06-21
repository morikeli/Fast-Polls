from .models import Questions, Choices, VotersDetails
from django.contrib import admin

@admin.register(Questions)
class PollsTable(admin.ModelAdmin):
    list_display = ['author', 'category', 'close_voting']
    readonly_fields = ['quiz', 'category', 'close_voting']

@admin.register(Choices)
class ChoicesTable(admin.ModelAdmin):
    list_display = ['choice', 'total_votes', 'edited']
    readonly_fields = ['choice', 'total_votes']

@admin.register(VotersDetails)
class VotersTable(admin.ModelAdmin):
    list_display = ['polls', 'voted']
    