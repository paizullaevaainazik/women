# from django.urls import path
# from users import views
# urlpatterns = [
#     path('index/', views.index),
#     path('index2/', views.index2),
#     path('index3/', views.index3),
#     path('practice/', views.practice),
# ]



from django.urls import path

from .views import *
urlpatterns = [path('', index , name = 'home'),
               path('about/', about ,name= 'about'),
]