from django.urls import path
from .views import NutrisumHomeView, NutrisumSocialView, NutrisumHistoryCRUDView, NutrisumFoodListView, NutrisumExerciseListView, NutrisumLogDetailView, NutrisumLogDetailUpdateView, NutrisumLogDetailDeleteView, CommentDeleteView, NutrisumFoodListDeleteView, NutrisumExerciseListDeleteView

app_name = 'nutrisum'

urlpatterns = [
	path('home/', NutrisumHomeView.as_view(), name='nutrisum-home'),
	path('social/', NutrisumSocialView.as_view(), name='nutrisum-social'),
	path('crud/', NutrisumHistoryCRUDView.as_view(), name='nutrisumhistory-crud'),
	path('foodlist/', NutrisumFoodListView.as_view(), name='nutrisum-food-list'),
	path('foodlist/delete/<int:pk>', NutrisumFoodListDeleteView.as_view(), name='nutrisum-foodlist-delete'),
	path('exerciselist/', NutrisumExerciseListView.as_view(), name='nutrisum-exercise-list'),
	path('exerciselist/delete/<int:pk>', NutrisumExerciseListDeleteView.as_view(), name='nutrisum-exerciselist-delete'),
	path('logdetail/<int:pk>', NutrisumLogDetailView.as_view(), name='nutrisum-logdetail'),
	path('logdetail/update/<int:pk>', NutrisumLogDetailUpdateView.as_view(), name='nutrisum-logdetail-update'),
	path('logdetail/delete/<int:pk>', NutrisumLogDetailDeleteView.as_view(), name='nutrisum-logdetail-delete'),
	path('logdetail/<int:log_pk>/comment/delete/<int:pk>', CommentDeleteView.as_view(), name='nutrisum-comment-delete'),
]