from django.urls import path

from app.views.base import IndexView
from app.views.cv import (
    CVCreateView,
    json_cv_delete,
    CVChangeView,
    json_cv_update,
    json_cv_publish,
)
from app.views.education import json_education_delete, json_education
from app.views.experience import json_experience
from app.views.responses import ResponsesListView
from app.views.vacancy import (
    VacancyListView,
    VacancyView,
    CreateVacancyView,
    UpdateVacancyView,
    DeleteVacancyView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("profile/<int:pk>/cv/add/", CVCreateView.as_view(), name="cv_add"),
    path("json-education/", json_education, name="json_education"),
    path("json-experience/", json_experience, name="json_experience"),
    path("json-cv-delete/<int:id>", json_cv_delete, name="json_cv_delete"),
    path("json-cv-update/<int:id>", json_cv_update, name="json_cv_update"),
    path("json-cv-publish/<int:id>", json_cv_publish, name="json_cv_publish"),
    path("cv/<int:pk>/", CVChangeView.as_view(), name="cv_update"),
    path(
        "json-education-delete/<int:id>",
        json_education_delete,
        name="json_education_delete",
    ),
    path(
        "user/<int:pk>/vacancies/", VacancyListView.as_view(), name="vacancies"
    ),
    path(
        "vacancy/<int:pk>/",
        VacancyView.as_view(),
        name="vacancy",
    ),
    path("vacancy/add", CreateVacancyView.as_view(), name="vacancy_add"),
    path(
        "user/<int:user_pk>/vacancy/<int:pk>/update/",
        UpdateVacancyView.as_view(),
        name="vacancy_update",
    ),
    path(
        "user/<int:user_pk>/vacancy/<int:pk>/delete/",
        DeleteVacancyView.as_view(),
        name="vacancy_delete",
    ),
    path('user/<int:user_pk>/responses/', ResponsesListView.as_view(), name='responses'),
]
