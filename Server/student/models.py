from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Student(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)
    mobile = models.CharField(max_length=25, blank=False, null=False)
    college_id = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
