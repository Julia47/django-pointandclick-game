from catalog.lib.objects import NoteBuilder
# from game.catalog.lib.objects import NoteBuilder
from catalog.models import Note, GameProgress, GameUser
from django.core.management.base import BaseCommand


def load_progress():
    p1 = GameProgress(1, 1, [2, 3], "catalog/user_table.html")
    p2 = GameProgress(2, 2, [1], "catalog/letter.html")
    p3 = GameProgress(3, 3, [4], "catalog/start_game.html")
    p4 = GameProgress(4, 4, [5], "catalog/house.html")
    p5 = GameProgress(5, 5, [4, 6], "catalog/door.html")
    p6 = GameProgress(6, 6, [5, 7, 11, 14, 18], "index.html")
    p7 = GameProgress(7, 7, [6, 8, 9], "catalog/piano/piano.html")
    p8 = GameProgress(8, 8, [7], "catalog/piano/piano2.html")
    p9 = GameProgress(9, 9, [7], "catalog/piano/piano3.html")
    p10 = GameProgress(10, 10, [7], "catalog/piano/piano_secret.html")
    p11 = GameProgress(11, 11, [6, 12], "catalog/box/box.html")
    p12 = GameProgress(12, 12, [11], "catalog/box/box_left.html")
    p13 = GameProgress(13, 13, [11], "catalog/box/box_right.html")
    p14 = GameProgress(14, 14, [6, 16, 15], "catalog/bed_room.html")
    p15 = GameProgress(15, 15, [14], "catalog/clock.html")
    p16 = GameProgress(16, 16, [17, 14], "catalog/recipe/book_recipe.html")
    p17 = GameProgress(17, 17, [16, 14], "catalog/recipe/book_recipe2.html")
    p18 = GameProgress(18, 18, [6], "catalog/table_letter.html")
    obj_list = [p1, p2, p3, p4, p5, p6, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18]
    for o in obj_list:
        o.save()

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
    n1 = NoteBuilder(
    ).loadLevel("1").setId(1).setProgressId(1).setTextQuestion(
        "Ви отримали в спадок будинок від вашого дядька. Оглянтесь в ньому, на столі знайдете записку, котра прояснить певні деталі."
    ).save().addQuestion(
    ).setId(1).setNoteId(1).question("Як звати власника будинку?").correct("Джо").bad([
        "Пітер", "Анна"
    ]).ui("buttons-template").save().build().addQuestion().setId(2).setNoteId(
        1).question("Where are you?").correct("second").bad([
            "at home", "atschool"
        ]).ui("buttons-template").save().build().addQuestion().setId(
            3).setNoteId(1).question("Where are you?").correct("third").bad([
                "athome", "at school"
            ]).ui("buttons-template").save().build().addQuestion().setId(
                6).setNoteId(1).question("How are you?").correct("last").bad([
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
    print("_____________DATA WAS LOADED___________")


class Command(BaseCommand):
    help = "Command for loading data"

    def handle(self, *args, **kwargs):
        load_data()
