import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from app.forms import CVCreationMultiForm
from app.models import Education, Experience


class CVCreateView(LoginRequiredMixin, CreateView):
    template_name = "create_cv.html"
    form_class = CVCreationMultiForm

    def form_valid(self, form):
        form['cv'].instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.request.user.pk})


@csrf_exempt
def json_education(request, *args, **kwargs):
    if request.method == "POST" and request.body:
        education = json.loads(request.body)
        try:
            education = Education.objects.create(**education)
            response = JsonResponse(education.as_dict)
            response.status_code = 201
        except Exception:
            response_data = {"detail": "Некорректный набор данных"}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


@csrf_exempt
def json_experience(request, *args, **kwargs):
    if request.method == "POST" and request.body:
        experience = json.loads(request.body)
        try:
            experience = Experience.objects.create(**experience)
            response = JsonResponse(experience.as_dict)
            response.status_code = 201
        except Exception:
            response_data = {"detail": "Некорректный набор данных"}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response
