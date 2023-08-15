from django.views.generic import RedirectView, ListView

from app.models import Vacancy


class IndexView(ListView):
    template_name = "index.html"
    model = Vacancy

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_published=True)
        return queryset

class IndexRedirectView(RedirectView):
    pattern_name = "index"
