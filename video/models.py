# coding=utf-8
from __future__ import unicode_literals
from django import forms
from django.db import models


class NeedUploadToYouManager(models.Manager):
    def get_queryset(self):
        need_upload_to_youku_queryset = super(NeedUploadToYouManager,
                                              self).get_queryset().filter(
            # 在SQLite数据库中，django model BooleanField True对应1，False对应0
            # 不知道在Django1.7之后的版本是否修改该bug
            allow_upload_youku=1,
            youku__isnull=False,
            youku__youku_video_id='')

        return need_upload_to_youku_queryset


class DownloadedManager(models.Manager):
    def get_queryset(self):
        return super(DownloadedManager, self).get_queryset().filter(
            file__isnull=False)


# Create your models here.
class Video(models.Model):
    video_id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=200, )
    description = models.TextField(max_length=300, blank=True)
    publishedAt = models.DateTimeField(null=True, blank=True)
    thumbnail = models.URLField(max_length=300, blank=True)
    channel = models.ForeignKey('YT_channel', null=True, blank=True)

    title_cn = models.CharField(max_length=150, blank=True)
    subtitle_en = models.CharField(max_length=200, blank=True)
    subtitle_cn = models.CharField(max_length=200, blank=True)
    subtitle_merge = models.CharField(max_length=200, blank=True, null=True)

    # The exception is CharFields and TextFields, which in Django are never saved as NULL.
    #  Blank values are stored in the DB as an empty string ('').
    # Avoid using null on string-based fields such as CharField and TextField because empty string values will always
    #  be stored as empty strings, not as NULL. If a string-based field has null=True, that means it has two possible
    #  values for "no data": NULL, and the empty string. In most cases, it’s redundant to have two possible values
    # for "no data"; the Django convention is to use the empty string, not NULL.
    file = models.CharField(max_length=200, blank=True)
    # youku = models.ForeignKey('Youku', null=True, blank=True)
    subtitle_video_file = models.CharField(max_length=200, blank=True,
                                           null=True)
    allow_upload_youku = models.BooleanField(blank=True, default='True',
                                             help_text='是否可以上传到优酷，默认为True')
    baidu_yun = models.ForeignKey('BaiduYun', null=True, blank=True)
    remark = models.CharField(max_length=300, blank=True)

    objects = models.Manager()
    need_upload_to_youku = NeedUploadToYouManager()
    downloaded = DownloadedManager()

    def __str__(self):
        return self.title

    def thumbnail_image(self):
        return '<img src="%s"/>' % self.thumbnail

    @property
    def youtube_url(self):
        return 'https://www.youtube.com/watch?v=%s' % self.video_id

        # youtube_url = property(_youtube_url)


class YT_channel(models.Model):
    channel_id = models.URLField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)
    thumbnail = models.URLField(max_length=300, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True)
    is_download = models.NullBooleanField(null=True, blank=True)
    remark = models.CharField(max_length=50, blank=True)

    @property
    def url(self):
        url = 'https://www.youtube.com/channel/' + self.channel_id
        return url

    def thumbnail_image(self):
        return '<img src="%s"/>' % self.thumbnail

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'YouTube Channel'
        verbose_name_plural = 'YouTube Channels'


class YouTube(models.Model):
    """
    设置关注youtube的用户，或者
    """
    vid_id = models.CharField(max_length=50)
    vid_url = models.CharField(max_length=50)
    playlist_url = models.URLField(max_length=300)
    user = models.URLField(max_length=300)
    keywords = models.CharField(max_length=50)


# http://cloud.youku.com/docs?id=90
YOUKU_PALYLIST_CATEGORY = (
    ("Games", "游戏"),
    ("Tech", "科技"),
    ("News", "资讯"),
    ("LifeStyle", "生活"),
    ("Original", "原创"),
    ("TV", "电视剧"),
    ("Entertainment", "娱乐"),
    ("Movies", "电影"),
    ("Sports", "体育"),
    ("Music", "音乐"),
    ("Anime", "动漫"),
    ("Fashion", "时尚"),
    ("Parenting", "亲子"),
    ("Autos", "汽车"),
    ("Travel", "旅游"),
    ("Education", "教育"),
    ("Humor", "搞笑"),
    ("Ads", "广告"),
    ("Others", "其他"),
)


class Youku(models.Model):
    # 主键的名称为 id
    # youku_video_id 是视频上传到优酷的video id
    youku_video_id = models.CharField(max_length=50, blank=True)
    # 说明 doc.open.youku.com/?docid=393
    title = models.CharField(max_length=100, blank=True,
                             help_text='视频标题，能填写2-50个字符,上传时必选')
    tags = models.CharField(max_length=50, blank=True,
                            help_text="自定义标签不超过10个，单个标签最少2个字符，最多12个字符（6个汉字），多个标签之间用逗号(,)隔开，上传时必选"
                            )
    description = models.TextField(max_length=300, blank=True, default='',
                                   help_text='视频描述，最多能写2000个字')
    category = models.CharField(max_length=50, blank=True,
                                choices=YOUKU_PALYLIST_CATEGORY)
    published = models.DateTimeField(null=True, blank=True)
    # on_delete=models.SET_NULL 表示如果对应的Video被删除，Youku只将个属性设置为null，不会删除youku对象
    # OneToOneField要设置在 要被显示在inline的model里
    # 参考 http://stackoverflow.com/questions/1744203/django-admin-onetoone-relation-as-an-inline
    # 指向video model，所以youku model会有一个video id属性，注意与youku_video_id的区别
    video = models.OneToOneField('Video', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    youku_playlist = models.ForeignKey('YoukuPlaylist',
                                       on_delete=models.SET_NULL, null=True,
                                       blank=True)

    @property
    def url(self):
        url = 'http://v.youku.com/v_show/id_' + self.youku_video_id + '.html'
        return url

    def __str__(self):
        return self.youku_video_id


class YoukuPlaylist(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    play_link = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    video_count = models.CharField(max_length=10, blank=True, null=True)
    view_count = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class BaiduYun(models.Model):
    uri = models.CharField(max_length=50)


class Category(models.Model):
    title = models.CharField(max_length=50, blank=True)
    youku_playlist_category = models.CharField(max_length=50, blank=True,
                                               choices=YOUKU_PALYLIST_CATEGORY,
                                               default="Others")
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
