from django.contrib import admin
from .models import NutrisumHistoryModel, NutrisumFoodModel, NutrisumExerciseModel, NutrisumFoodListModel, NutrisumExerciseListModel

# Register your models here.
admin.site.register(NutrisumHistoryModel)
admin.site.register(NutrisumFoodModel)
admin.site.register(NutrisumExerciseModel)
admin.site.register(NutrisumFoodListModel)
admin.site.register(NutrisumExerciseListModel)