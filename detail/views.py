from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

# Create your views here.


def home(request):
	users = Profile.objects.all()
	context = {'users': users }
	return render(request, 'registration/all.html', context)


def signup(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ProfileForm()
	context = {'form': form}
	return render(request, 'registration/signup.html', context)
