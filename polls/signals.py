from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Questions, Choices, VotersDetails
from datetime import datetime
import uuid

@receiver(pre_save, sender=Questions)
def generate_questionID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:20]
    
    # check if the closing datetime is due and mark the polls as closed - i.e no voting on the poll.
    if instance.closing_dt >= datetime.now().strftime('%Y-%m-%d'):
        instance.is_closed = True

@receiver(pre_save, sender=Choices)
def generate_choicesID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:20]

@receiver(pre_save, sender=VotersDetails)
def generate_votersID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:20]
