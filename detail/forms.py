from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = (
				'name',
				'username',
				'email',
				'gender',
				'mobile',
				'education',
				'profile_pic'
			)
		labels = {
		'profile_pic': 'Choose Image'
		}

		def __init__(self, *args, **kwargs):
			super(ProfileForm,self).__init__(*args, **kwargs)
			self.fields['gender'].empty_label = 'Choose'