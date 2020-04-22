from django.db import models

# Create your models here.
# 创建自己的模型

# 自定义管理器类,继承django内部的models.Manager
class BookInfoManager(models.Manager):
    '''
    # 图书模型管理器类
    # 1.自定义all方法，修改原始查询集，重写all()方法
    # 默认查询未删除的图书信息
    # 调用父类的成员语法为：super().方法名
    # BookInfo.objects1.all()
    def all(self):
        return super().all().filter(isDelete=False)

    # 2. 在管理器类中定义创建对象的方法
    # 创建模型类，接收参数为属性赋值
    # 自定义一个创建一个图书对象的方法
    # BookInfo.objects1.create_book("abc",date(1980,1,1))
    def create_book(self, title, pub_date):
        # 创建模型类对象self.model可以自动获得模型类的名称，所以图书类名称变化也可以自动获取
        book = self.model() # book = BookInfo
        book.btitle = title
        book.bpub_date = pub_date
        book.bread = 0
        book.bcommet = 0
        book.isDelete = False
        # 将数据插入进数据表
        book.save()
        return book

    # 定义元选项
    # 在模型类中定义类Meta，用于设置元信息，如使用db_table自定义表的名字。
    # 数据表的默认名称为：
    # appname_modelname
    # booktest_bookinfo
    # class Meta:
        # db_table='bookinfo' #指定BookInfo生成的数据表名为bookinfo,我们也可以自定义其它名称作为model_name
        # 指定BookInfo默认生成的数据表名为bookinfo
        # 相当于使用bookinfo替换默认的名称booktest_bookinfo
        # 好处：即使应用名称改变对表名也没有影响
    '''

# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20) # 图书名称
    bpub_date = models.DateField() # 发布日期
    bread = models.IntegerField(default=0) # 阅读量
    bcomment = models.IntegerField(default=0) # 评论量
    isDelete = models.BooleanField(default=False) # 逻辑删除

    # 自定义管理器,本来objects是Django帮我自动生成的管理器对象，objects是models.Manger类的一个对象
    # objects = models.Manager()  objects1 = BookInfoManager() = models.Manager()
    # 实际使用中，自定义objects后的名称还是使用objects，除了重写自定义的方法，其它方法还是继承自models.Manager()
    # 此处自定义一个objects1实际所有功能和默认的objects是相同的
    objects1 = BookInfoManager()

# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20) # 英雄姓名
    hgender = models.BooleanField(default=True) # 英雄性别
    isDelete = models.BooleanField(default=False) # 逻辑删除
    hcomment = models.CharField(max_length=200) # 英雄描述信息
    # BookInfo类和HeroInfo类之间具有一对多的关系，这个一对多的关系应该定义在多的那个类，也就是HeroInfo类中
    # 注意设置外键时候django1.8版本以后需要on_delete参数，不然会错误
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE) # 英雄与图书表的关系为一对多，所以属性定义在英雄模型类中

