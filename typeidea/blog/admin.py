from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag


# Register your models here.
# 分类
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')  # 控制保存后的列表显示字段信息
    fields = ('name', 'status', 'is_nav')  # 控制新增页面显示的字段信息

    def save_model(self, request, obj, form, change):  # 自动设置owner
        obj.owner = request.user  # 获取当前已经登录的用户
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


# 标签
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')  # 控制保存后的列表显示字段信息
    fields = ('name', 'status')  # 控制新增页面显示的字段信息

    def save_model(self, request, obj, form, change):  # 自动设置owner
        obj.owner = request.user  # 获取当前已经登录的用户
        return super(TagAdmin, self).save_model(request, obj, form, change)


# 文章
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'status', 'created_time', 'operator'
    ]
    list_display_links = []

    list_filter = ['category']
    search_fields = ['title', 'category_name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    fields = (
        ('category', 'title'),
        'desc',
        'status',
        'content',
        'tag',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)
