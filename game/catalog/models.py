import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class GameProgress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID")
    progress = models.IntegerField()

    def __str__(self):
        return str(self.progress)


class GameUser(AbstractUser):
    progress_id = models.ForeignKey(GameProgress, on_delete=models.CASCADE, null=True)
    # process = models.IntegerField(blank=True, null=True)


class Piano(models.Model):
    password = models.CharField(max_length=20, help_text="Password for open key")

    def __str__(self):
        return self.password


class Box(models.Model):
    password = models.CharField(max_length=20, help_text="Password for open key")

    def __str__(self):
        return self.password


# class Book(models.Model):
#     secret_word = models.CharField(max_length=20, help_text="Password for open key")
#
#     def __str__(self):
#         return self.secret_word


class MysteryInstance(models.Model):
    t = True


class History(models.Model):
    text_note = models.TextField(max_length=1000, help_text="Enter a description for history")
    progress_id = models.ForeignKey(GameProgress, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text_note


class Note(models.Model):
    text_note = models.TextField(max_length=1000, help_text="Enter a description for note")
    progress_id = models.ForeignKey(GameProgress, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text_note


class NoteInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this note")
    note = models.ForeignKey('Note', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('t', 'Visible'),
        ('f', 'Invisible'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='f', help_text='Book availability')

    def __str__(self):
        return '%s (%s)' % (self.id, self.note.text_note)
