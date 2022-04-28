from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='제목'
        )# UI에 표시될 내용

    contents = models.TextField(
        verbose_name='내용'
        )# UI에 표시될 내용

    writer = models.ForeignKey(
        'fcuser.Fcuser', 
        on_delete=models.CASCADE,
        verbose_name='작성자'
        )# UI에 표시될 내용

    tags = models.ManyToManyField(
        'tag.Tag',
        verbose_name='테그'
        )

    register_dttm = models.DateTimeField(
        auto_now=True,
        verbose_name='등록시간'
        )
        
    # 클래스의 이름과 저장위치를 알고싶을 때 print(클래스객체)이런식으로 확인할 수 있는데
    # 이때 object클래스의 __str__매서드가 호출되어 반환된 문자열 정보이다.
    def __str__(self):
        return self.title 

    # 테이블 명을 별도로 지정하고 싶을 때 
    class Meta:
        db_table = 'fastcampus_board' # db 테이블 설정
        verbose_name = '페스트캠퍼스 게시글' # admin페이지에서 테이블 출력 이름 설정
        verbose_name_plural = '페스트캠퍼스 게시글'