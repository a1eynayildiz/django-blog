from django.db import models
from django.utils import timezone

#Post isminde bir tablo oluşturduk
class Post(models.Model):
    title =models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
#Burada da kullanıcıların yorum yapabilmesi için gerekli alanı oluşturuyoruz.

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=100)
    email=models.EmailField()
    body=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.name}'
