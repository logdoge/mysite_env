from django.db import models


# Create your models here.

class User(models.Model):
    gender = (('man', "先生"), ('women', "女士"))


#unique：检测是否唯一
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="先生")
    createdate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username

    class Meta:

        verbose_name = "用户"
        verbose_name_plural = "用户"