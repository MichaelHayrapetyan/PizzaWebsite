from django.db import models

PIZZA_TYPE_CHOICES = (
    ('thick', 'Thick'),
    ('thin', 'Thin'),
)


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pizza_type = models.CharField(max_length=100)
    dough = models.CharField(max_length=100, choices=PIZZA_TYPE_CHOICES)
    image = models.ImageField(upload_to='pizza_images')
    description = models.TextField()

    def __str__(self):
        return f"{self.company.name} - {self.pizza_type} Pizza"
