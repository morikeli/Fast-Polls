from polls.models import Question, Choice
from .forms import LoginForm, SetMultipleChoices, SignUpForm, SetQuestionsForm
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from polls.utils import get_plot

class UserLogin(LoginView):
    authentication_form = LoginForm
    template_name = 'polls/login.html'
    

def signup_view(request):
    form = SignUpForm()
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            reg_user = form.save(commit=False)
            reg_user.username = reg_user.first_name + ' ' + reg_user.last_name
            reg_user.is_staff = True
            reg_user.save()
            messages.success(request, 'You have successully created an account')
            return redirect('login')
    
    context = {'signup_form': form}
    return render(request, 'polls/register.html', context)

def homepage_view(request):
    all_quiz = Question.objects.all()
    
    context = {'questions': all_quiz}
    return render(request, 'polls/index.html', context)

@login_required(login_url='login')
def set_questions_view(request):
    quiz_form = SetQuestionsForm()
    choice_form = SetMultipleChoices()
    
    if request.method == 'POST':
        quiz_form = SetQuestionsForm(request.POST)
        choice_form = SetMultipleChoices(request.POST)
        
        if quiz_form.is_valid():
            quiz_set = quiz_form.save(commit=False)
            quiz_set.set_by = request.user.userprofile
            quiz_set.save()
            messages.success(request, 'Your question has been posted successfully!')      
        
        elif choice_form.is_valid():
            choice = choice_form.save(commit=False)
            if Choice.objects.filter(question=choice.question, option=choice.option).exists():
                messages.warning(request, f'Choice --> {choice.option} <-- for question "{choice.question.question_text}" already exists!')
            else:
                choice.save()
                messages.info(request, 'Multiple choice included successfully!')
        
        return redirect('add_quiz')
           
    context = {'quiz_form': quiz_form, 'choice_form': choice_form}
    return render(request, 'polls/set_polls.html', context)


@login_required(login_url='login')
def edit_questions_view(request, pk):
    obj = Question.objects.get(id=pk)
    edit_quiz_form = SetQuestionsForm(instance=obj)
        
    if request.method == 'POST':
        edit_quiz_form = SetQuestionsForm(request.POST, instance=obj)

        if edit_quiz_form.is_valid():
            edit_quiz_form.save()
            
            messages.info(request, 'Question edited successfully!')
            return redirect('edit_question', pk)
    
    context = {'quiz_form': edit_quiz_form, 'obj': obj}
    return render(request, 'polls/edit-quiz.html', context)

@login_required(login_url='login')
def edit_choices_view(request, pk):
    obj = Choice.objects.get(id=pk)
    edit_choice_form = SetMultipleChoices(instance=obj)
        
    if request.method == 'POST':
        edit_choice_form = SetMultipleChoices(request.POST, instance=obj)

        if edit_choice_form.is_valid():
            edit_choice_form.save()
            
            messages.info(request, 'Multiple choice edited successfully!')
            return redirect('edit_choice', pk)
    context = {'obj': obj, 'choice_form': edit_choice_form}
    return render(request, 'polls/edit-choice.html', context)

@login_required(login_url='login')
def delete_view(request, pk):
    try:
        obj = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        obj = Choice.objects.get(id=pk)
    
    if request.method == 'POST':
        obj.delete()
        messages.warning(request, f'You have deleted {obj.question_text}')
        
    context = {'obj': obj}
    return render(request, 'polls/delete.html', context)


def vote_view(request, pk):
    quiz = Question.objects.get(id=pk)
    choices = Choice.objects.filter(question__question_text=quiz).all().order_by('option')
    
    if request.method == 'POST':
        try:
            user_choice = request.POST['choice']
            selection = choices.get(id=user_choice)
            selection.total_votes += 1
            selection.save()
            
            messages.success(request, 'Your vote has been submitted successfully!')
            return redirect('results', pk)
        except MultiValueDictKeyError:
            messages.error(request, 'You have not selected a valid choice.')
            return redirect('vote', pk)
    context = {'quiz': quiz, 'choices': choices}
    return render(request, 'polls/vote.html', context)


def poll_results_view(request, pk):
    quiz = Question.objects.get(id=pk)
    results_choice = Choice.objects.filter(question__question_text=quiz).all()
    x_axis = [x.option[:7] for x in results_choice]
    y_axis = [y.total_votes for y in results_choice]
    chart = get_plot(x_axis, y_axis)
    
    context = {'question': quiz, 'results': results_choice, 'chart': chart}
    return render(request, 'polls/stats.html', context)


class LogoutUser(LogoutView):
    template_name = 'polls/logout.html'