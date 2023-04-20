from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone

from app.models.vacancy import JobCategoryChoice


class StatusChoice(TextChoices):
    ACTIVE = 'ACTIVE', 'Активна'
    NOT_ACTIVE = 'NOT_ACTIVE', 'Неактивна'


class EducationLevelChoice(TextChoices):
    SECONDARY = "secondary", "Среднее"
    SECONDARY_SPECIALIZED = "secondary specialized", "Среднее специальное"
    INCOMPLETE_HIGHER = "incomplete higher", "Неоконченное высшее"
    HIGHER = "higher", "Высшее"
    BACHELOR = "bachelor", "Бакалавр"
    MASTER = "master", "Магистр"
    PhD = "PhD", "Кандидат наук"
    Ph_D = "Ph.D", "Доктор наук"


class CV(models.Model):
    status = models.CharField(
        verbose_name='Статус',
        choices=StatusChoice.choices,
        max_length=20,
        default=StatusChoice.NOT_ACTIVE)

    author = models.ForeignKey(
        verbose_name="Автор",
        to=get_user_model(),
        related_name="cv",
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(
        verbose_name="Имя", blank=False, null=True, max_length=50
    )
    last_name = models.CharField(
        verbose_name="Фамилия", blank=False, null=True, max_length=50
    )
    job_category = models.TextField(
        max_length=100,
        choices=JobCategoryChoice.choices,
        verbose_name="Уровень образования",
        default=JobCategoryChoice.OTHER,
        blank=False,
    )
    position = models.CharField(
        verbose_name="Должность", blank=False, null=True, max_length=50
    )
    salary = models.IntegerField(verbose_name="Зарплата", blank=False, null=True)
    education_level = models.TextField(
        max_length=100,
        choices=EducationLevelChoice.choices,
        verbose_name="Уровень образования",
        default=EducationLevelChoice.SECONDARY,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
    )
    contacts = models.ForeignKey(
        verbose_name="Контакты",
        to="Contacts",
        related_name="cv_contacts",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def update(self, using=None, keep_parents=False):
        self.update_at = timezone.now()
        self.save()
