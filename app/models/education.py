from django.core.validators import MinValueValidator
from django.db import models

from app.models.experience import max_value_current_year


class Education(models.Model):
    place = models.CharField(
        verbose_name="Образовательное учреждение", blank=False, max_length=500
    )
    course = models.CharField(verbose_name="Курс/Факультет", blank=True, max_length=200)
    specialization = models.CharField(
        verbose_name="Специализация/Профессия", blank=False
    )
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
        verbose_name="Контакты",
        to="CV",
        related_name="education",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    @property
    def as_dict(self):
        return {
            "id": self.pk,
            "place": self.place,
            "course": self.course,
            "specialization": self.specialization,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "cv_id": self.cv_id,
        }
