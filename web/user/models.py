from django.db import models

Class User(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 30)
    account_type = models.CharField(max_length = 30,
                                    choices = ( ('military', '군인'),
                                                ('counselor', '상담사')),
                                    default = "")
    id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    #tag = 

Class Military_User(User):
    rank = models.CharField(max_length = 30)
    workplace = models.CharField(max_length = 200)

Class Counselor_User(User):
    career = models.TextField()
    #photo = 

    
