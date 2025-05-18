from django.urls import path
from .views import general, gallery, about, news, vacancy, tenders

app_name = 'general'

urlpatterns = [
    path('',general.home, name="home"),
    path('contact/',general.contact, name="contact"),
    path('team/<str:category>/',general.teams, name="teams"),
    path('downloads/<str:category>/',general.downloads, name="downloads"),
    path('our-gallery-folders/',gallery.folders, name='folders'),
    path('folders/images/<slug:slug>/',gallery.folders_images, name='folders_images'),
    path('media/',gallery.media, name='media'),
    path('division/<slug:slug>/',about.division_details, name='division_details'),
    path('background-mandate/',about.background_or_mandate, name='background_or_mandate'),
    path('news/',news.news, name='news'),
    path('news-details/<slug:slug>/',news.news_details, name='news_details'),
    path('l/<slug:slug>/',general.legislation, name='legislation'),
    path('vacancies/',vacancy.vacancies, name='vacancies'),
    path('vacancy/<int:id>/<slug:slug>/',vacancy.vacancy_details, name='vacancy_details'),
    path('tenders/',tenders.tenders, name='tenders'),

]
