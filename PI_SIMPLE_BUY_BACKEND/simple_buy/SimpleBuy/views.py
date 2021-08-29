from django.http import HttpResponse
from django.shortcuts import render




def index(request):

    context = {
        'latest_question_list': 'for ',
    }
    return render(request, 'SimpleBuy/index.html')