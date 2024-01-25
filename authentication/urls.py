from django.contrib import admin
from django.urls import path, include
from .views import AssessmentView, QuestionView, RegisterView, LoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'assessments', AssessmentView, basename='assessments')


router2 = DefaultRouter()
router2.register(r'questions', QuestionView, basename='que')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('adminregistration/', SuperUserRegisterView.as_view(), name='superuser-registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/', include(router.urls)),
    path('api/', include(router2.urls)),
]