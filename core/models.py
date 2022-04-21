from django.db import models
from django.apps import AppConfig

SEX_CHOICES = (('FEMALE', 'FEMALE'), ('MALE', 'MALE'))
PREFIX_CHOICES = (('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'),
                  ('Dr.', 'Dr.'), ('Engr.', 'Engr.'),
                  ('Proff.', 'Mr.'), ('Proff.', 'Proff.'))
LANG_CHOICES = (('N/A', 'N/A'), ('Beginner', 'Beginner'),
                  ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'),
                  ('Expert', 'Expert'))


class Personal(models.Model):
    title = models.CharField(max_length=7, blank=False, choices=PREFIX_CHOICES)
    full_name = models.CharField(max_length=25, primary_key=True, null=False)
    sex = models.CharField(max_length=7, null=False, choices=SEX_CHOICES)
    address = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=30, blank=True)
    site = models.CharField(max_length=25, blank=True)
    degree = models.CharField(max_length=30, blank=True)
    freelance = models.CharField(max_length=15, blank=True)


class Education(models.Model):
    user = models.ForeignKey(Personal, on_delete=models.CASCADE)
    school = models.CharField(max_length=50, blank=False, null=False)
    course = models.CharField(max_length=25, blank=False, null=False)
    start = models.CharField(max_length=4, blank=False, null=False)
    end = models.CharField(max_length=4, blank=False, null=False)


class OtherTraining(models.Model):
    user = models.ForeignKey(Personal, on_delete=models.CASCADE)
    site = models.CharField(max_length=50, blank=False, null=False)
    course = models.CharField(max_length=25, blank=False, null=False)
    start = models.CharField(max_length=4, blank=False, null=False)
    end = models.CharField(max_length=4, blank=False, null=False)


class ProfExperience(models.Model):
    user = models.ForeignKey(Personal, on_delete=models.CASCADE)
    position = models.CharField(max_length=25, blank=False, null=False)
    company = models.CharField(max_length=25, blank=False, null=False)
    start = models.CharField(max_length=4, blank=False, null=False)
    end = models.CharField(max_length=4, blank=False, null=False)
    description1 = models.TextField(max_length=100, blank=False, null=False)
    description2 = models.TextField(max_length=100, blank=True, null=True)
    description3 = models.TextField(max_length=100, blank=True, null=True)
    description4 = models.TextField(max_length=100, blank=True, null=True)


class Skills(models.Model):
    user = models.ForeignKey(Personal, on_delete=models.CASCADE)
    skill = models.CharField(max_length=20, blank=False, null=False)
    percentage = models.CharField(max_length=3, blank=False, null=False)


class Language(models.Model):
    user = models.ForeignKey(Personal, on_delete=models.CASCADE)
    language = models.CharField(max_length=15, primary_key=True, null=False)
    listening = models.CharField(max_length=13, null=False, choices=LANG_CHOICES)
    reading = models.CharField(max_length=13, null=False, choices=LANG_CHOICES)
    speaking = models.CharField(max_length=13, null=False, choices=LANG_CHOICES)
    writing = models.CharField(max_length=13, null=False, choices=LANG_CHOICES)


class Achievement(models.Model):
    user = models.ForeignKey(Personal, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False, null=False)
    description1 = models.TextField(max_length=100, blank=False, null=False)
    description2 = models.TextField(max_length=100, blank=False, null=False)


class Hobby(models.Model):
    user = models.ForeignKey(Personal, on_delete=models.CASCADE)
    hobby = models.CharField(max_length=15, blank=False, null=False)
    Description = models.CharField(max_length=50, blank=False, null=False)


class Gallery(models.Model):
    user = models.ForeignKey(Personal, on_delete=models.CASCADE)
    image = models.ImageField(max_length=50, blank=False, null=False)
    Description = models.CharField(max_length=50, blank=False, null=False)


class Reference(models.Model):
    user = models.ForeignKey(Personal, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=15, blank=False, null=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    contact = models.CharField(max_length=50, blank=False, null=False)


