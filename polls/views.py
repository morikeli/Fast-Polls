from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Questions, Choices
from .forms import CreatePollsForm, CreateMultipleChoicesForm, VotingForm, EditPollsForm, EditMultipleChoicesForm


class HomepageView(View):
    template_name = 'polls/homepage.html'

    def get(self, request, *args, **kwargs):
        all_polls = []
        if request.user.is_authenticated:
            all_polls = Questions.objects.all()
            public_polls = []
        else:
            public_polls = Questions.objects.filter(category='Public').all()

        created_polls = list(public_polls) + list(all_polls)

        context = {
            'polls': created_polls, 
        }
        return render(request, self.template_name, context)

@method_decorator(login_required, name='get')
class CreatePollsView(View):
    form_class = CreatePollsForm
    template_name = 'polls/create-polls.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {'CreateNewPollForm': form}
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
    
class EditPollsView(View):
    form_class = EditPollsForm
    template_name = 'polls/edit-polls.html'

    def get(self, request, pk, *args, **kwargs):
        poll_obj = Questions.objects.get(id=pk)
        form = self.form_class(instance=poll_obj)

        context = {'EditPollsForm': form}
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

    
class CreateNewChoicesView(View):
    form_class = CreateMultipleChoicesForm
    template_name = 'polls/create-choices.html'

    def get(self, request, pk, *args, **kwargs):
        quiz_obj = Questions.objects.get(id=pk)
        form = self.form_class()

        context = {'CreateNewChoicesForm': form}
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

class EditChoicesView(View):
    form_class = EditMultipleChoicesForm
    template_name = 'polls/edit-choices.html'

    def get(self, request, pk, *args, **kwargs):
        poll_obj = Choices.objects.get(id=pk)
        form = self.form_class(instance=poll_obj)

        context = {'EditChoicesForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, pk, *args, **kwargs):
        poll_obj = Choices.objects.get(id=pk)
        form = self.form_class(request.POST, instance=poll_obj)
        if form.is_valid():
            form.save(commit=False)
            messages.warning(request, 'Choice successfully updated!')
            return redirect('edit-choices', pk)
        
        context = {'EditChoicesForm': form}
        return render(self, self.template_name, context)

class VotingView(View):
    form_class = VotingForm
    template_name = 'polls/vote.html'

    def get(self, request,  pk, *args, **kwargs):
        form = self.form_class()

        context = {'VotingForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=False)
            messages.success(request, 'Form successfully submitted!')
            return redirect('vote', pk)
        
        context = {'VotingForm': form}
        return render(request, self.template_name, context)

