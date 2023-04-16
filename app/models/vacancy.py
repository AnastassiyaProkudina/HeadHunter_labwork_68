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


# class Vacancy(models.Model):
#     text = models.TextField(
#         verbose_name="Текст", null=False, max_length=2200, blank=True
#     )
#     author = models.ForeignKey(
#         verbose_name="Автор",
#         to=get_user_model(),
#         related_name="vacancies",
#         on_delete=models.CASCADE,
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name="Время создания",
#     )
#     updated_at = models.DateTimeField(
#         auto_now=True,
#         verbose_name="Дата и время обновления",
#     )
