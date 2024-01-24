from django.shortcuts import render
from rest_framework import generics,status,viewsets, permissions
from .models import Assessment, Question, User
from .serializer import AssessmentSerializer, QuestionSerializer, ResgisterSerializer, LoginSerializer
from rest_framework.response import Response

class RegisterView(generics.GenericAPIView):
    serializer_class = ResgisterSerializer
    
    def post(self, request):
        user = self.serializer_class(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        userauth = user.data
        user = User.objects.get(email = userauth['email'])
        return Response(userauth, status=status.HTTP_201_CREATED)
    

class LoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AssessmentView(viewsets.ModelViewSet):
    serializer_class = AssessmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Assessment.objects.all()

class QuestionView(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Question.objects.all()

    def perform_create(self, serializer):
        return serializer.save(assessment=)
