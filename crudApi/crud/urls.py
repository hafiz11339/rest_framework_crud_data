from django.urls import path
from . import views


from rest_framework.authtoken.views import obtain_auth_token 
urlpatterns = [
    path("create",views.CreateListData.as_view(),name="list"),
    path('list',views.UserList.as_view(),name='list'),
    path("update/<str:pk>",views.UpdateData.as_view(),name="update"),
    path("destroy/<str:pk>",views.DestroyData.as_view(),name="destroy"),
    # This is for toekn 
    #path('get_token',obtain_auth_token),
    path('user',views.UserData.as_view(),name="user"),
    path('login',views.LoginData.as_view(),name="login"),
    path("logout",views.Logout.as_view()),

   
]