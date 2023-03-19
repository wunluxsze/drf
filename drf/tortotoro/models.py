from django.db import models

# Create your models here.
class Grades(models.Model):
    gradename = models.CharField(max_length=200)

    def __str__(self):
        return self.gradename


class Workers(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    fathername = models.CharField(max_length=200)
    login = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    photo = models.ImageField()
    grade = models.ForeignKey(Grades, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = [
        ('добавлен', 'добавлен'),
        ('готовится', 'готовится'),
        ('готов', 'готов'),
        ('отменен', 'отменен'),
        ('оплачен', 'оплачен'),

    ]
    table = models.CharField(max_length=200)
    worker = models.ForeignKey(Workers ,on_delete=models.CASCADE)
    data = models.TimeField()
    status = models.CharField(choices=STATUS, max_length=200)
    price = models.IntegerField()
