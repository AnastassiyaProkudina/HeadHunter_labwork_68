from django.contrib.auth import get_user_model
from django.db import models


class Response(models.Model):

    user = models.ForeignKey(
        verbose_name="Пользователь",
        to=get_user_model(),
        related_name="response_user",
        on_delete=models.CASCADE,
    )

    cv = models.ForeignKey(
        verbose_name='Резюме',
        to='app.CV',
        on_delete=models.CASCADE,
        related_name='response_cv'
    )
    vacancy = models.ForeignKey(
        verbose_name='Вакансия',
        to='app.Vacancy',
        on_delete=models.CASCADE,
        related_name='response_vacancy'
    )

    def __str__(self):
        return f"{self.cv} {self.vacancy}"

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"