from django.urls import path

from app.views.base import IndexView
from app.views.cv import CVCreateView, json_cv_delete, CVChangeView
from app.views.education import json_education_delete, json_education
from app.views.experience import json_experience

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("profile/<int:pk>/cv/add/", CVCreateView.as_view(), name="cv_add"),
    path("json-education/", json_education, name="json_education"),
    path("json-experience/", json_experience, name="json_experience"),
    path('json-cv-delete/<int:id>', json_cv_delete, name='json_cv_delete'),
    path("cv/<int:pk>/", CVChangeView.as_view(), name="cv_update"),
    path('json-education-delete/<int:id>', json_education_delete, name='json_education_delete'),
]
