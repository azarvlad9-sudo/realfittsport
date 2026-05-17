from django.db import models

class Trainer(models.Model):
    # Додали вибір зірок від 1 до 5
    STARS_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]

    name = models.CharField(max_length=100, verbose_name="Ім'я тренера")
    specialization = models.CharField(max_length=100, verbose_name="Спеціалізація", blank=True)
    photo = models.ImageField(upload_to='trainer_photos/', blank=True, null=True, verbose_name="Фото тренера")
    rating = models.IntegerField(choices=STARS_CHOICES, default=5, verbose_name="Рейтинг (Зірки)")

    def __str__(self):
        return f"{self.name} ({self.get_rating_display()})"

class Client(models.Model):
    SUB_TYPES = [
        ('day', 'На день'),
        ('month', 'Місяць'),
        ('year', 'Рік'),
    ]

    full_name = models.CharField(max_length=200, verbose_name="Прізвище та ім'я")
    phone = models.CharField(max_length=20, verbose_name="Номер телефону")
    sub_type = models.CharField(max_length=10, choices=SUB_TYPES, default='month', verbose_name="Тип абонемента")
    photo = models.ImageField(upload_to='client_photos/', blank=True, null=True, verbose_name="Фото клієнта")
    is_active = models.BooleanField(default=True, verbose_name="Активний статус")
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тренер")

    def __str__(self):
        return self.full_name