# coding=utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin

__author__ = 'GoTop'


class DownloadFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = '是否下载视频文件'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'download'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('0', '未下载'),
            ('1', '已下载'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # 未下载
        if self.value() == '0':
            return queryset.filter(file='')
        # 已下载
        if self.value() == '1':
            # 设置了youku model，并且已下载youtube视频文件到本地
            return queryset.exclude(file='')

class UploadFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = '是否上传到优酷'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'upload'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('0', '未上传'),
            ('1', '已上传'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # 未上传到youku
        if self.value() == '0':
            return queryset.filter(youku__youku_video_id='')
        # 已上传到youku
        if self.value() == '1':
            # 设置了youku model，并且已下载youtube视频文件到本地
            return queryset.exclude(youku__youku_video_id='')
