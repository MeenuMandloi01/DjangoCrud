from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
