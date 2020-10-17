from django.contrib import admin

from .models import Book
from .models import compositionclass5
from .models import compositionclass6
from .models import compositionclass7
from .models import compositionclass8


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


class compositionclass5Admin(admin.ModelAdmin):
    list_display = ('title', 'author')


class compositionclass6Admin(admin.ModelAdmin):
    list_display = ('title', 'author')


class compositionclass7Admin(admin.ModelAdmin):
    list_display = ('title', 'author')


class compositionclass8Admin(admin.ModelAdmin):
    list_display = ('title', 'author')


admin.site.register(Book, BookAdmin),
admin.site.register(compositionclass5, compositionclass5Admin),
admin.site.register(compositionclass6, compositionclass6Admin),
admin.site.register(compositionclass7, compositionclass7Admin),
admin.site.register(compositionclass8, compositionclass8Admin),
