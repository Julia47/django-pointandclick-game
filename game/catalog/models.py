import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


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
        print(question.__dict__)
        if question is None:
            return None
        while True:
            answer = yield
            if answer is not None and question.correct == answer:
                question.done = True
                question = next(questions, None)
                if question is None:
                    return None
                #print(question.__dict__)
                yield question
            else:
                return None
            #yield question

    # def get_question(self, note, answer):
    #     questions = note.question_set.all()
    #     q_generator = self.question_generator(answer)
    #     q_generator.send(None)
    #     for question in questions:
    #         try:
    #             data = q_generator.send(question)
    #             if data is not None:
    #                 print(data.__dict__)
    #             next(q_generator)
    #         except StopIteration:
    #             break
    #     q_generator.close()

    # def questionGenerator(note):
    #     questions = note.question_set.all()
    #     questions = iter(questions)
    #     while True:
    #         if answer == questions[i + 1].correct:
    #             questions[i + 1].done = True
    #         q = yield questions[i]
    #         i += 1
    #     yield questions[i - 1]

    # @staticmethod
    # def get_question(note, answer):
    #     questions = Note.questionGenerator(note, answer)
    #     for _ in questions:
    #         try:
    #             question = next(questions)
    #             print(question)
    #         except StopIteration:
    #             break
    #     return question


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
