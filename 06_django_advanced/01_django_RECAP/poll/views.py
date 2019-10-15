from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from .forms import ChoiceModelForm

def poll_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choice = get_object_or_404(Choice, question_id=question_id)
    form = ChoiceModelForm()
    context = {'question': question, 'form': form}
    return render(request, 'poll/question_detail.html', context)


def upvote(request, question_id, choice_id):
    choice = get_object_or_404(Choice, id=choice_id)
    form = ChoiceModelForm(request.POST, instance=choice)
    if form.is_valid():
        if form.content == '한식':
            choice.vote += 1
        elif form.content == '중식':
            choice.vote += 1
        elif form.content == '양식':
            choice.vote += 1
    return redirect('poll:poll_detail', question_id)
