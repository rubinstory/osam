from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 30)
    account_type = models.CharField(max_length = 30,
                                    choices = ( ('military', '군인'),
                                                ('counselor', '상담사')),
                                    default = "")
    password = models.CharField(max_length=30)
    #tag = 

    def __str__(self):
        return (self.name)

class Military_User(User):
    rank = models.CharField(max_length = 30)
    workplace = models.CharField(max_length = 200)
    def __str__(self):
        return (self.name)

class Counselor_User(User):
    career = models.TextField()
    #photo = 
    def __str__(self):
        return (self.name)
