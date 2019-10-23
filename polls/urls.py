from django.urls import path

from . import views
app_name='moives'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home,name='home'),
    path('home/<int:movie_id>',views.detail,name='detail'),

]
