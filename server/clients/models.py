from django.db import models


class Csv(models.Model):
    file = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File id: {self.id}'


class Deal(models.Model):
    customer = models.CharField(max_length=120)
    item = models.CharField(max_length=150)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
