from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView, ListView


from app.models import Vacancy


class IndexView(ListView):
    template_name = "index.html"
    model = Vacancy
    context_object_name = "vacancies"


class IndexRedirectView(RedirectView):
    pattern_name = "index"
