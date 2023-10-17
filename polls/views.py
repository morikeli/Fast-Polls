from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Questions, Choices, VotersDetails
from .forms import CreatePollsForm, CreateMultipleChoicesForm, EditPollsForm, EditMultipleChoicesForm


class HomepageView(View):
    template_name = 'polls/homepage.html'

    def get(self, request, *args, **kwargs):
        all_polls = []
        if request.user.is_authenticated:
            all_polls = Questions.objects.filter(is_closed=False).all()
            public_polls = []
        else:
            public_polls = Questions.objects.filter(is_closed=False).all()

        created_polls = list(public_polls) + list(all_polls)

        context = {
            'polls': created_polls, 
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        delete_obj = request.POST['delete-request']
        poll_obj = Questions.objects.get(id=delete_obj).delete()
        return redirect('homepage')


@method_decorator(login_required, name='get')
class CreatePollsView(View):
    form_class = CreatePollsForm
    template_name = 'polls/create-polls.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        polls = Questions.objects.filter(author=request.user).all()

        context = {'CreateNewPollForm': form, 'polls': polls}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_poll = form.save(commit=False)
            new_poll.author = request.user
            new_poll.save()

            messages.success(request, 'Poll successfully created!')
            return redirect('create-polls')
        
        context = {'CreateNewPollForm': form}
        return render(request, self.template_name, context)

@method_decorator(login_required, name='get')
class EditPollsView(View):
    form_class = EditPollsForm
    template_name = 'polls/edit-polls.html'

    def get(self, request, pk, *args, **kwargs):
        poll_obj = Questions.objects.get(id=pk)
        form = self.form_class(instance=poll_obj)
        choices = Choices.objects.filter(question__author=request.user).all()


        context = {'EditPollsForm': form, 'choices': choices}
        return render(request, self.template_name, context)
    
    def post(self, request, pk, *args, **kwargs):
        poll_obj = Questions.objects.get(id=pk)
        form = self.form_class(request.POST, instance=poll_obj)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Poll successfully updated')
            return redirect('edit-polls', pk)
        
        context = {'EditPollsForm': form}
        return render(self, self.template_name, context)

@method_decorator(login_required, name='get')
class CreateNewChoicesView(View):
    form_class = CreateMultipleChoicesForm
    template_name = 'polls/create-choices.html'

    def get(self, request, pk, *args, **kwargs):
        quiz_obj = Questions.objects.get(id=pk)
        form = self.form_class()

        context = {'CreateNewChoicesForm': form, 'poll': quiz_obj}
        return render(request, self.template_name, context)
    
    def post(self, request, pk, *args, **kwargs):
        quiz_obj = Questions.objects.get(id=pk)

        form = self.form_class(request.POST)
        if form.is_valid():
            new_choice = form.save(commit=False)
            new_choice.question = quiz_obj
            new_choice.save()

            messages.success(request, 'Choice successfully created!')
            return redirect('create-choices', pk)
        
        context = {'CreateNewChoicesForm': form}
        return render(request, self.template_name, context)

@method_decorator(login_required, name='get')
class EditChoicesView(View):
    form_class = EditMultipleChoicesForm
    template_name = 'polls/edit-choices.html'

    def get(self, request, pk, *args, **kwargs):
        poll_obj = Choices.objects.get(id=pk)
        form = self.form_class(instance=poll_obj)
        choices = Choices.objects.filter(question__author=request.user).all()


        context = {'EditChoicesForm': form, 'choices': choices}
        return render(request, self.template_name, context)
    
    def post(self, request, pk, *args, **kwargs):
        poll_obj = Choices.objects.get(id=pk)
        form = self.form_class(request.POST, instance=poll_obj)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Choice successfully updated!')
            return redirect('edit-choices', pk)
        
        context = {'EditChoicesForm': form}
        return render(self, self.template_name, context)

@method_decorator(login_required, name='get')
class VotingView(View):
    template_name = 'polls/vote.html'

    def get(self, request,  pk, *args, **kwargs):
        poll_obj = Questions.objects.get(id=pk)
        choice_obj = Choices.objects.filter(question_id=poll_obj).all()
        voters_obj = None
        
        try:
            voters_obj = VotersDetails.objects.get(voter=request.user, polls_id__question=poll_obj)
        except VotersDetails.DoesNotExist:
            voters_obj = None
        
        context = {'poll': poll_obj, 'choices': choice_obj, 'voters_obj': voters_obj}
        return render(request, self.template_name, context)
    
    def post(self, request, pk, *args, **kwargs):
        selected_choice = request.POST['Choice']
        choice_qs = Choices.objects.get(id=selected_choice)
        
        # increment total votes
        choice_qs.total_votes += 1
        choice_qs.save()

        # save voters details        
        save_voter = VotersDetails.objects.create(polls_id=selected_choice, voter=request.user, selected_choice=choice_qs.choice)
        save_voter.save()
        messages.success(request, 'Form successfully submitted!')
        return redirect('vote', pk)

    