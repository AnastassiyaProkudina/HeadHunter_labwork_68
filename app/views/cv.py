import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DeleteView, UpdateView

from app.forms import CVCreationMultiForm
from app.models import Education, Experience, CV


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


def json_cv_delete(request, id, *args, **kwargs):
    cv = get_object_or_404(CV, id=id)
    cv.delete()
    return JsonResponse({'success': True, 'message': 'Delete', 'id': id})


class CVChangeView(UpdateView):
    model = CV
    form_class = CVCreationMultiForm

    def get_form_kwargs(self):
        kwargs = super(CVChangeView, self).get_form_kwargs()
        kwargs.update(instance={
            'cv': self.object,
            'contacts': self.object.contacts,
        })
        return kwargs

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER")
