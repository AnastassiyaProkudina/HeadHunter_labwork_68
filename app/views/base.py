from django.views.generic import RedirectView, TemplateView


class IndexView(TemplateView):
    template_name = "index.html"



class IndexRedirectView(RedirectView):
    pattern_name = "index"
