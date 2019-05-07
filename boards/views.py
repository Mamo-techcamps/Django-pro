from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Board

# Create your views here.

# def index(request):
#   boards = Board.objects.all()    # return querySet as strings bcz __str__() in Data model 
#   boards_names = list()
#   for board in boards:
#     boards_names.append(board.name)

#   result_response = '<br>'.join(boards_names)
  
#   return HttpResponse(result_response)
  #return HttpResponse('Hello world, Welcome to Techcampus Ramadan')


def index(request):
  boards = Board.objects.all()
  
  return render(request, 'home.html', {'boards':boards})

  