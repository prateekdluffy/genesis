from django import forms
from datetime import date
from .models import NutrisumHistoryModel, NutrisumFoodListModel, NutrisumExerciseListModel, NutrisumFoodModel, NutrisumExerciseModel, CommentModel

class NutrisumHistoryForm(forms.ModelForm):
	class Meta:
		model = NutrisumHistoryModel
		fields = ['date', 'height', 'weight', 'food_list', 'exercise_list', 'public']


	def __init__(self, user,*args, **kwargs):
		super(NutrisumHistoryForm, self).__init__(*args, **kwargs)
		self.fields['food_list'].queryset = NutrisumFoodListModel.objects.filter(owner=user)
		self.fields['exercise_list'].queryset = NutrisumExerciseListModel.objects.filter(owner=user)

	date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), initial=date.today)
	food_list = forms.ModelMultipleChoiceField(queryset=NutrisumFoodListModel.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
	exercise_list = forms.ModelMultipleChoiceField(queryset=NutrisumExerciseListModel.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

class NutrisumFoodListForm(forms.ModelForm):
	class Meta:
		model = NutrisumFoodListModel
		fields = ['food_item']

class NutrisumExerciseListForm(forms.ModelForm):
	class Meta:
		model = NutrisumExerciseListModel
		fields = ['exercise_item']

class CommentForm(forms.ModelForm):
	class Meta:
		model = CommentModel
		fields = ['comment']

	comment = forms.CharField(widget=forms.Textarea(attrs={'rows':'2', 'placeholder':'Be kind, words are very powerful!'}))