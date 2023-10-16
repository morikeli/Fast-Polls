from .models import Questions, Choices, VotersDetails
from django.contrib import admin

@admin.register(Questions)
class PollsTable(admin.ModelAdmin):
    list_display = ['author', 'category', 'closing_dt', 'is_private', 'is_closed']
    readonly_fields = ['quiz', 'category', 'closing_dt', 'is_private', 'is_closed']

@admin.register(Choices)
class ChoicesTable(admin.ModelAdmin):
    list_display = ['choice', 'total_votes', 'edited']
    readonly_fields = ['choice', 'total_votes']

@admin.register(VotersDetails)
class VotersTable(admin.ModelAdmin):
    list_display = ['polls', 'voting_date']
    readonly_fields = ['voter', 'polls', 'selected_choice']