from django.views.generic import ListView

from app.models import Response


class ResponsesListView(ListView):
    template_name = 'responses.html'
    model = Response
    context_object_name = 'responses'




