from django.db import models

# Create your models here.
class Response(models.Model):
    question1 = models.CharField(max_length=1028)
    question2 = models.CharField(max_length=1028)
    question3 = models.CharField(max_length=1028)
    question4 = models.CharField(max_length=1028)
    question5 = models.CharField(max_length=1028)
    question6 = models.CharField(max_length=1028)
    question7 = models.CharField(max_length=1028)
    question8 = models.CharField(max_length=1028)
    question9 = models.CharField(max_length=1028)
    question10 = models.CharField(max_length=1028)
    question11 = models.CharField(max_length=1028)

    drawing = models.CharField(max_length=1000000000)

class Consent(models.Model):
    consent0 = models.BooleanField()
    consent1 = models.BooleanField()
    consent2 = models.BooleanField()
    consent3 = models.BooleanField()
    consent4 = models.BooleanField()
    consent5 = models.BooleanField()
    consent6 = models.BooleanField()
    consent7 = models.BooleanField()
    consent8 = models.BooleanField()

class Interview(models.Model):
    over18 = models.BooleanField()
    email = models.CharField(max_length=1028)
