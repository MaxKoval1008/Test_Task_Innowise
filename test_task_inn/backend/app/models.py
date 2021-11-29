from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    ticket = models.TextField(max_length=1000)
    choice = (
        ('RD', 'Ready'),
        ('NR', 'Not ready'),
        ('FR', 'Frozen'),
    )
    status = models.CharField('choice', choices=choice, max_length=10)

    def __str__(self):
        return self.name
