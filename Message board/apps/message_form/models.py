from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=20, verbose_name='name', primary_key=True)
    email = models.EmailField(verbose_name='email')
    address = models.CharField(max_length=100, verbose_name='address')
    message = models.TextField(verbose_name='message')

    class Meta:
        # 表名
        verbose_name = 'message'
        # 后台管理系统表名
        verbose_name_plural = verbose_name
        # 自己配置表名
        db_table = 'message'