from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')# UI에 표시될 내용

    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')# UI에 표시될 내용

    registered_dttm = models.DateTimeField(auto_now_add=True,# 장고에 auto_now라는 기능이 있어서 그 시간대 바로 등록 가능.
                                            verbose_name='등록시간')# UI에 표시될 내용

    # 클래스의 이름과 저장위치를 알고싶을 때 print(클래스객체)이런식으로 확인할 수 있는데
    # 이때 object클래스의 __str__매서드가 호출되어 반환된 문자열 정보이다.
    # Fcuser라는 클래스가 문자열로 출력될 때 어떻게 출력시킬지 정해주는 파이썬 내장함수로 원하는 값으로 정해주면 그 값을 출력해주도록 설정할 수 있다.
    def __str__(self):
        return self.username 

    # 테이블 명을 별도로 지정하고 싶을 때 
    class Meta:
        db_table = 'fastcampus_fcuser' # db 테이블 설정
        verbose_name = '페스트캠퍼스 사용자' # admin페이지에서 테이블 출력 이름 설정
        verbose_name_plural = '페스트캠퍼스 사용자'