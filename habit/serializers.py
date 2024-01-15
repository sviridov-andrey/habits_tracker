from rest_framework import serializers

from habit.models import Habit
from habit.validators import validator_habit


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Habit """

    class Meta:
        model = Habit
        fields = '__all__'

        validators = [validator_habit,]
