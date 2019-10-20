from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    org_name = models.CharField(max_length=255)
    org_contact = models.CharField(max_length=255)
    org_address =models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True,db_index=True)

class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    contact = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True,db_index=True)

class EmailInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    cc = models.CharField(max_length=255)
    msg_body = models.CharField(max_length=255)
    is_phishing = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True,db_index=True)
