from django.db import models


class Contacts(models.Model):
    telegram = models.CharField(verbose_name="Telegram", blank=True, max_length=70)
    email = models.EmailField(verbose_name="Эл.почта*", blank=False)
    phone = models.CharField(verbose_name="Номер телефона", blank=True, max_length=30)
    facebook = models.CharField(verbose_name="Facebook", blank=True, max_length=100)
    linkedin = models.CharField(verbose_name="Linkedin", blank=True, max_length=100)
