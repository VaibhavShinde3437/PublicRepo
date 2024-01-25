from django.shortcuts import render
from rest_framework import generics,status,viewsets, permissions
from .models import Assessment, Question, User
from .permission import SuperuserPermission
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
    
# class SuperUserRegisterView(generics.GenericAPIView):
#     serializer_class = SuperUserRegistrationSerializer
    
#     def post(self, request):
#         user = self.serializer_class(data=request.data)
#         user.is_valid(raise_exception=True)
#         user.save()
#         userauth = user.data
#         return Response(userauth, status=status.HTTP_201_CREATED)
    

class LoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AssessmentView(viewsets.ModelViewSet):
    serializer_class = AssessmentSerializer
    permission_classes = (permissions.IsAuthenticated, SuperuserPermission)
    queryset = Assessment.objects.all()


    def create(self, request):
        if SuperuserPermission.has_permission(self, request):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(created_by=self.request.user, update_by=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({"error" : "Only Admin can create Assessments"})
        

    @action(detail=True, methods=['GET','POST'], serializer_class=QuestionSerializer)
    def questions(self, request, pk):
        if request.method == "GET":
            ques = Question.objects.filter(assessment_id=pk)
            serializer = self.get_serializer(ques, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if SuperuserPermission.has_permission(self, request):
                assess = self.get_object()
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save(assessment=assess, created_by=self.request.user, update_by=self.request.user)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response({"error" : "Only Admin can create Questions"})
            



class QuestionView(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Question.objects.all()


