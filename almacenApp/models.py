from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.role)


class User(models.Model):
    firstName = models.CharField(max_length=30, null=False)
    lastName = models.CharField(max_length=30)
    userName = models.CharField(max_length=15, null=False, unique=True)
    password = models.CharField(max_length=20, null=False)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName


