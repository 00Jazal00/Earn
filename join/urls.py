from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home, name="Home"),
    path('join_us/',views.Join_us, name="Join_us"),
    path('thanks_for_join/',views.Thanks_for_join, name="Thanks_for_join"),
  
]
