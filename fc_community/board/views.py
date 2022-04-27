from django.shortcuts import render
from .models import Board

# Create your views here.
def board_list(request):
    boards = Board.objects.all().order_by('-id') # '-'는 역순이라는 뜻
    return render(request,'board_list.html',{'boards':boards})    