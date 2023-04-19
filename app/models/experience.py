import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Experience(models.Model):
    company_name = models.CharField(
        verbose_name="Название компании", blank=False, null=True, max_length=130
    )
    position = models.CharField(
        verbose_name="Должность", blank=False, null=True, max_length=50
    )
    duties = models.TextField(verbose_name="Должностные обязанности", blank=True)
    started_at = models.IntegerField(
        verbose_name="C",
        validators=[MinValueValidator(1960), max_value_current_year],
        blank=False,
    )
    finished_at = models.IntegerField(
        verbose_name="По",
        validators=[MinValueValidator(1960), max_value_current_year],
        blank=False,
    )
    cv = models.ForeignKey(
        verbose_name="опыт",
        to="CV",
        related_name="experience",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    @property
    def as_dict(self):
        return {
            "id": self.pk,
            "company_name": self.company_name,
            "position": self.position,
            "duties": self.duties,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "cv_id": self.cv_id,
        }
