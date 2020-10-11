from django.shortcuts import render  # django의 단축함수인 render()를 사용합니다
from django.shortcuts import get_object_or_404
from .models import Question  # Question 테이블에 엑세스하기 위해 polls.models.Question 클래스를 임포트합니다.


def index(request):  # 뷰 함수를 정의합니다. request 객체는 뷰 함수의 필수 인자입니다.
    latest_question_list = Question.objects.all().order_by('-pub_date')[
                           :5]  # 템플릿에게 넘겨줄 객체 latest_question_list를 만들어 넘겨줄 준비를 하며\
    # latest_question_list 객체는 Question 테이블 객체에서 pub_date 칼럼 뒤의 5개를 가져옵니다.
    context = {'latest_question_list': latest_question_list}  # dict 타입으로 매핑해서 보내줍니다.
    return render(request, 'polls/index.html', context)  # render() 함수는 템플릿 파일인 polls/index.html에 context 변수를 적용하여\
    # 사용자에게 보여줄 최종 HTML 텍스트를 만들고 이를 HttpResponse 객체로 만들어서 반환합니다.


# index() 뷰 함수는 최종적으로 클라이언트에게 응답할 데이터인 HttpResponse 객체를 반환합니다.


def detail(request, question_id):  # 뷰 함수를 정의하여 reqeust 필수 객체에 question_id 인자를 받습니다.
    # 이전의 URL 패턴에서 정규식으로 추출한 question_id 파라미터가 뷰 함수의 인자로 넘어옵니다.
    question = get_object_or_404(Question, pk=question_id)  # 단축함수 get_object_or_404입니다.
    # Question 모델 클래스로부터 pk가question_id로 입력받은 값과 비교합니다. 조건에 맞는 객체가 없으면 404에러를 발생합니다.
    context = {'question': question}
    return render(request, 'polls/detail.html', context)
    # polls/detail.html에 컨텍스트 변수를 추가하여 HTML텍스트를 만들고 HttpResponse객체를 반환합니다.
    # 템플릿에게 넘겨주는 컨텍스트 사전을 render() 함수의 인자로 직접 써주고 있으며, 템플릿에서는 question이란 변수를 사용 할 수 있게 되었습니다.
    # detail() 뷰 함수는 최종적으로 detail.html의 텍스트 데이터를 담은 HttpResponse 객체를 반환합니다.


from django.http import HttpResponseRedirect, HttpResponse  # 리다이렉트 클래스를 사용합니다
from django.urls import reverse  # url 처리를 위한 reverse() 함수를 임포트합니다
from .models import Choice


def vote(request, question_id):  # 뷰 함수 정의 question_id는 urls에서 정의해놓았음
    question = get_object_or_404(Question,
                                 pk=question_id)  # get_object_or_404() 단축함수를 사용하며 검색조건은 pk=request.POST['choice']입니다

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST는 제출된 폼의 데이터를 담고 있는 객체로, 파이썬 사전처럼 키로 그 값을 구할 수 있습니다. request.POST['choice']는 폼데이터에서
        # 키가 choice에 해당하는 choice.id를 스트링으로 가져옵니다.
    except (KeyError, Choice.DoesNotExist):  # 폼의 POSt 데이터에서 'choice'라는 키가 없으면 에러를 발생시킵니다. 객체가없으면 Choice...에러가 발생합니다
        # 이 에러는 python상의 에러인지 DB상의 에러인지를 구별하는 역할을 합니다
        # 설문 투표 폼을 다시 보여준다
        context = {'question': question, 'error_message': "You didn't select a choice."}
        return render(request, 'polls/detail.html', context)
        # exception이 발생하면 render() 함수에 의해서 question과 error_message 컨텍스트 변수를
        # detail.html 템플릿으로 전달합니다. 그 결과 사용자에게는 에러 메세지와 질문 항목을 다시 보여줍니다.

    else:  # 예외가 발생하지 않고 정상적으로 처리 된 경우
        selected_choice.votes += 1  # 선택값 1 추가
        selected_choice.save()  # 변경사항 저장
        # POST 데이터를 정상적으로 처리하였으면,
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리합니다.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
        # view함수가 반환하는 객체는 HttpResponse가 아니라 HttpResponseReirect입니다.
        # HttpResponseRedirect 객체의 생성자는 리다이렉트할 타겟 URL을 인자로 받습니다. 타겟은 reverse()함수로 만듭니다.

        # 최종적으로 vote()뷰 함수는 리다이렉트할 URL을 담은 HttpResponseRedirect 객체를 반환합니다.
        # 이처럼 웹 프로그램에서 POST 방식의 폼 데이터를 처리하는 경우, 그 결과를 보여줄 수 있는 페이지로 이동시키기 위해
        # HttpResponseRedirect 객체를 리턴하는 것이 일반적입니다


def result(request, question_id):  #받는 객체는 다음과 같습니다 path('polls/<int:question_id>/results/', views.results, name='results')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})
    # 최종적으로 results.html템플릿 코드를 렌더링한 결과인 HTML 텍스트 데이터를 담은 HttpResponse 객체를 반환합니다.
