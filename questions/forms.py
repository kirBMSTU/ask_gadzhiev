from django import forms

from questions.models import User

class PostForm(forms.Form):

	def clean_username(self):
		data = self.cleaned_data('username')
		if "*" in data:
			raise ValidationError("Hi!")
		return data


	class Meta:
		model = User
		fields = ('username', 'password')