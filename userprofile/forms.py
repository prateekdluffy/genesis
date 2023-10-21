from django import forms

from .models import ProfilePageModel

class ProfilePageForm(forms.ModelForm):
	class Meta:
		model = ProfilePageModel
		fields = ['name', 'title', 'bio', 'birth_date', 'profile_picture', 'cover_picture']

	birth_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
	bio = forms.CharField(widget=forms.Textarea(attrs={'rows':'2', 'placeholder':'Tell us something about yourself or the things that you like!'}), required=False)