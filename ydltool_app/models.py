from django.db import models
from datetime import datetime,timezone

# Create your models here.

class userInfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15,blank=True,null=True,default='')
    email = models.EmailField(max_length=100,null=True,blank=True,default='',unique=True)
    password = models.CharField(max_length=100,null=True,blank=True,default='')
    conf_password = models.CharField(max_length=100,null=True,blank=True,default='')
    ip_address = models.CharField(max_length=50,null=True,blank=True,default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(default=None,blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    
    def softDelete(self):
        self.is_deleted = True
        self.deleted = datetime.now(timezone.utc)
        self.save()


class videoInfo(models.Model):
    id = models.AutoField(primary_key=True)
    video_id = models.CharField(max_length=255,null=True,blank=True,default='')
    webpageurl = models.URLField(max_length=255,null=True,blank=True,default='')
    json_data = models.JSONField(null=True,blank=True,default=dict)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(default=None,blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    
    def softDelete(self):
        self.is_deleted = True
        self.deleted = datetime.now(timezone.utc)
        self.save()

class mp3SongsData(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255,blank=True,null=True,default='')
    file_path = models.FileField(upload_to='userData/mp3_songs',max_length=255,blank=True,null=True,default='')
    user_id = models.ForeignKey(userInfo,on_delete=models.CASCADE,default='',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(default=None,blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    
    def softDelete(self):
        self.is_deleted = True
        self.deleted = datetime.now(timezone.utc)
        self.save()


class audioSongsData(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255,blank=True,null=True,default='')
    file_path = models.FileField(upload_to='userData/audio_songs',max_length=255,blank=True,null=True,default='')
    user_id = models.ForeignKey(userInfo,on_delete=models.CASCADE,default='',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(default=None,blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    
    def softDelete(self):
        self.is_deleted = True
        self.deleted = datetime.now(timezone.utc)
        self.save()


class mp4VideosData(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255,blank=True,null=True,default='')
    file_path = models.FileField(upload_to='userData/mp4_songs',max_length=255,blank=True,null=True,default='')
    user_id = models.ForeignKey(userInfo,on_delete=models.CASCADE,default='',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(default=None,blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    
    def softDelete(self):
        self.is_deleted = True
        self.deleted = datetime.now(timezone.utc)
        self.save()


class zipFileData(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255,blank=True,null=True,default='')
    file_path = models.FileField(upload_to='userData/zip_files',max_length=255,blank=True,null=True,default='')
    media_ids = models.CharField(max_length=50,blank=True,null=True,default='')
    user_id = models.ForeignKey(userInfo,on_delete=models.CASCADE,default='',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(default=None,blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    
    def softDelete(self):
        self.is_deleted = True
        self.deleted = datetime.now(timezone.utc)
        self.save()