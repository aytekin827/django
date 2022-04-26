from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username','password','registered_dttm')
    # fcuser admin페이지에서 칼럼에 나타낼 값들을 정해줄 수 있따.

# admin/fc_user(앱이름)/fcuser로 라우팅될때 FCuserAdmin이라는 클래스가 리턴되도록
admin.site.register(Fcuser, FcuserAdmin) 