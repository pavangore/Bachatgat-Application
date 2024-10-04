from django.db import models

# Create your models here.
class BachatGatRegistration(models.Model):
    MR = 'Mr.'
    MRS = 'Mrs.'
    TITLE_CHOICES = [
        (MR, 'Mr.'),
        (MRS, 'Mrs.'),
    ]

    bachatgat_name = models.CharField(max_length=255)
    start_month = models.CharField(max_length=50)
    start_year = models.CharField(max_length=4)
    chairperson_title = models.CharField(max_length=5, choices=TITLE_CHOICES)
    chairperson_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.bachatgat_name





class MemberRegistration(models.Model):
    ROLE_CHOICES = [
        ('Member', 'Member'),
        ('Chairperson', 'Chairperson'),
    ]


    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    entry_month = models.CharField(max_length=20)
    entry_year = models.IntegerField()
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.name