from django.shortcuts import render
from .models import ProfilePageModel
from .forms import ProfilePageForm
from django.contrib.auth.models import User
from nutrisum.models import NutrisumHistoryModel
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class ProfilePageView(View):
	def get(self, request, username, *args, **kwargs):
		obj = User.objects.get(username=username)
		profile = ProfilePageModel.objects.get(user=obj)
		user = profile.user
		logs = NutrisumHistoryModel.objects.filter(owner=user)

		context = {
			'user' : user,
			'profile' : profile,
			'logs' : logs
		}

		return render(request, 'userprofile/profile_page.html', context)

class ProfilePageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = ProfilePageModel
	form_class = ProfilePageForm
	template_name = 'userprofile/profile_page_update.html'

	def get_object(self):
		if self.kwargs.get('pk'):
			return User.objects.get(pk=self.kwargs['pk'])
		else:
			return User.objects.get(username=self.kwargs['username'])

	def get_success_url(self):
		return reverse_lazy('userprofile:profilepage', kwargs={'username':self.request.user.username})

	def test_func(self):
		profile = self.get_object()
		return self.request.user == profile