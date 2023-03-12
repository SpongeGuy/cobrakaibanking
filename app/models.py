from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

user = User.objects.create_user('myusername', 'myemail@cobrakai.com', 'mypassword')

user.first_name = 'Bill'
user.last_name = 'Clinton'
user.save()

class new_user(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)

