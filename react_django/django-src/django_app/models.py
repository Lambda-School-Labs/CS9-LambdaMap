from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=50, default='', unique=True)
    student = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    pwd = models.CharField(max_length=50, default='')

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username

class Students(models.Model):
    username = models.CharField(max_length=50, default='', unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, default='')
    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    linkedIn = models.CharField(max_length=50, default='')
    twitter = models.CharField(max_length=50, default='')
    github = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    relocate = models.BooleanField(default=False)
    remote = models.BooleanField(default=False)

class Employers(models.Model):
    username = models.CharField(max_length=50, default='', unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, default='')
    firstName = models.CharField(max_length=50, default='',)
    lastName = models.CharField(max_length=50, default='',)
    companyName = models.CharField(max_length=50, default='',)
    city = models.CharField(max_length=50, default='',)
    state = models.CharField(max_length=50, default='',)
    currentlySubscribed = models.BooleanField(default=False)

class Student_Phones(models.Model):
    studentID = models.ForeignKey(Students,on_delete=models.CASCADE)
    number = models.CharField(max_length=20,unique=True)

class Employer_Phones(models.Model):
    employerID = models.ForeignKey(Employers,on_delete=models.CASCADE)
    number = models.CharField(max_length=20,unique=True)

class Student_Favorites(models.Model):
    studentID = models.ForeignKey(Students,on_delete=models.CASCADE)
    employerID = models.ForeignKey(Employers,on_delete=models.CASCADE)

class Employer_Favorites(models.Model):
    employerID = models.ForeignKey(Employers,on_delete=models.CASCADE)
    studentID = models.ForeignKey(Students,on_delete=models.CASCADE)

class Messages(models.Model):
    employerID = models.ForeignKey(Employers,on_delete=models.CASCADE)
    studentID = models.ForeignKey(Students,on_delete=models.CASCADE)
    content = models.CharField(max_length=400,unique=True)
    postTime = models.CharField(max_length=400,unique=True)

class Job_Listings(models.Model):
    employerID = models.ForeignKey(Employers,on_delete=models.CASCADE)
    positionTitle = models.CharField(max_length=400,unique=True)
    post_time = models.CharField(max_length=400,unique=True)
    remote = models.BooleanField(default=False)

