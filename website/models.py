from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Investor(models.Model):
    CHOICE = (
            ('MALE', 'male'),
            ('FEMALE', 'female'),
            )

    RELIGION = (
            ('CHRISTIAN', 'christian'),
            ('MUSLIM', 'muslim'),
            ('OTHERS', 'others'),
            )

    Firstname = models.CharField(max_length=15)
    Surname = models.CharField(max_length=15)
    Othername = models.CharField(max_length=15)
    Gender = models.CharField(max_length=15, choices=CHOICE, default="male")
    Religion = models.CharField(max_length=15, choices=RELIGION, default="christian")

    Date_of_Birth = models.DateField(default=timezone.now)
    Phone = PhoneNumberField(region="NG")
    Whatsapp = PhoneNumberField(region="NG")
    Email = models.EmailField(null=True)

    class Seeds(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    Seed = models.IntegerField(choices=Seeds)
    Address = models.TextField()
    Hobbies = models.TextField()
    Ref = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.Firstname} {self.Surname}"