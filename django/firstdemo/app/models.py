from django.db import models

# Create your models here.
class Today(models.Model):
    class Meta:
        db_table = 'today'#指定数据表的名称
    date = models.CharField(max_length=20)
    json = models.TextField()
    update_time = models.DateTimeField(auto_now=True)

class Actionlog(models.Model):
    class Meta:
        db_table = 'action_log'  # 指定数据表的名称
    id=models.AutoField(primary_key=True)
    ip=models.CharField(max_length=20)
    dist=models.CharField(max_length=255,null=True)
    create_time=models.DateTimeField(auto_now_add=True)
    updata_time=models.DateTimeField(auto_now=True)