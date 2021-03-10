from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question


def indexx(request,user,a):
    return HttpResponse("Hello, world. You're at the polls index.%s"%user)
    # return HttpResponse("<h1>12345</>")
def index1(request,a):
    return HttpResponse("Hello, world. You're at the polls index. %s"%a)
    # return HttpResponse("<h1>1234567891111</>")
def index2(request,user,a):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse("<h1>1234567890 %s %s</>"%(user,a))
# def detail(request, question_id):
#     return HttpResponse("Detail_You're looking at question %s." % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)#lấy đối tượng Question theo id
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id,stt):
    response = "Results_You're looking at the results of question %s va %s"
    return HttpResponse(response % (question_id, stt))

def vote(request, question_id):
    return HttpResponse("Vote_You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]#sắp xếp list đối tượng Question theo thời gian
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/header.html', context)