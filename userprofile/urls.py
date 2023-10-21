from django.urls import path
from .views import ProfilePageView, ProfilePageUpdateView

app_name = 'userprofile'

urlpatterns = [
	path('profilepage/<str:username>', ProfilePageView.as_view(), name='profilepage'),
	path('profilepage/update/<str:username>', ProfilePageUpdateView.as_view(), name='profilepage-update'),
]