from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(
        max_length=32, 
        verbose_name='테그명'
        )
    registered_dttm = models.DateTimeField(
        auto_now_add=True, # 장고에 auto_now라는 기능이 있어서 그 시간대 바로 등록 가능.
        verbose_name='등록시간' # UI에 표시될 내용
        )

    def __str__(self):
        return self.name

    # 테이블 명을 별도로 지정하고 싶을 때 
    class Meta:
        db_table = 'fastcampus_tag' # db 테이블 설정
        verbose_name = '페스트캠퍼스 테그' # admin페이지에서 테이블 출력 이름 설정
        verbose_name_plural = '페스트캠퍼스 테그'