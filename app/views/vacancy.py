from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from accounts.models import Account
from app.forms import VacancyForm
from app.models import Vacancy


class VacancyListView(LoginRequiredMixin, ListView):
    template_name = 'vacancies.html'
    model = Vacancy

    def get(self, request, pk, *args, **kwargs):
        self.user_obj = get_object_or_404(Account, pk=pk)
        vac_pk = request.GET.get('vac_pk')
        public = request.GET.get('public')

        if public:
            vacancy = get_object_or_404(Vacancy, pk=vac_pk)
            vacancy.is_published = 0
            vacancy.save()
        not_public = request.GET.get('not_public')
        if not_public:
            vacancy = get_object_or_404(Vacancy, pk=vac_pk)
            vacancy.is_published = 1
            vacancy.save()
        update = request.GET.get('update')
        if update:
            vacancy = get_object_or_404(Vacancy, pk=vac_pk)
            vacancy.save()
        return super(VacancyListView, self).get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = Vacancy.objects.filter(author_id=self.request.user.pk).order_by('-updated_at')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user_obj'] = self.user_obj
        return context


class VacancyView(LoginRequiredMixin, DetailView):
    template_name = 'vacancy.html'
    model = Vacancy
    context_object_name = 'vacancy'

    def get(self, request, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, pk=kwargs.get('pk'))
        self.user_obj = vacancy.author
        update = request.GET.get('update')
        if update:
            vacancy.save()
        return super(VacancyView, self).get(request, *args, **kwargs)



class CreateVacancyView(LoginRequiredMixin, CreateView):
    template_name = 'create_vacancy.html'
    model = Vacancy
    form_class = VacancyForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.author = request.user
            vacancy.save()
            return redirect('vacancies', pk=self.request.user.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('vacancies', kwargs={'pk': self.request.user.pk})


class UpdateVacancyView(LoginRequiredMixin, UpdateView):
    template_name = 'update_vacancy.html'
    model = Vacancy
    form_class = VacancyForm
    permission_required = 'webapp.change_vacancies'

    def get_success_url(self):
        return reverse('vacancy', kwargs={'user_pk': self.request.user.pk, 'pk': self.object.pk})


class DeleteVacancyView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_vacancy.html'
    model = Vacancy
    context_object_name = 'vacancy'

    def get_success_url(self):
        return reverse('vacancies', kwargs={'pk': self.request.user.pk})
