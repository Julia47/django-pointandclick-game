from copy import deepcopy
import django
from catalog.models import Note, GameProgress, Question


class QuestionBuilder():
    __note_builder = None
    __question = Question()

    def __init__(self, note_builder: object):
        self.__note_builder = note_builder

    def setId(self, id: int):
        self.__question.id = id
        return self

    def setNoteId(self, id: int):
        self.__question.note = (Note.objects.filter(id__exact=id)).first()
        return self

    def question(self, question: str):
        self.__question.question = question
        return self

    def correct(self, correct: str):
        self.__question.correct = correct
        return self

    def bad(self, bad: list):
        self.__question.bad = bad
        return self

    def ui(self, ui: list):
        self.__question.ui = ui
        return self

    def save(self):
        self.__question.save()
        return self

    def build(self):
        return self.__note_builder


class NoteBuilder():
    __question = None
    __note = Note()
    
    def addQuestion(self):
        self.__question = QuestionBuilder(self)
        return self.__question

    def setTextQuestion(self, text_question: list):
        self.__note.text_question = text_question
        return self

    def setId(self, id: int):
        self.__note.id = id
        return self

    def setProgressId(self, progress_id: int):
        print('HEYY')
        self.__note.progress = GameProgress.objects.filter(id__exact=progress_id).first()
        return self        

    def copyFrom(self, note_obj):
        self.__note = deepcopy(note_obj)
        return self

    def loadLevel(self, level: int):
        return self

    def save(self):
        self.__note.save()
        return self

    # to do check this 
    def validate(self):
        print(self.__note.__dict__)
        print('HEYYYYYYYYYYY')
        data = self.__note.__dict__
        if '_state' in data:
            data.pop('_state')
        data = data.values()
        data = filter(lambda x: x is not None, data)
        print('Heyyyy 2')
        print(data)
        return all(True if type(value) == django.db.models.base.ModelState else len(value) > 0 for value in data)

    def build(self):
        return self.__note
#        return self.__note if self.validate() else "problem with validation"
# class TestBuilder(Test):
#     def __init__():
#         self.test == "a"
