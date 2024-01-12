from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """ Привычки в админке """

    list_display = ('name', 'habit_is_public', 'user',)
    list_filter = ('name',)
    search_fields = ('name',)
