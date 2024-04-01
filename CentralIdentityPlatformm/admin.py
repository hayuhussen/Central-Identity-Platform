from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(GovernmentAgency)
admin.site.register(UserGovernmentAgency)
admin.site.register(IdentityProvider)
admin.site.register(Service)
admin.site.register(UserServiceAccess)
admin.site.register(UserAuthenticationLog)
admin.site.register(Authorization)
admin.site.register(SecurityProtocol)
admin.site.register(RegulatoryCompliance)
admin.site.register(UserExperience)
admin.site.register(AdministrativeProcess)
admin.site.register(Project)
admin.site.register(SocialLogin)
