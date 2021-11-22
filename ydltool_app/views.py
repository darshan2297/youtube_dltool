from django.shortcuts import render
from youtube_dl import YoutubeDL
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ydltool_app.models import videoInfo,userInfo
from django.conf import settings
import os

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class youtubeDLTool(View):

    def getUserObj(request):
        ip_address = get_client_ip(request)
        userObj = userInfo.objects.filter(ip_address=ip_address).first()
        return userObj

    @classmethod
    @csrf_exempt
    def extractVideoInfo(self,request):
        if request.method == 'POST':
            video_url = request.POST['video_url']
            if not self.getUserObj(request):
                userInfo.objects.create(ip_address=get_client_ip(request))

            getVideoInfo = videoInfo.objects.filter(webpageurl=video_url).first()
            if getVideoInfo:
                video_info = getVideoInfo.json_data
            else:
                video_info = YoutubeDL().extract_info(
                    url = video_url,download=False
                )
                videoInfo.objects.create(video_id = video_info['id'],webpageurl=video_info['webpage_url'],json_data=video_info)
                
        return JsonResponse(video_info)

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class Downloader(youtubeDLTool):

    mediaRoot = settings.MEDIA_ROOT

    # def videoInfoObj(self,url):
    #     webpageurl = url
    #     vinfoObj = videoInfo.objects.filter(webpageurl=webpageurl)
    #     return vinfoObj

    def my_hook(d):
        # print(d)
        if d['status'] == 'finished':
            pass
            # file_tuple = os.path.split(os.path.abspath(d['filename']))
            # print("Done downloading {}".format(file_tuple[1]))
        if d['status'] == 'downloading':
            print(d['_percent_str'], d['_eta_str'])


    def setYdlOptions(self,format):
        
        # filename = f"{video_info['title']}.mp3"
        filename = 'file.mp4'
        format = format
        keepvideo = False
        print(format)
        ydl_opts = {
            'format': format,
            'outtmpl':filename,
            'keepvideo': keepvideo,
            'logger': MyLogger(),
            'progress_hooks': [self.my_hook],
        }

        return ydl_opts

    def downloadFile(self,option,video_url):
        ydl = YoutubeDL(option)
        ydl.download([video_url])

    
    def mp3SongsSave(self,title,video_url,extension,resolution):
        makeuserDatafolder = os.path.join(self.mediaRoot,str('userData'))
        if not os.path.exists(makeuserDatafolder):
            os.makedirs(makeuserDatafolder)

        makemp3songsfolder = os.path.join(makeuserDatafolder,str('mp3_songs'))
        if not os.path.exists(makemp3songsfolder):
            os.makedirs(makemp3songsfolder)
        
        if extension != '':
            extension = extension
        else:
            extension = 'mp3'

        if resolution != '':
            resolution = resolution
        else:
            resolution = '320'
        
        filename = f'{title}.{extension}'

        format = 'bestaudio/best'
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':os.path.join(makemp3songsfolder, filename),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
                'keepvideo':True,
            }],
        }
        
        # opt = self.setYdlOptions(self,format)
        # opt['keepvideo'] = False
        # opt['postprocessors'] = [{
        #         'key': 'FFmpegExtractAudio',
        #         'preferredcodec': 'mp3',
        #         'preferredquality': resolution,
        # }]
        # opt['outtmpl'] = os.path.join(makemp3songsfolder, filename)
        print(options)
        # exit()

        self.downloadFile(self,options,video_url)
       

    @classmethod
    @csrf_exempt
    def download(self, request):
        if request.method == 'POST':
            video_url = request.POST['video_url']
            format = request.POST['format']
            codec = request.POST['codec']
            title = request.POST['title']
            extension = request.POST['extension']
            resolution = request.POST['resolution']

            if codec == "vcodec":
                self.mp3SongsSave(self,title,video_url,extension,resolution)
                pass
            elif codec == "acodec":
                pass
            else:
                pass

            ydl = YoutubeDL(self.setYdlOptions(self,format))
            ydl.download([video_url])