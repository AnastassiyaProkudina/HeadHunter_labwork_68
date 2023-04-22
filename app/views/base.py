from django.views.generic import RedirectView, ListView

from app.models import Vacancy


class IndexView(ListView):
    template_name = "index.html"
    model = Vacancy



class IndexRedirectView(RedirectView):
    pattern_name = "index"
