from django.db import models
from ckeditor.fields import RichTextField
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage
import sys
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_img = models.FileField(blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekleyin")
    def __str__(self):
        return self.title
    class Meta :
        ordering = ["-created_at"]

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ["-comment_date"]


