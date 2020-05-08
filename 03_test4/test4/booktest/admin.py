# Register your models here.

# test4文件夹右键标记为source root
from django.contrib import admin
from booktest.models import BookInfo,HeroInfo,AreaInfo


# 自定义管理模型类
# 图书模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    # 后台管理显示的内容，列表里面是要显示的列的名称
    list_display = ['id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'isDelete']
# 英雄模型管理类
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname','hgender','hcomment', 'hbook', 'isDelete']



class AreaStackedInline(admin.StackedInline):
    '''栏目方式嵌入数据'''
    # 先写多类的名字
    model = AreaInfo
    # 显示空白栏的数量
    extra = 2

class AreaTabularInline(admin.TabularInline):
    '''表格方式嵌入数据'''
    # 先写多类的名字
    model = AreaInfo
    # 显示空白栏的数量
    extra = 2


# 地区类
class AreaInfoAdmin(admin.ModelAdmin):
    # 数据表显示的内容，即列的标题, title和parent是模型类里面定义的方法
    list_display = ['id', 'atitle', 'title','aParent', 'parent']
    list_per_page = 5 # 指定每页显示的数据条数
    # 显示操作框在底部，默认是顶部
    actions_on_bottom = True
    actions_on_top = False
    # 右侧显示过滤栏,指定过滤字段
    list_filter = ['atitle']
    # 显示搜索框,指定搜索字段
    search_fields = ['atitle']

    # 显示地区元素详情页内容，显示顺序调整
    # fields = ['aParent', 'atitle']
    # fieldsets设置更加详细的信息，fields和fieldsets只能使用一个
    fieldsets = (
        ('地级市', {'fields': ['atitle']}),
        ('省份', {'fields': ['aParent']})
    )

    # 上面查看市时候已经显示了省份信息，我们想在页面显示成都市下面所有区信息
    # 页面嵌入数据，栏目和表格两种方式
    # inlines = [AreaStackedInline]
    inlines = [AreaTabularInline]



# 注册管理模型类到后台管理中，注意，先自定义后然后再注册，并且注册时候同一个类写在一起注册
# 注册图书类和自定义的图书模型管理类到后台管理中，注册后刷新后台已经显示所有信息了
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(AreaInfo, AreaInfoAdmin)