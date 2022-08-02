from .models import UserProfile, Question, Choice
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
import uuid


@receiver(pre_save, sender=UserProfile)
def generate_user_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace("-", "")[:15]

@receiver(pre_save, sender=Question)
def generate_quiz_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace("-", "")[:16]

@receiver(pre_save, sender=Choice)    
def generate_choice_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace("-", "")[:16]


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is True and instance.is_superuser is False:
            UserProfile.objects.create(name=instance)

@receiver(post_save, sender=UserProfile)
def create_quiz_rel(sender, instance, created, **kwargs):
    if created:
        Question.objects.create(set_by=instance)