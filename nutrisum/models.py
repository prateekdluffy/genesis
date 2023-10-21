from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
import decimal

# Create your models here.
class NutrisumHistoryModel(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(default=date.today)
	height = models.DecimalField(max_digits=5, decimal_places=2)
	weight = models.DecimalField(max_digits=5, decimal_places=2)
	calorie_intake_count = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	calorie_burnt_count = models.DecimalField(max_digits=6, decimal_places=2, default =0.00)
	food_list = models.ManyToManyField('NutrisumFoodListModel', related_name='Food_Intake_List', blank=True, through='AddToFoodListModel')
	exercise_list = models.ManyToManyField('NutrisumExerciseListModel', related_name='Exercise_Completed_List', blank=True, through='AddToExerciseListModel')
	public = models.BooleanField(default=True)

	class Meta:
		ordering = ('-date',)
		unique_together = [('owner', 'date')]

	def __str__(self):
		return f"{self.owner} - {self.date}"

	def save(self, *args, **kwargs):
		try:
			food_item_list = self.food_list.all()
			cal = decimal.Decimal(0.00)
			for food in food_item_list:
				cal += food.food_item.calories
			self.calorie_intake_count = cal
			exercise_item_list = self.exercise_list.all()
			cal = decimal.Decimal(0.00)
			for exercise in exercise_item_list:
				cal += exercise.exercise_item.calories_burn
			self.calorie_burnt_count = cal
		except:
			pass

		super(NutrisumHistoryModel, self).save(*args, **kwargs)

class NutrisumFoodModel(models.Model):
	name = models.CharField(max_length=128)
	calories = models.DecimalField(max_digits=5, decimal_places=2)
	protein = models.DecimalField(max_digits=5, decimal_places=2)
	carbohydrate = models.DecimalField(max_digits=5, decimal_places=2)
	fat = models.DecimalField(max_digits=5, decimal_places=2)
	vitamins = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class NutrisumExerciseModel(models.Model):
	name = models.CharField(max_length=128)
	calories_burn = models.DecimalField(max_digits=5, decimal_places=2)
	part_name = models.CharField(max_length=128)
	weight_or_strength = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class NutrisumFoodListModel(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	food_item = models.ForeignKey('NutrisumFoodModel', on_delete=models.CASCADE)

	class Meta:
		unique_together = [('owner', 'food_item')]

	def __str__(self):
		return self.food_item.name

class NutrisumExerciseListModel(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	exercise_item = models.ForeignKey('NutrisumExerciseModel', on_delete=models.CASCADE)

	class Meta:
		unique_together = [('owner', 'exercise_item')]

	def __str__(self):
		return self.exercise_item.name
class AddToFoodListModel(models.Model):
	food_list = models.ForeignKey('NutrisumFoodListModel', on_delete=models.CASCADE)
	history = models.ForeignKey('NutrisumHistoryModel', on_delete=models.CASCADE)
	quantity = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)

class AddToExerciseListModel(models.Model):
	exercise_list = models.ForeignKey('NutrisumExerciseListModel', on_delete=models.CASCADE)
	history = models.ForeignKey('NutrisumHistoryModel', on_delete=models.CASCADE)
	quantity = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)

class CommentModel(models.Model):
	comment = models.TextField()
	created_on = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	log = models.ForeignKey('NutrisumHistoryModel', on_delete=models.CASCADE)