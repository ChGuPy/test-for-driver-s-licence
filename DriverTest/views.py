# -*- coding:utf-8 -*-
from django.shortcuts import render
from forms import UserLoginForm, TestsForm
from models import Question, CompleteTest, Answer
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
# Create your views here.





def index(request):
    error = ''
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                try:
                    CompleteTest.objects.get(user=request.user).delete()
                except:
                    pass
                return HttpResponseRedirect('/test/1')
            error += u'Неверные данные'
    return render(request, 'index.html', {'form': form, 'error': error})


def test(request, pk):
    all = Question.objects.exclude(is_active=False)
    amount_of_question = len(all)
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    pk = int(pk)
    if request.method == 'POST':
        CompleteTest.objects.get_or_create(user=request.user)
        try:
            answer = request.POST['choices']
            ans = Answer.objects.get(id=int(answer))
            if ans.true_or_false:
                x = CompleteTest.objects.get(user=request.user)
                x.right_answers += 1
                x.save()
        except:
            pass
        if (pk - 1) < (amount_of_question - 1) :
            return HttpResponseRedirect('/test/%s' % str(pk+1))
        else:
            return HttpResponseRedirect('/finish/')
    print amount_of_question
    form = all[pk-1]
    return render(request, 'test.html', {'form': form})


def finish(request):
    all_questions = len(Question.objects.exclude(is_active=False))
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    user = CompleteTest.objects.get(user=request.user)
    return render(request, 'finish.html', {'right_answers': user.right_answers,
                                           'amount_of_question': all_questions})
