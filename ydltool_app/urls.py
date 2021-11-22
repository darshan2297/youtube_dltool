from django.urls import path
from ydltool_app.views import youtubeDLTool,Downloader

urlpatterns = [
    path('extractinfo',youtubeDLTool.extractVideoInfo,name='extractinfo'),
    path('download',Downloader.download,name='download'),
]
