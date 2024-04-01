from rest_framework import routers

from .views import (
    UserViewSet,
    GovernmentAgencyViewSet,
    UserGovernmentAgencyViewSet,
    IdentityProviderViewSet,
    ServiceViewSet,
    UserServiceAccessViewSet,
    UserAuthenticationLogViewSet,
    AuthorizationViewSet,
    SecurityProtocolViewSet,
    RegulatoryComplianceViewSet,
    UserExperienceViewSet,
    AdministrativeProcessViewSet,
    ProjectViewSet,
    SocialLoginViewSet,
)


router = routers.DefaultRouter()

router.register(r"User", UserViewSet, basename="User")
router.register(
    r"GovernmentAgency", GovernmentAgencyViewSet, basename="GovernmentAgency"
)
router.register(
    r"UserGovernmentAgency",
    UserGovernmentAgencyViewSet,
    basename="UserGovernmentAgency",
)
router.register(
    r"IdentityProvider", IdentityProviderViewSet, basename="IdentityProvider"
)
router.register(r"Service", ServiceViewSet, basename="Service")
router.register(
    r"UserServiceAccess", UserServiceAccessViewSet, basename="UserServiceAccess"
)
router.register(
    r"UserAuthenticationLog",
    UserAuthenticationLogViewSet,
    basename="UserAuthenticationLog",
)
router.register(r"Authorization", AuthorizationViewSet, basename="Authorization")

router.register(
    r"SecurityProtocol", SecurityProtocolViewSet, basename="SecurityProtocol"
)
router.register(
    r"RegulatoryCompliance",
    RegulatoryComplianceViewSet,
    basename="RegulatoryCompliance",
)
router.register(r"UserExperience", UserExperienceViewSet, basename="UserExperience")
router.register(
    r"AdministrativeProcess",
    AdministrativeProcessViewSet,
    basename="AdministrativeProcess",
)
router.register(r"Project", ProjectViewSet, basename="Project")
router.register(r"SocialLogin", SocialLoginViewSet, basename="SocialLogin")


urlpatterns = router.urls
