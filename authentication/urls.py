from django.contrib import admin
from django.urls import path, include
from .views import AssessmentView, QuestionView, RegisterView, LoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'assessment', AssessmentView, basename='assessment')

router.register(r'question', QuestionView, basename='question')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/', include(router.urls)),
    # path('api/assessment/', include(router.urls)),

]