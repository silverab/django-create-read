from django.db import models

# Create your models here.

class Profile(models.Model):
	Gender = (
		('Male', 'Male'),
		('Female', 'Female')
		)
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=50)
	email = models.EmailField()
	gender = models.CharField(max_length=6, choices=Gender)
	mobile = models.IntegerField()
	education = models.CharField(max_length=30)
	joining_date = models.DateField(auto_now_add=True)
	profile_pic = models.ImageField(upload_to='profile/', null=True, blank=True)