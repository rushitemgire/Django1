from django.urls import path

from . import views

urlpatterns = [
    #/webone/
    path('',views.index, name='index'),

    #/webone/1
    path('<int:webone_id>',views.details,name="details")

]