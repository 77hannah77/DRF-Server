from django.contrib import admin
from django.urls import path,include

from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'post',PostViewSet)

urlpatterns=[
    path('',include(router.urls)),
]


# urlpatterns = [
    
#     path('',PostViewSet.as_view({'get':'list','post':'create'})),
#     path('<int:pk>',PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),
    
#     # path('retrieve/<int:pk>/',PostRetrieveAPIView.as_view()),
#     # path('update/<int:pk>/',PostUpdateAPIView.as_view()),
#     # path('destroy/<int:pk>/',PostDestroyAPIView.as_view()), 
# ]



