from django.contrib import admin
from backend.srvs.camp.camp.models import (
    Post,
    CompanyPage,
)

admin.site.register(Post)
admin.site.register(CompanyPage)
