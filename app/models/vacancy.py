from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices


class JobCategoryChoice(TextChoices):
    OTHER = "other", "Другое"
    FINANCE = "finance", "Финансы"
    JURISPRUDENCE = "jurisprudence", "Юриспруденция"
    IT = "IT", "IT"
    DOMESTIC_SERVICES = "domestic services", "Бытовые услуги"
    MANAGEMENT = "management", "Менеджмент"
    MARKETING = "marketing", "Маркетинг"
    ART = "art", "Искусство"
    TOURISM = "tourism", "Туризм"


class Vacancy(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='vacancies',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    job_title = models.CharField(
        verbose_name="Должность",
        max_length=50,
        null=False,
        blank=False
    )
    category = models.CharField(
        verbose_name='Категория',
        choices=JobCategoryChoice.choices,
        default=JobCategoryChoice.OTHER
    )
    salary = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Зарплата',
    )
    description = models.TextField(
        verbose_name="Описание вакансии",
        blank=True,
        null=True
    )
    min_experience = models.IntegerField(
        verbose_name='Минимальный опыт',
        null=False,
        blank=False,
    )
    max_experience = models.IntegerField(
        verbose_name='Максимальный опыт',
        null=False,
        blank=False,
    )
    is_published = models.BooleanField(
        verbose_name='Видимость вакансии',
        default=False,
        null=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
    )

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"



