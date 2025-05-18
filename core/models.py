from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from core.enums import DownloadEnum, TeamEnum

# Create your models here.

class Slider(models.Model):
    header_one = models.CharField(max_length=255, default="Competition and Tariff Commission")
    header_one_color = models.CharField(max_length=255, default="#0E1089")
    header_two = models.CharField(max_length=255, null=True, blank=True)
    header_two_color = models.CharField(max_length=255, default="#ffffff")
    button_text = models.CharField(max_length=255,default="Read more")
    button_link = models.URLField(max_length=255)
    button_color = models.CharField(max_length=255, default="#0E1089")
    background_image = models.ImageField(upload_to="slider")
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header_one

    class Meta:
        ordering = ["-timestamp", ] 

class Division(models.Model):
    heading = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, null=True, blank=True)
    small_description = models.TextField()
    main_description = RichTextUploadingField()
    slug =models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ["-timestamp", ] 

class Folder(models.Model):
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='cover_image')
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-timestamp", ]


class Image(models.Model):
    folder = models.ForeignKey(Folder,on_delete = models.CASCADE, related_name = 'image_folder')
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"image caption {self.caption} :folder {self.folder.name}"
    
    class Meta:
        ordering = ["-timestamp", ]


class Download(models.Model):
    CAT = (
        ('','Select a Category'),
        ("comesa-competition-commission","Comesa Competition Commission"),
        ("commission-decisions","Commission Decisions"),
        ("forms","Forms"),
        ("legal-and-corporate-issues","Legal & Corporate Issues"),
        ("guidelines","Guidelines"),
        ("brochures","Brochures"),
        ("policies","Policies"),
        ("annual-reports","Annual Reports"),
        ("newsletter","Newsletter"),
        ("strategic-plan","Strategic Plan"),
        ("stakeholder-consultations","Stakeholder Consultations"),
        ("sector-studies","Sector Studies"),
        ("african-competition-forum-studies","African Competition Forum Studies"),
        ("analytical-papers","Analytical Papers"),
        ("complaints-form-relating-to-restrictive-practices","Complaints Form relating to Restrictive Practices"),
        ("merger-notification-form","Merger Notification Form"),
        ("dumping-form","Dumping Form"),
        ("summary-merger-decisions","Summary Merger Decisions"),
        )
    
    category = models.CharField(max_length=255, choices=CAT, unique=True)
    file_name = models.CharField(max_length=255) 
    file_size = models.CharField(max_length=255, default="0")  
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"file: {self.file_name}"
    
    class Meta:
        ordering = ["-timestamp", ]

    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)

class Team(models.Model):
    CAT = (
        ('','Select a Category'),
        ('board-of-commissioners',TeamEnum.BOARD_OF_COMMISSIONERS.value),
        ('management',TeamEnum.MANAGEMENT.value),
        ('staff-member',TeamEnum.STAFF_MEMBER.value),
        )
    category = models.CharField(max_length=255, choices=CAT)
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)  
    profile_picture = models.ImageField(upload_to='profile_picture/%Y/%m/%d/')
    facebook = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"file: {self.full_name}"
    
    class Meta:
        ordering = ["-timestamp", ]

class BlogPost(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    author = models.CharField(max_length=255, default='Admin')
    cover_image = models.ImageField(upload_to='news/%Y/%m/%d/')
    content = RichTextUploadingField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('general:detail', kwargs={'slug': self.slug}) 
    
class Media(models.Model):
    CAT = (
        ('','Select a Category'),
        ('radio','Radio'),
        ('tv','TV')
        )
    category = models.CharField(max_length=255, choices=CAT)
    youtube_link = models.URLField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
    
    class Meta:
        ordering = ["-timestamp", ]


class Legislation(models.Model):
    slug = models.SlugField(unique=True, max_length=255, default='legislation')
    content = RichTextUploadingField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug
    
class LegislationFile(models.Model):
    category = models.ForeignKey(Legislation, on_delete=models.CASCADE, related_name="legislation_files")
    file_name = models.CharField(max_length=255) 
    file_size = models.CharField(max_length=255, default="0")  
    file = models.FileField(upload_to='legislation/%Y/%m/%d/')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"file: {self.file_name}"
    
    class Meta:
        ordering = ["-timestamp", ]

    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    JOB_TYPES = (
        ('','Select a category'),
        ('full-time', 'Full time'),
        ('part-time','Part time'),
        ('remote','Remote'),
        ('project','Project')
    )
    job_type = models.CharField(max_length=100,choices=JOB_TYPES)
    job_title = models.CharField(max_length=255) 
    closing_date = models.DateField()
    published = models.BooleanField(default=False)
    file_size = models.CharField(max_length=255, default="0")  
    attachment = models.FileField(upload_to='job/%Y/%m/%d/',blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    slug = models.SlugField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title
    
    class Meta:
        ordering = ["-timestamp", ]

    def save(self, *args, **kwargs):
        if self.attachment:
            self.file_size = self.attachment.size
        super().save(*args, **kwargs)
        

class Emblem(models.Model):
    name = models.CharField(max_length=255) 
    file_size = models.CharField(max_length=255, default="0")  
    link = models.URLField()
    logo = models.FileField(upload_to='emblem/%Y/%m/%d/',blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-timestamp", ]

    def save(self, *args, **kwargs):
        if self.logo:
            self.file_size = self.logo.size
        super().save(*args, **kwargs)

class Tender(models.Model):
    name = models.CharField(max_length=255) 
    file_size = models.CharField(max_length=255, default="0")  
    file = models.FileField(upload_to='tenders/%Y/%m/%d/',blank=True, null=True)
    due_date = models.DateField()
    time = models.TimeField()
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-timestamp", ]

    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)







