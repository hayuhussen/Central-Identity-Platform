# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    name_in_amharic = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True
    )
    password = models.CharField(max_length=128)
    status = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    dob = models.DateField()
    country = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    kebele = models.CharField(max_length=255, null=True)
    woreda = models.CharField(max_length=255, null=True)
    remark = models.TextField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email


class GovernmentAgency(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    website = models.URLField()
    abbreviation = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20, default="Active"
    )  # Add the 'status' field here

    def __str__(self):
        return self.name


class UserGovernmentAgency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    GovernmentAgency = models.ForeignKey(GovernmentAgency, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.GovernmentAgency.name}"


class IdentityProvider(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()
    support_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    authentication_protocol = models.CharField(max_length=50)
    security_level = models.CharField(max_length=50)
    status = models.TextField(null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    STATUS_CHOICES = (
        (1, "Active"),
        (2, "Inactive"),
    )
    name = models.CharField(max_length=100)
    GovernmentAgency = models.ForeignKey(GovernmentAgency, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.name


class UserServiceAccess(models.Model):
    STATUS_CHOICES = (
        (1, "Active"),
        (2, "Inactive"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f"{self.user.email} - {self.service.name}"


class UserAuthenticationLog(models.Model):

    STATUS_CHOICES = (
        (1, "Active"),
        (2, "Inactive"),
        # Add other status choices as needed
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f"{self.user.email} - {self.login_time}"


class Authorization(models.Model):
    STATUS_CHOICES = (
        (1, "Active"),
        (2, "Inactive"),
        # Add other status choices as needed
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_time = models.DateTimeField(auto_now_add=True)
    activity_type = models.CharField(max_length=50)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, null=True, blank=True
    )
    role = models.CharField(max_length=100)
    permission = models.CharField(max_length=100)
    granted_date = models.DateField()
    expiration_date = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f"{self.user.email} - {self.service.name} - {self.activity_type}"


class SecurityProtocol(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    implementation_date = models.DateField()
    encryption_algorithm = models.CharField(max_length=50)
    key_length = models.IntegerField()
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class RegulatoryCompliance(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    regulation_date = models.DateField()
    compliance_status = models.BooleanField(default=False)
    compliance_notes = models.TextField(blank=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class UserExperience(models.Model):

    STATUS_CHOICES = (
        (1, "Active"),
        (2, "Inactive"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    satisfaction_rating = models.PositiveIntegerField(
        default=0, verbose_name="Satisfaction Rating (out of 10)"
    )
    feedback = models.TextField(blank=True)
    last_interaction = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f"{self.user.username} - Satisfaction Rating: {self.satisfaction_rating}"


class AdministrativeProcess(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    responsible_department = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Ongoing", "Ongoing"),
            ("Completed", "Completed"),
        ],
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Ongoing", "Ongoing"),
            ("Completed", "Completed"),
        ],
    )
    project_manager = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Application(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     url = models.URLField()


# class UserApplication(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     application = models.ForeignKey(Application, on_delete=models.CASCADE)
#     is_active = models.BooleanField(default=True)


# class AuthenticationMethod(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()


# class AuthenticationRecord(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     authentication_method = models.ForeignKey(
#         AuthenticationMethod, on_delete=models.CASCADE
#     )
#     authentication_time = models.DateTimeField(auto_now_add=True)


# class AuthorizationRecord(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     application = models.ForeignKey(Application, on_delete=models.CASCADE)
#     authorization_time = models.DateTimeField(auto_now_add=True)
#     authorization_data = models.JSONField()


class SocialLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    social_id = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=200, blank=True, null=True)
    token_expires = models.DateTimeField()
    status = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s Social Login ({self.provider})"
