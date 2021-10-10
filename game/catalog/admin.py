from django.contrib import admin
from .models import GameUser, Piano, Note, NoteInstance, History, Box, GameProgress
from django.contrib.auth.models import User


class GameUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(GameUser, GameUserAdmin)


@admin.register(Piano)
class PianoAdmin(admin.ModelAdmin):
    list_display = ('password',)


class NoteInstanceInline(admin.TabularInline):
    model = NoteInstance


class NoteAdmin(admin.ModelAdmin):
    inlines = [NoteInstanceInline]


admin.site.register(Note)
admin.site.register(History)
admin.site.register(Box)
admin.site.register(GameProgress)
