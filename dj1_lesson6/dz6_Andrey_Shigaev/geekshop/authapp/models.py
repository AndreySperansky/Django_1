from django.db import models
from django.contrib.auth.models import AbstractUser



class ShopUser(AbstractUser):
    
    SEX_MAIL = 'mail'
    SEX_FEMAIL = 'femail'
    SEX_OTHER = 'other'
    
    SEX_CHOICE = (
        (SEX_MAIL, 'Мужской'),
        (SEX_FEMAIL, 'Женский'),
        (SEX_OTHER, 'Не указан')
    )
    
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст')
    sex = models.CharField(max_length = 6, choices=SEX_CHOICE, default = SEX_OTHER, verbose_name = 'Пол')    # male, female