from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from .serializers import (
    UserSerializer,
    GovernmentAgencySerializer,
    UserGovernmentAgencySerializer,
    IdentityProviderSerializer,
    ServiceSerializer,
    UserServiceAccessSerializer,
    UserAuthenticationLogSerializer,
    AuthorizationSerializer,
    SecurityProtocolSerializer,
    RegulatoryComplianceSerializer,
    UserExperienceSerializer,
    AdministrativeProcessSerializer,
    ProjectSerializer,
    SocialLoginSerializer,
)

from .models import (
    User,
    GovernmentAgency,
    UserGovernmentAgency,
    IdentityProvider,
    Service,
    UserServiceAccess,
    UserAuthenticationLog,
    Authorization,
    SecurityProtocol,
    RegulatoryCompliance,
    UserExperience,
    AdministrativeProcess,
    Project,
    SocialLogin,
)


# Create your views here.
class UserViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = User.objects.filter(status=1).all()
    serializer_class = UserSerializer


class GovernmentAgencyViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = GovernmentAgency.objects.filter(status=1).all()
    serializer_class = GovernmentAgencySerializer


class UserGovernmentAgencyViewSet(viewsets.ModelViewSet):
    queryset = UserGovernmentAgency.objects.filter(user__is_active=True).all()
    serializer_class = UserGovernmentAgencySerializer


class IdentityProviderViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = IdentityProvider.objects.filter(status=1).all()
    serializer_class = IdentityProviderSerializer


class ServiceViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = Service.objects.filter(status=1).all()
    serializer_class = ServiceSerializer


class UserServiceAccessViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = UserServiceAccess.objects.filter(status=1).all()
    serializer_class = UserServiceAccessSerializer


class UserAuthenticationLogViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = UserAuthenticationLog.objects.filter(status=1).all()
    serializer_class = UserAuthenticationLogSerializer


class AuthorizationViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = Authorization.objects.filter(status=1).all()
    serializer_class = AuthorizationSerializer


class SecurityProtocolViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = SecurityProtocol.objects.filter(status=1).all()
    serializer_class = SecurityProtocolSerializer


class RegulatoryComplianceViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = RegulatoryCompliance.objects.filter(status=1).all()
    serializer_class = RegulatoryComplianceSerializer


class UserExperienceViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = UserExperience.objects.filter(status=1).all()
    serializer_class = UserExperienceSerializer


class AdministrativeProcessViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = AdministrativeProcess.objects.filter(status=1).all()
    serializer_class = AdministrativeProcessSerializer


class ProjectViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = Project.objects.filter(status=1).all()
    serializer_class = ProjectSerializer


class SocialLoginViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = SocialLogin.objects.filter(status=1).all()
    serializer_class = SocialLoginSerializer
