# Register your models here.

# test4文件夹右键标记为source root
from django.contrib import admin
from booktest.models import BookInfo,HeroInfo


# 自定义管理模型类
# 图书模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    # 后台管理显示的内容，列表里面是要显示的列的名称
    list_display = ['id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'isDelete']
# 英雄模型管理类
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname','hgender','hcomment', 'hbook', 'isDelete']


# 注册管理模型类到后台管理中，注意，先自定义后然后再注册，并且注册时候同一个类写在一起注册
# 注册图书类和自定义的图书模型管理类到后台管理中，注册后刷新后台已经显示所有信息了
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)