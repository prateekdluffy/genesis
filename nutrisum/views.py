from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import NutrisumHistoryModel, NutrisumFoodListModel, NutrisumExerciseListModel, CommentModel
from .forms import NutrisumHistoryForm, NutrisumFoodListForm, NutrisumExerciseListForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.
class NutrisumHomeView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		user_history = NutrisumHistoryModel.objects.filter(owner=request.user)

		context = {
			'user_history_list' : user_history,
		}

		return render(request, 'nutrisum/nutrisum_home.html', context)

class NutrisumSocialView(View):
	def get(self, request, *args, **kwargs):
		nutrisumhistory = NutrisumHistoryModel.objects.filter(public=True)

		context = {
			'nutrisumhistory_list': nutrisumhistory,
		}

		return render(request, 'nutrisum/nutrisum_social.html', context)

	def post(self, request, *args, **kwargs):
		nutrisumhistory = NutrisumHistoryModel.objects.filter(public=True)

		context = {
			'nutrisumhistory_list': nutrisumhistory,
		}

		return render(request, 'nutrisum/nutrisum_social.html', context)

class NutrisumHistoryCRUDView(LoginRequiredMixin, CreateView):
	model = NutrisumHistoryModel
	form_class = NutrisumHistoryForm
	template_name = 'nutrisum/nutrisum_history_crud.html'

	def form_valid(self,form):
		if form.is_valid():
			new_item = form.save(commit=False)
			new_item.owner = self.request.user
		try:
			form.save()
		except IntegrityError:
				messages.error(self.request, 'You already have a log on this date! Please change the date.')
				return super(NutrisumHistoryCRUDView, self).form_invalid(form)
		return super(NutrisumHistoryCRUDView, self).form_valid(form)

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'user': self.request.user})
		return kwargs
	def get_success_url(self):
		pk = self.object.pk
		return reverse_lazy('nutrisum:nutrisum-logdetail', kwargs={'pk':pk})

class NutrisumFoodListView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		food_list = NutrisumFoodListModel.objects.filter(owner=request.user)
		form = NutrisumFoodListForm()

		context = {
			'form' : form,
			'item_list' : food_list,
		}

		return render(request, 'nutrisum/nutrisum_food_list.html', context)

	def post(self, request, *args, **kwargs):
		food_list = NutrisumFoodListModel.objects.filter(owner=request.user)
		form = NutrisumFoodListForm(request.POST)

		if form.is_valid():
			new_item = form.save(commit=False)
			new_item.owner = request.user
			try:
				new_item.save()
			except IntegrityError:
				messages.error(request, 'Item already in the List!')

		context = {
			'form' : form,
			'item_list' : food_list,
		}

		return render(request, 'nutrisum/nutrisum_food_list.html', context)

class NutrisumExerciseListView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		exercise_list = NutrisumExerciseListModel.objects.filter(owner=request.user)
		form = NutrisumExerciseListForm()

		context = {
			'form' : form,
			'item_list' : exercise_list,
		}

		return render(request, 'nutrisum/nutrisum_exercise_list.html', context)

	def post(self, request, *args, **kwargs):
		exercise_list = NutrisumExerciseListModel.objects.filter(owner=request.user)
		form = NutrisumExerciseListForm(request.POST)

		if form.is_valid():
			new_item = form.save(commit=False)
			new_item.owner = request.user
			try:
				new_item.save()
			except IntegrityError:
				messages.error(request, 'Item already in the List!')

		context = {
			'form' : form,
			'item_list' : exercise_list,
		}

		return render(request, 'nutrisum/nutrisum_exercise_list.html', context)

class NutrisumLogDetailView(LoginRequiredMixin, View):
	def get(self, request, pk, *args, **kwargs):
		item = NutrisumHistoryModel.objects.get(pk=pk)
		form = CommentForm()
		comments = CommentModel.objects.filter(log=item).order_by('-created_on')

		context = {
			'item' : item,
			'form' : form,
			'comments' : comments,
		}

		return render(request, 'nutrisum/log_detail.html', context)

	def post(self, request, pk, *args, **kwargs):
		item = NutrisumHistoryModel.objects.get(pk=pk)
		form = CommentForm(request.POST)

		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.owner = request.user
			new_comment.log = item
			new_comment.save()

		comments = CommentModel.objects.filter(log=item).order_by('-created_on')

		form = CommentForm()

		context = {
			'item' : item,
			'form' : form,
			'comments' : comments,
		}

		return render(request, 'nutrisum/log_detail.html', context)

class NutrisumLogDetailUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = NutrisumHistoryModel
	form_class = NutrisumHistoryForm
	template_name = 'nutrisum/log_detail_update.html'

	def form_valid(self,form):
		try:
			form.save()
		except IntegrityError:
				messages.error(self.request, 'You already have a log on this date! Please change the date.')
				return super(NutrisumLogDetailUpdateView, self).form_invalid(form)
		return super(NutrisumLogDetailUpdateView, self).form_valid(form)

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'user': self.request.user})
		return kwargs

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse_lazy('nutrisum:nutrisum-logdetail', kwargs={'pk':pk})

	def test_func(self):
		log = self.get_object()
		return self.request.user == log.owner

class NutrisumLogDetailDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = NutrisumHistoryModel
	template_name = 'nutrisum/delete.html'
	success_url = reverse_lazy('nutrisum:nutrisum-home')

	def test_func(self):
		log = self.get_object()
		return self.request.user == log.owner

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = CommentModel
	template_name = 'nutrisum/delete.html'

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse_lazy('nutrisum:nutrisum-logdetail', kwargs={'pk':pk})

	def test_func(self):
		log = self.get_object()
		return self.request.user == log.owner


class NutrisumFoodListDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = NutrisumFoodListModel
	template_name = 'nutrisum/delete.html'
	success_url = reverse_lazy('nutrisum:nutrisum-food-list')

	def test_func(self):
		log = self.get_object()
		return self.request.user == log.owner

class NutrisumExerciseListDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = NutrisumExerciseListModel
	template_name = 'nutrisum/delete.html'
	success_url = reverse_lazy('nutrisum:nutrisum-exercise-list')

	def test_func(self):
		log = self.get_object()
		return self.request.user == log.owner