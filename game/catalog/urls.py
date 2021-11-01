from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from catalog.lib.data_generator import load_data
from catalog.models import GameUser, Note, Question
from django.db.models import Count

# import django_filters
# app_name = "game"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^login/$', views.user_login, name='login'),
    path('piano/', views.piano, name='piano'),
    path('piano2/', views.piano2, name='piano2'),
    path('piano3/', views.piano3, name='piano3'),
    path('piano_secret/', views.piano_secret, name='piano_secret'),
    path('bed_room/', views.bed_room, name='bed_room'),
    path('clock/', views.clock, name='clock'),
    path('box/', views.box, name='box'),
    path('box_left/', views.box_left, name='box_left'),
    path('box_right/', views.box_right, name='box_right'),
    path('table_recipe/', views.table_recipe, name='table_recipe'),
    path('book_recipe/', views.book_recipe, name='book_recipe'),
    path('book_recipe2/', views.book_recipe2, name='book_recipe2'),
    path('notes/', views.notes, name='notes'),
    path('register/', views.register_request, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='registration/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name="registration/logged_out.html"),
         name='logout'),
    path('note_template/', views.note_template, name='note_template'),
    path('load_note/', views.load_note, name='load_note'),
    # url(r'^load_question/w+', views.load_question, name='load_question'),
    path('load_question/<slug:answer>', views.load_question, name='load_question'),
    path('test_data/', views.test_data, name='test_load'),
]

# load_data()

# TEST DATA
print('888888888888888888888888888')
# return all question with progress in notes 1

# note = Note.getNote()
# n = note.getQuestion()
# print("HEYYYY")
# print(n.send(None))
# next(n)
# print(n.send("fine"))
# next(n)
# print(n.send("here"))
# next(n)
# print(n.send("white"))
# print(n.send("white"))

# test = n.send("fine")
# n.close()


# print(notes)
# print("+++++++++++++++++++++++++++++")
# test = questions

# test = pd.DataFrame(list(test.values()))
# print(test)
# # print(test.groupby('note'))
# print(questions)
print("------------------------------------------------------------")
# print(objs[0].note.all())x
# for q in Question.objects.all():
#     print(q.note.progress)

# group by questions by note
# n_questions = (Question.objects.all()
#             .values('note')
#            .annotate(dcount=Count('note'))
#             .order_by())

# def get_note_and_questions(notes):
#     n_generator = createGenerator(notes)
#     note = next(n_generator)
#     questions = note.question_set.all()
#     print(questions)
#     while all(value.done == True for value in questions):
#         try:
#             print("**********")
#             note = next(n_generator)
#             questions = note.question_set.all()
#             print(questions)
#         except StopIteration:
#             break
#     return note, questions

# #print(get_note_and_questions(notes))

# def get_question(questions):
#     q_generator = createGenerator(questions)
#     question = next(q_generator)
#     while question.done == True:
#         try:
#             print("++++++++++++++++++++++")
#             question = next(q_generator)
#             print(question)
#         except StopIteration:
#             break
#     return question

#print(get_question(get_note_and_questions(notes)[1]))

# n_question = (filter(lambda q: q.note.done == False, n_questions.first()))

# print(n_questions)
# print(n_question)
