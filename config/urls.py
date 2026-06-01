from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.users.urls")),
]

import debug_toolbar

urlpatterns += [
    path("__debug__/", include(debug_toolbar.urls)),
]