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

# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20) # 英雄姓名
    hgender = models.BooleanField(default=True) # 英雄性别
    isDelete = models.BooleanField(default=False) # 逻辑删除
    hcomment = models.CharField(max_length=200) # 英雄描述信息
    # BookInfo类和HeroInfo类之间具有一对多的关系，这个一对多的关系应该定义在多的那个类，也就是HeroInfo类中
    # 注意设置外键时候django1.8版本以后需要on_delete参数，不然会错误
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE) # 英雄与图书表的关系为一对多，所以属性定义在英雄模型类中


# 定义地区类
class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20) # 地区名称
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE) # 自关联属性

    # 该魔法方法用于django后台管理, 对象以什么显示，
    # 此处对象设置为以名称显示,admin.py中如果设置对象展示方式list_display，该方法自动忽略
    def __str__(self):
        return self.atitle

    # 自定义title方法，admin.py里面的list_display可以写上面的属性，也可以写方法名称
    def title(self):
        return self.atitle
    # 后台管理可以通过属性点击排序，方法要支持排序，增加下面的排序依据字段
    title.admin_order_field = 'atitle'
    # 指定该方法的在后台中的标题名称，相当于重新命名
    title.short_description = '地区名称'

    # 自定义parent方法
    def parent(self):
        if self.aParent is None:
            return ''
        else:
            return self.aParent.atitle
    parent.short_description = '父级地区名称'
    

# 图片类，用于上传保存图片
class PicTest(models.Model):
    '''上传图片'''
    # upload_to参数就是上传保存图片的文件夹
    # settings里面设置MEDIA_ROOT路径下面的文件夹，一个应用对应自己应用名称的文件夹
    goods_pic = models.ImageField(upload_to='booktest')