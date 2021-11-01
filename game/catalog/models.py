import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from dataclasses import dataclass


global_note = None
q_generator = None

 
class GameProgress(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    progress = models.IntegerField()

    def __str__(self):
        return str(self.progress)


class GameUser(AbstractUser):
    progress = models.ForeignKey(GameProgress,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)


#@dataclass
class Note(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    progress = models.ForeignKey(GameProgress,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)
    done = models.BooleanField(default=False)
    text_question = models.TextField(
        max_length=1000,
        help_text="Enter a description for history",
        null=True,
        blank=True)
    questions = None

    def update_fields(self, **entries):
        self.__dict__.update(entries)

    @staticmethod
    def getNote():
        """Get notes in which not are done and filter by progress of user"""
        notes = Note.objects.filter(progress="1").filter(done=False)
        if len(notes) == 0:
            return None
        else:
            note = notes[0]
            note.questions = note.question_set.all()
            return note

    def getQuestion(self):
        questions = iter(self.questions)
        question = next(questions, None)
        # print(question.__dict__)
        if question is None:
            yield None
        while True:
            answer = yield
            if answer is not None and question.correct == answer:
                question = next(questions, None)
                if question is None:
                    self.done = True
                    yield None
                print("YESSS")
                yield question
            else:
                print("NO NO NO")
                yield None




class Question(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    note = models.ForeignKey(Note,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    question = models.TextField(max_length=100,
                                help_text="Enter a question",
                                null=True,
                                blank=True)
    correct = models.TextField(max_length=100,
                               help_text="Enter a correct answer",
                               null=True,
                               blank=True)
    bad = models.TextField(max_length=100,
                           help_text="Enter a bad answer",
                           null=True,
                           blank=True)
    ui = models.TextField(max_length=100,
                          help_text="Enter ui elements",
                          null=True,
                          blank=True)


class Piano(models.Model):
    password = models.CharField(max_length=20,
                                help_text="Password for open key")

    def __str__(self):
        return str(self.password)


class Box(models.Model):
    password = models.CharField(max_length=20,
                                help_text="Password for open key")

    def __str__(self):
        return str(self.password)


# class Book(models.Model):
#     secret_word = models.CharField(max_length=20, help_text="Password for open key")
#
#     def __str__(self):
#         return self.secret_word


class MysteryInstance(models.Model):
    t = True


class History(models.Model):
    text_note = models.TextField(max_length=1000,
                                 help_text="Enter a description for history")
    progress = models.ForeignKey(GameProgress,
                                 on_delete=models.CASCADE,
                                 null=True)

    def __str__(self):
        return str(self.text_note)
