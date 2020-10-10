
from django.urls import path
from . import views           # views 모듈을 가져와서 연결

urlpatterns = [                                                                 # url 매핑 변수
    #path('admin/', admin.site.urls),                                           # admin과 관련된 변수는 필요없음 ( 계층화 )
    path('polls/', views.index, name='index'),                                  # polls 어플리케이션에 대한 URL/ 뷰 매핑 정의
    path('polls/<int:question_id>', views.detail, name='detail'),               # 그 외의 페이지 등
    path('polls/<int:question_id>/results/', views.results, name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote')
]