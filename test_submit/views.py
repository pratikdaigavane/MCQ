from django.shortcuts import render
from django.http import HttpResponse
from questions.models import Question

score = 0
# Create your views here.

def submit_data(request):
    if request.method == 'POST':
        name = request.POST['object']
        ans = request.POST['ans']
        global score


        print(name)
        print(ans)
        print (Question.objects.get(id=name).correct_option.upper())
        if(Question.objects.get(id=name).correct_option.upper()==ans):
            print ('correct')
            score+=1
            print(score)
        else:
            print('wrong')
        return HttpResponse(score)




