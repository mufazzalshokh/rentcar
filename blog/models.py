from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PostTagModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post tag')
        verbose_name_plural = _('post tags')


class PostModel(models.Model):
    title = models.CharField(max_length=512, verbose_name=_('title'))
    image = models.ImageField(upload_to='posts', null=True, blank=True, verbose_name=_('image'))
    video = models.FileField(upload_to='videos/%y', null=True, blank=True, verbose_name=_('video'))
    content = RichTextUploadingField(verbose_name=_('content'))
    brand = models.CharField(max_length=20, verbose_name=_('brand'))
    product_code = models.CharField(max_length=30, verbose_name=_('product_code'))
    availability = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('availability'))
    price = models.FloatField(verbose_name=_('price'))
    quantity = models.IntegerField(verbose_name=_('quantity'))
    tags = models.ManyToManyField(PostTagModel, related_name='posts', verbose_name=_('tags'))
    short_description = models.TextField(null=True, blank=True, verbose_name=_('short_description'))
    long_description = RichTextField(null=True, blank=True, verbose_name=_('long_description'))
    extra_content = models.TextField(null=True, blank=True, verbose_name=_('extra_content'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def get_comments(self):
        return self.comments.order_by('-created_at')

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class CommentModel(models.Model):
    post = models.ForeignKey(
        PostModel,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name=_('post')
    )
    name = models.CharField(max_length=30, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('phone'))
    comment = models.TextField(verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
