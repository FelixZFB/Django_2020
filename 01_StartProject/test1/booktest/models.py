from django.db import models
# 设计和表对应的类，模型类
# Create your models here.

# 图书类
class BookInfo(models.Model):
    '''图书模型类'''
    # 表中的id不用定义，会自动生成
    # CharFiled说明是一个字符串，max_length指定字符串的最大长度
    btitle = models.CharField(max_length=20)
    # DateField说明是一个日期类型
    bpub_date = models.DateField()

