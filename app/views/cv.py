from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from accounts.models import Account
from app.forms import CVCreationMultiForm
from app.models import CV


class CVCreateView(LoginRequiredMixin, CreateView):
    def get(self, *args, **kwargs):
        user_obj = get_object_or_404(Account, pk=self.kwargs['pk'])
        cv, created = CV.objects.get_or_create(
            first_name=user_obj.first_name,
            last_name=user_obj.last_name,
            author_id=user_obj.id,
            salary=None
        )
        return redirect("cv_update", cv.id)

    def get_form_kwargs(self):
        kwargs = super(CVCreateView, self).get_form_kwargs()
        kwargs.update(instance={
            'cv': self.object,
            'contacts': self.object.contacts,
        })
        return kwargs

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.kwargs['pk']})


def json_cv_delete(request, id, *args, **kwargs):
    cv = get_object_or_404(CV, id=id)
    cv.delete()
    return JsonResponse({'success': True, 'message': 'Delete', 'id': id})


def json_cv_update(request, id, *args, **kwargs):
    cv = get_object_or_404(CV, id=id)
    cv.update()
    return JsonResponse({'success': True, 'message': 'Delete', 'updated': cv.updated_at})


class CVChangeView(LoginRequiredMixin, UpdateView):
    model = CV
    form_class = CVCreationMultiForm
    template_name = "create_cv.html"

    def get_form_kwargs(self):
        kwargs = super(CVChangeView, self).get_form_kwargs()
        kwargs.update(instance={
            'cv': self.object,
            'contacts': self.object.contacts,
        })
        return kwargs

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.request.user.pk})
