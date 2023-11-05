from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=12)
    description = models.TextField()

    def __str__(self):
        return self.email


class Enrollment(models.Model):
    fullName = models.CharField(max_length=55)
    email = models.EmailField()
    gender = models.CharField(max_length=25)
    phoneNumber = models.CharField(max_length=12)
    dob = models.CharField(max_length=50)
    selectMembershipPlan = models.CharField(max_length=200)
    selectTrainer = models.CharField(max_length=55)
    reference = models.CharField(max_length=55)
    address = models.TextField()
    paymentStatus = models.CharField(max_length=55, blank=True, null=True)
    price = models.IntegerField(max_length=55, blank=True, null=True)
    dueDate = models.DateTimeField(blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.fullName


class Trainer(models.Model):
    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    salary = models.IntegerField(max_length=25)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class MembershipPlan(models.Model):
    plan = models.CharField(max_length=185)
    price = models.IntegerField(max_length=55)

    def __int__(self):
        return self.id


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='gallery')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __int__(self):
        return self.id


class Attendence(models.Model):
    select_date = models.DateTimeField(auto_now_add=True)
    phoneNumber = models.CharField(max_length=15)
    logar = models.CharField(max_length=100)
    deslogar = models.CharField(max_length=100)
    select_workout = models.CharField(max_length=100)
    trainer_by = models.CharField(max_length=100)

    def __int__(self):
        return self.id
