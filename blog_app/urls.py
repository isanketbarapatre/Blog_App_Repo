from django.urls import path
from . import views

urlpatterns = [
    path("api/posts/", views.BlogListCreateView.as_view(), name ='Create_blog'),
    path("api/posts/<int:pk>/", views.BlogRetrieveUpdateDestroy.as_view(), name = 'Update_blog'),
    path("register/", views.UserCreate.as_view(), name= "register"),

]