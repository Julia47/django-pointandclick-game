from .objects import NoteBuilder
# from game.catalog.lib.objects import NoteBuilder
from catalog.models import Note, GameProgress, GameUser


def load_progress():
    p1 = GameProgress()
    p2 = GameProgress()
    p3 = GameProgress()
    p1.id = 1
    p2.id = 2
    p3.id = 3
    p1.progress = 1
    p2.progress = 2
    p3.progress = 3
    p1.save()
    p2.save()
    p3.save()


def load_user():
    u1 = GameUser()
    u1.id = 1
    u1.progress = GameProgress.objects.filter(id__exact=1).first()
    u1.password = 'zibert230'
    u1.username = 'julka'
    u1.is_superuser = True
    u1.is_staff = True
    u1.save()


def load_note():
    n1 = NoteBuilder().loadLevel("1").setId(1).setProgressId(
        1).setTextQuestion("TEXT ! STRING").save().addQuestion(
        ).setId(1).setNoteId(1).question("How are you?").correct("first").bad([
            "bad", "terribly"
        ]).ui("buttons-template").save().build().addQuestion().setId(
            2).setNoteId(1).question("Where are you?").correct("second").bad([
                "at home", "atschool"
            ]).ui("buttons-template").save().build().addQuestion().setId(
                3).setNoteId(1).question("Where are you?").correct(
                    "third").bad(
                        ["athome", "at school"]).ui("buttons-template").save(
                        ).build().addQuestion().setId(6).setNoteId(1).question(
                            "How are you?").correct("last").bad([
                                "bad", "terribly"
                            ]).ui("buttons-template").save().build().build()
    n2 = NoteBuilder().loadLevel("1").setId(2).setProgressId(
        1).setTextQuestion("TEXT 2 HEYY").save().addQuestion().setId(
            4).setNoteId(2).question("Heyyy?").correct("yes").bad([
                "no", "probably no"
            ]).ui("buttons-template").save().build().addQuestion().setId(
                5).setNoteId(2).question("Where are you?").correct("here").bad(
                    ["at home", "at school"
                     ]).ui("buttons-template").save().build().build()


def load_data():
    load_progress()
    load_user()
    load_note()
