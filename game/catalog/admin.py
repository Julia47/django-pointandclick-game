from django.contrib import admin
from .models import GameUser, Piano, History, Box, GameProgress, Note
from django.contrib.auth.models import User


class GameUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(GameUser, GameUserAdmin)
admin.site.register(Note)

@admin.register(Piano)
class PianoAdmin(admin.ModelAdmin):
    list_display = ('password',)


admin.site.register(History)
admin.site.register(Box)
admin.site.register(GameProgress)
