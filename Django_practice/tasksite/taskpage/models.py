from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    country = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    date = models.DateTimeField("Created on")

    def __str__(self):
        return self.user_name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField("Created on")
    status = models.BooleanField(default=False)
    asign = models.ManyToManyField(User, related_name='task_asign')

    def __str__(self):
        return self.title

    def assign_user(self):
        return ",".join([str(p) for p in self.asign.all()])