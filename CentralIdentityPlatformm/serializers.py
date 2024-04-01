from rest_framework import serializers

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


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "address",
            "phone_number",
            "email",
            "profile_picture",
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
            "gender",
            "dob",
            "country",
            "region",
            "city",
            "remark",
            "kebele",
            "woreda",
            "status",
            "name_in_amharic",
        ]
        read_only_fields = ["id", "remark", "date_joined"]


class GovernmentAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentAgency
        fields = [
            "name",
            "location",
            "contact_email",
            "contact_phone",
            "website",
            "abbreviation",
            "address",
            "zipcode",
            "city",
            "description",
            "status",  # Include the 'status' field here
        ]
        read_only_fields = ["name", "status", "description"]


class UserGovernmentAgencySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserGovernmentAgency
        fields = [
            "user",
            "GovernmentAgency",
        ]
        read_only_fields = ["id", "GovernmentAgency", "user"]


class IdentityProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = IdentityProvider
        fields = [
            "name",
            "description",
            "website",
            "support_email",
            "contact_phone",
            "authentication_protocol",
            "security_level",
            "status",
        ]
        read_only_fields = ["id", "status", "name"]


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = [
            "name",
            "GovernmentAgency",
            "status",
        ]
        read_only_fields = ["id", "status", "name"]


class UserServiceAccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserServiceAccess
        fields = ["user", "service", "is_active", "created_at", "updated_at", "status"]
        read_only_fields = ["id", "status", "created_at"]


class UserAuthenticationLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAuthenticationLog
        fields = [
            "user",
            "login_time",
            "logout_time",
            "is_active",
            "status",
        ]
        read_only_fields = ["id", "status", "is_active"]


class AuthorizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authorization
        fields = [
            "user",
            "activity_time",
            "activity_type",
            "service",
            "role",
            "permission",
            "granted_date",
            "expiration_date",
            "status",
        ]
        read_only_fields = ["id", "status", "expiration_date"]


class SecurityProtocolSerializer(serializers.ModelSerializer):

    class Meta:
        model = SecurityProtocol
        fields = [
            "name",
            "description",
            "implementation_date",
            "encryption_algorithm",
            "key_length",
            "status",
        ]
        read_only_fields = ["id", "status", "implementation_date"]


class RegulatoryComplianceSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegulatoryCompliance
        fields = [
            "name",
            "description",
            "regulation_date",
            "compliance_status",
            "compliance_notes",
            "status",
        ]
        read_only_fields = ["id", "status", "regulation_date"]


class UserExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserExperience
        fields = [
            "user",
            "satisfaction_rating",
            "feedback",
            "compliance_status",
            "last_interaction",
            "status",
        ]
        read_only_fields = ["id", "status", "satisfaction_rating"]


class AdministrativeProcessSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdministrativeProcess
        fields = [
            "name",
            "description",
            "responsible_department",
            "start_date",
            "end_date",
            "status",
        ]
        read_only_fields = ["id", "status", "start_date"]


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "start_date",
            "end_date",
            "budget",
            "status",
            "project_manager",
            "team_members",
        ]
        read_only_fields = ["id", "status", "start_date"]


class SocialLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialLogin
        fields = [
            "user",
            "provider",
            "access_token",
            "social_id",
            "refresh_token",
            "status",
            "token_expires",
        ]
        read_only_fields = ["id", "status", "social_id"]
