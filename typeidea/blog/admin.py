from django.contrib import admin

from .models import Post,Category,Tag

# Register your models here.
# 分类
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','is_nav','created_time')  # 控制保存后的列表显示字段信息
    fields = ('name','status','is_nav')  # 控制新增页面显示的字段信息

    def save_model(self, request, obj, form, change):  # 自动设置owner
        obj.owner = request.user   # 获取当前已经登录的用户
        return super(CategoryAdmin,self).save_model(request,obj,form,change)
# 标签
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','status','created_time')  # 控制保存后的列表显示字段信息
    fields = ('name','status')  # 控制新增页面显示的字段信息

    def save_model(self, request, obj, form, change):  # 自动设置owner
        obj.owner = request.user   # 获取当前已经登录的用户
        return super(TagAdmin,self).save_model(request,obj,form,change)

