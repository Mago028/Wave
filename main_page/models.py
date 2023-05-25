from django.db import models

# Create your models here.
class Search(models.Model):
    content = models.CharField(max_length=50) #검색 내용
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'[{self.pk}] {self.title}'
    #문자열 반환 함수
    #return해주는 형식대로 admin사이트에서 보이게 된다.
    
    
    def get_absolute_url(self):
        return f'{self.pk}'