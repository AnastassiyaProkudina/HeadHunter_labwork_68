from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from accounts.models import Account
from app.forms import VacancyForm
from app.models import Vacancy, CV, Response


class VacancyListView(LoginRequiredMixin, ListView):
    template_name = "vacancies.html"
    model = Vacancy

    def get(self, request, pk, *args, **kwargs):
        self.user_obj = get_object_or_404(Account, pk=pk)
        vac_pk = request.GET.get("vac_pk")
        public = request.GET.get("public")

        if public:
            vacancy = get_object_or_404(Vacancy, pk=vac_pk)
            vacancy.is_published = 0
            vacancy.save()
        not_public = request.GET.get("not_public")
        if not_public:
            vacancy = get_object_or_404(Vacancy, pk=vac_pk)
            vacancy.is_published = 1
            vacancy.save()
        update = request.GET.get("update")
        if update:
            vacancy = get_object_or_404(Vacancy, pk=vac_pk)
            vacancy.save()
        return super(VacancyListView, self).get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = Vacancy.objects.filter(
            author_id=self.request.user.pk
        ).order_by("-updated_at")
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["user_obj"] = self.user_obj
        return context


class VacancyView(DetailView):
    template_name = "vacancy.html"
    model = Vacancy
    context_object_name = "vacancy"

    def get(self, request, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, pk=kwargs.get("pk"))
        self.user_obj = vacancy.author
        update = request.GET.get("update")
        if update:
            vacancy.save()
        return super(VacancyView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        cvs = CV.objects.filter(author=request.user)
        obj = self.model.objects.get(pk=kwargs.get('pk'))
        for cv in cvs:
            x = request.POST.get(str(cv.pk))
            if str(x) == "on":
                cv = CV.objects.get(pk=cv.pk)
                resp, created = Response.objects.get_or_create(user=request.user, cv_id=cv.pk, vacancy_id=obj.pk)
                resp.save()
                return redirect(self.request.META.get("HTTP_REFERER"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["user_cvs"] = CV.objects.filter(author=self.request.user, status="ACTIVE")
        return context


class CreateVacancyView(LoginRequiredMixin, CreateView):
    template_name = "create_vacancy.html"
    model = Vacancy
    form_class = VacancyForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.author = request.user
            vacancy.save()
            return redirect("vacancies", pk=self.request.user.pk)
        context = {"form": form}
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse("vacancies", kwargs={"pk": self.request.user.pk})


class UpdateVacancyView(LoginRequiredMixin, UpdateView):
    template_name = "update_vacancy.html"
    model = Vacancy
    form_class = VacancyForm
    permission_required = "webapp.change_vacancies"

    def get_success_url(self):
        return reverse(
            "vacancy",
            kwargs={"user_pk": self.request.user.pk, "pk": self.object.pk},
        )


class DeleteVacancyView(LoginRequiredMixin, DeleteView):
    template_name = "delete_vacancy.html"
    model = Vacancy
    context_object_name = "vacancy"

    def get_success_url(self):
        return reverse("vacancies", kwargs={"pk": self.request.user.pk})
