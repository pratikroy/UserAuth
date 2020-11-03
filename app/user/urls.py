from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
    path('retrieve/', views.ListUserView.as_view(), name='retrieve'),
    path('manage/<str:email>/', views.UserManageView.as_view(), name='manage'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('search/', views.SearchUserView.as_view(), name='search'),
]
