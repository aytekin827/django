from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')

    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='등록시간')

    # 테이블 명을 별도로 지정하고 싶을 때 
    class Meta:
        db_table = 'fastcampus_fcuser' # db 테이블 설정
        verbose_name = '페스트캠퍼스 사용자' # admin페이지에서 테이블 출력 이름 설정
        verbose_name_plural = '페스트캠퍼스 사용자'