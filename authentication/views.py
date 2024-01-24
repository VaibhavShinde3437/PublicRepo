from django.shortcuts import render
from rest_framework import generics,status,viewsets, permissions
from .models import Assessment, Question, User
from .serializer import AssessmentSerializer, QuestionSerializer, ResgisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

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


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user, update_by=self.request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        

    @action(detail=True, methods=['GET','POST'], serializer_class=QuestionSerializer)
    def questions(self, request, pk):
        if request.method == "GET":
            ques = Question.objects.filter(assessment_id=pk)
            serializer = self.get_serializer(ques, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            assess = self.get_object()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(assessment=assess, created_by=self.request.user, update_by=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            



class QuestionView(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Question.objects.all()


