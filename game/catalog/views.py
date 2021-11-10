from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from json import dumps
from django.contrib.auth import authenticate, login
from jinja2.nodes import Test
from django.http import JsonResponse
from .forms import LoginForm, NewUserForm
from django.contrib import messages
from django.core import serializers
from django.forms.models import model_to_dict
from .models import Note, History, GameUser, GameProgress, global_note, q_generator
from .lib.objects import NoteBuilder
from catalog.lib.ui_dict import UI
from django.forms.models import model_to_dict
from catalog.service import get_random_answers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import QueryDict
import itertools
import json
import ast
from django.urls import reverse
from django.http import HttpResponseBadRequest
from django.utils.deprecation import MiddlewareMixin
from types import SimpleNamespace
from collections import namedtuple


def piano2(request):
    id_url = 8
    obj_progress = GameProgress.objects.filter(id=int(id_url)).first()
    template = obj_progress.template
    mapped_to = (eval(obj_progress.mapped_to))
    return render(
        request=request,
        template_name='catalog/piano/piano2.html',
        context={
            'piano': dumps({'password': 'cd'}),
            'mapped_to': mapped_to
        },
    )


def notes(request):
    return render(
        request,
        'catalog/notes/notes.html',
    )


def load_view(request, id_url):
    obj_progress = GameProgress.objects.filter(id=int(id_url)).first()
    template = obj_progress.template
    mapped_to = (eval(obj_progress.mapped_to))
    print(mapped_to)
    return render(request=request,
                  template_name=template,
                  context={'mapped_to': mapped_to})


# render(request=request,
#                   template_name="registration/register.html",
#                   context={"register_form": form})
#TO DO review this function
# def user_login(request):
#     if request.method == 'POST':
#         print("LOGIN**")
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     print("LOGIN----->>>>")
#                     # print(user.username)
#                     # print(user.progress)
#                     # print(user.id)
#                     # request.session['id'] = user.id
#                     # request.session['user_progress'] = user.progress
#                     # request.session['username'] = user.username
#                     return redirect('/catalog/user_table/')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'registration/login.html', {'form': form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/catalog/login")
        messages.error(request,
                       "Unsuccessful registration. Invalid information.")
        return HttpResponse('Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render(request=request,
                  template_name="registration/register.html",
                  context={"register_form": form})


def load_note(request):
    global global_note
    global q_generator
    global_note = Note.getNote()
    q_generator = global_note.getQuestion()
    next(q_generator)
    print("***************************")
    print("reload global_note")
    default_data = {'html': 'empty'}
    if global_note is None:
        return JsonResponse(default_data)
    question = global_note.questions.first()
    if question is None:
        return JsonResponse(default_data)
    answers = eval(question.bad)
    answers.append(question.correct)
    # print("USER>>>>>>>>>>")
    # print(request.session['username'])
    #    RANDOMIZER FOR ANSWERS
    #    UNCOMENT THIS AFTER DEBUG
    #    answers = get_random_answers(answers)
    ui = UI[question.ui](answers=answers,
                         text=global_note.text_question,
                         text_question=question.question)
    data = {'html': ui}
    return JsonResponse(data)


def load_question(request, *args, **kwargs):
    request.encoding = 'UTF-8'
    answer = request.GET.get("answer")
    print("ANSWER")
    print(answer)
    global global_note
    global q_generator
    question = None
    answers = "hey"
    ui = ""
    try:
        question = q_generator.send(answer)
        next(q_generator)
    except StopIteration:
        print("Error stop iteration")
        return redirect(reverse(load_note))
    if question is None:
        if global_note.done is True:
            global_note.save()
        return redirect(reverse(load_note))
    answers = eval(question.bad)
    answers.append(question.correct)
    #    RANDOMIZER FOR ANSWERS
    #    UNCOMENT THIS AFTER DEBUG
    #    answers = get_random_answers(answers)
    ui = UI[question.ui](answers=answers,
                         text=global_note.text_question,
                         text_question=question.question)
    data = {'html': ui}
    return JsonResponse(data)


def note_template(request):
    data = {
        'html': '<li class="mine"><span>I have something for you.</span></li>'
    }
    data = {'html': Note.objects.filter(progress_id__exact=1)}
    return JsonResponse(data)


def test_data(request):
    data = {'html': serializers.serialize("json", Note.objects.all())}
    return JsonResponse(data)
