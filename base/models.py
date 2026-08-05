from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=300)
    is_delete=models.BooleanField(default=False)
    is_complete=models.BooleanField(default=False)
    host=models.ForeignKey(User,on_delete=models.CASCADE)



'''
-->whenever u create any record in the TaskModel by default it 
will be active
-->if u want to delecte or complete it then u need make it inactive
by upadting is_delete or is_complete field to True respection

-->Home page- filter out the record where is_delete and 
is_complete=False
-->complete page -filter out the record where is_delete=Fasle and is_complete=True
-->trash page - filter out the records where is_delete and is_complete = False

--> relationship between the User Model and task model one to many relationship 

User Model - primary table
id(pk)   first_name  last_name  email  username  password
1     user1     1          user1  user1      1234
2     uesr1     2          user1  user2      1234


Taskmodel - Secondary table
id  title  desc  is_delete  is_complete host_id(fk)
'''
