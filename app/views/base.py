from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, ListView

from accounts.models import Account
from app.models import Vacancy


class IndexView(ListView):
    template_name = "index.html"
    model = Vacancy




class IndexRedirectView(RedirectView):
    pattern_name = "index"
