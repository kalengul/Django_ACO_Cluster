from django.contrib import admin
from django.urls import path, include

from PG.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/pg-auth/", include('rest_framework.urls')),
    path("api/v1/all/", AllAPIList.as_view()),
    path("api/v1/pg/", PGAPIList.as_view()),
    path("api/v1/pg/<int:pk>/", PGAPIUpdate.as_view()),
    path("api/v1/pg-delete/<int:pk>/", PGAPIDestroy.as_view()),
    path("api/v1/layer/", LayerAPIList.as_view()),
    path("api/v1/layer/<int:pk>/", LayerAPIUpdate.as_view()),
    path("api/v1/layer-delete/<int:pk>/", LayerAPIDestroy.as_view()),
    path("api/v1/node/", NodeAPIList.as_view()),
    path("api/v1/node/<int:pk>/", NodeAPIUpdate.as_view()),
    path("api/v1/node-delete/<int:pk>/", NodeAPIDestroy.as_view()),
]
