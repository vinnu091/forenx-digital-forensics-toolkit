from django.urls import path
from .views import FileHashView,ScanStatusView,ForensicReportView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns=[
    path('hash/',FileHashView.as_view(),name='file-hash'),
    path('token/', TokenObtainPairView.as_view()),
    path('token_refresh/', TokenRefreshView.as_view()),
    path('scan-status/<str:task_id>/', ScanStatusView.as_view()),
    path('generate-report/', ForensicReportView.as_view()),
]