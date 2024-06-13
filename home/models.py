from django.db import models

# Create your models here.
class Index(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    emailaddress = models.EmailField(max_length=40)
    bio = models.TextField(max_length=600)
    facebook = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=200, null=True)
    github = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}"

class Experience(models.Model):
    designation = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    started_date = models.IntegerField(max_length=5, null = True)
    end_date = models.CharField(max_length=10, null = True)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.designation}"
  
class Education(models.Model):
    college_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    start_date = models.IntegerField(max_length=5, null = True)
    end_date = models.CharField(max_length=20, null = True)

    def __str__(self):
        return f"{self.college_name}"

class Skills(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Interest(models.Model):
    description = models.TextField(max_length=200)

class Awards(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.title}"
    