from celery import shared_task
import string
import random
from models import Ticket


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def create_new_object():
    random_name = ''.join([random.choice(string.ascii_letters) for _ in range(100)])
    random_ticket = ''.join([random.choice(string.ascii_letters) for _ in range(100)])
    new_object = Ticket.object.create(name=random_name, ticket=random_ticket, status='NR')
    return new_object.name
