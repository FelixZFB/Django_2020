from django.db import models

# Create your models here.
# 创建自己的模型

# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20) # 图书名称
    bpub_date = models.DateField() # 发布日期
    bread = models.IntegerField(default=0) # 阅读量
    bcomment = models.IntegerField(default=0) # 评论量
    isDelete = models.BooleanField(default=False) # 逻辑删除

# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20) # 英雄姓名
    hgender = models.BooleanField(default=True) # 英雄性别
    isDelete = models.BooleanField(default=False) # 逻辑删除
    hcomment = models.CharField(max_length=200) # 英雄描述信息
    # BookInfo类和HeroInfo类之间具有一对多的关系，这个一对多的关系应该定义在多的那个类，也就是HeroInfo类中
    # 注意设置外键时候django1.8版本以后需要on_delete参数，不然会错误
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE) # 英雄与图书表的关系为一对多，所以属性定义在英雄模型类中