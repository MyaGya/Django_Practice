from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),   # polls와 관련된 값은 polls폴더의 urls에서 처리함
    path('', include('polls.urls'))
]