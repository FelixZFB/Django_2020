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

    # 该魔法方法用于django后台管理, 对象以什么显示，此处对象设置为以名称显示,admin.py中设置对象展示方式该方法自动忽略
    def __str__(self):
        return self.btitle


# # 英雄类
# # 类名：HeroInfo
# # 英雄姓名：hname
# # 英雄性别：hgender
# # 英雄简介：hcomment
# # 英雄所属图书：hbook   图书-英雄的关系为一对多
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcomment = models.CharField(max_length=100)
    # BookInfo类和HeroInfo类之间具有一对多的关系，这个一对多的关系应该定义在多的那个类，也就是HeroInfo类中
    # 注意设置外键时候django1.8版本以后需要on_delete参数，不然会错误
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE) # 让BookInfo类和HeroInfo类之间建立了一对多的关系

    # 该魔法方法用于django后台管理, 对象以什么显示，此处对象设置为以名称显示,admin.py中设置对象展示方式该方法自动忽略
    def __str__(self):
        return self.hname