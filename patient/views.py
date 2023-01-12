from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView, Response, Request, status
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Patient
from .serializers import PatientSerializer
from employee.permissions import (
    IsSecretaryPermission,
    IsDoctorPermission,
    IsDirectorPermission,
)


class PatientView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSecretaryPermission | IsDirectorPermission]

    def post(self, request: Request) -> Response:
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        patients = Patient.objects.all()
        return patients


class PatientCodeView(APIView):
    def get(self, request: Request, patient_code: str) -> Response:
        patient_obj = get_object_or_404(Patient, patient_code=patient_code)
        serializer = PatientSerializer(patient_obj)

        return Response(serializer.data)


class PatientIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSecretaryPermission, IsDirectorPermission]

    def delete(self, request: Request, patient_id: int) -> Response:
        patient_obj = get_object_or_404(Patient, id=patient_id)
        patient_obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
