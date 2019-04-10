from django.db import models

# Create your models here.


class Tags(models.Model):
    tag_name = models.CharField(verbose_name="标签名称", max_length=255)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Articles(models.Model):
    id = models.AutoField(verbose_name="文章id", primary_key=True)
    title = models.CharField(verbose_name="标题", max_length=255)
    contents = models.TextField(verbose_name="内容")
    date = models.DateTimeField(verbose_name="创建时间", auto_created=True)
    author = models.CharField(verbose_name="作者", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_tags(self):
        return list(self.articletag_set.values_list("tag__tag_name", flat=True))

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

class ArticleTag(models.Model):
    article = models.ForeignKey(verbose_name="文章", to=Articles, on_delete=models.CASCADE)
    tag = models.ForeignKey(verbose_name="标签", to=Tags , on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tag.tag_name
