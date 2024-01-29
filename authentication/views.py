from django.shortcuts import render
from rest_framework import generics,status,viewsets, permissions
from .models import Assessment, Question, User, AssessmentAssign, SubmittedAssessment
from .permission import SuperuserPermission
from .serializer import AssessmentSerializer, QuestionSerializer, ResgisterSerializer, LoginSerializer, AssessmentAssignSerializer, SubmittedAssessmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from project import settings

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

class AssessmentAssignView(viewsets.ModelViewSet):
    serializer_class=AssessmentAssignSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Assessment.objects.all()

    def create(self, request):
        if SuperuserPermission.has_permission(self, request):
            input = request.data
            data = AssessmentAssign.objects.filter(**input).exists()
            user_data = ResgisterSerializer(User.objects.get(id=input.get('user_id')))
            email = user_data.data.get("email")
            if not data:
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                send_mail("Assessment Assigned","Hi "+user_data.data.get('username')+", an Assessment has been assigned to you plz check", settings.EMAIL_HOST_USER, (email,),fail_silently=False )
                return Response("Email has been sent", status=status.HTTP_200_OK)
            send_mail("Assessment Assigned","Hi "+user_data.data.get('username')+", an Assessment has been assigned again to you plz check", settings.EMAIL_HOST_USER, (email,),fail_silently=False )
            return Response("Email has been sent", status=status.HTTP_200_OK)
        return Response("Only admin can assign assessments", status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        if SuperuserPermission.has_permission(self, request):
            assess = AssessmentAssign.objects.values('assess_id')
            result = Assessment.objects.filter(id__in=assess)
            serializer = AssessmentSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        assess = AssessmentAssign.objects.filter(user_id=self.request.user.id).values('assess_id')
        result = Assessment.objects.filter(id__in=assess)
        serializer = AssessmentSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubmittedAssessmentView(viewsets.ModelViewSet):
    serializer_class = SubmittedAssessmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SubmittedAssessment.objects.all()

    def create(self, request):
        input = request.data
        data = AssessmentAssign.objects.filter(**input)
        user_data = ResgisterSerializer(User.objects.get(id=input.get('user_id')))
        email = user_data.data.get("email")
        if str(self.request.user.id) == request.data.get('user_id'):
            if data.exists():
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                data.delete()
                send_mail("Assessment Submitted",user_data.data.get('username')+", submitted an Assessment", email, [settings.EMAIL_HOST_USER], fail_silently=False )
                return Response("Email has been sent", status=status.HTTP_200_OK)
            return Response("Assement has been not assigned or already submitted", status=status.HTTP_400_BAD_REQUEST)
        return Response("Cannot submit the Assessment of other Users")
    
    def list(self, request):
        if SuperuserPermission.has_permission(self, request):
            assess = SubmittedAssessment.objects.values('assess_id')
            result = Assessment.objects.filter(id__in=assess)
            serializer = AssessmentSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        assess = SubmittedAssessment.objects.filter(user_id=self.request.user.id).values('assess_id')
        result = Assessment.objects.filter(id__in=assess)
        serializer = AssessmentSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

