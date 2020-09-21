from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=32, unique=True)
    desc = models.TextField(db_index=True)
    price = models.IntegerField()
    count = models.PositiveSmallIntegerField(null=True)
    # 1 - много
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # много - много
    # categories = models.ManyToManyField(Category)
    # 1 - 1
    # category = models.OneToOneField(category)

    def __str__(self):
        return f'{self.name}'

    # полезные типы
    # t = models.DateTimeField()
    # t = models.TimeField()
    # t = models.DateField()
    # t = models.DecimalField()
    # t = models.SmallIntegerField()
    # t = models.PositiveIntegerField()
    # t = models.FloatField()
    # t = models.BooleanField()
    # t = models.ImageField()
    # t = models.FileField()
    # # удобные
    # t = models.URLField()
    # t = models.BinaryField()
