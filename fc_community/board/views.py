from flask import redirect
from fcuser.models import Fcuser
from django.http import Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import BoardForm
from .models import Board

# Create your views here.
def board_detail(request, pk):
    # 예외처리 - 게시글이 없을 경우
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html',{'board':board})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login')


    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            print(user_id)
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            return redirect('/board/list')

    else:
        form = BoardForm()

    return render(request,'board_write.html',{'form':form})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id') # '-'는 역순이라는 뜻
    page = request.GET.get('p',1)
    paginator = Paginator(all_boards,2)

    boards = paginator.get_page(page)
    return render(request,'board_list.html',{'boards':boards})    
