from django.conf.urls import url
from sk import views

urlpatterns = [

    url(r'^api/student/$',
        views.StudentList.as_view(),
        name=views.StudentList.name
    ),
    url(r'^api/student/(?P<pk>[0-9]+)/$',
        views.StudentDetail.as_view(),
        name=views.StudentDetail.name
    ),
    url(r'^api/lecture/$',
        views.LectureList.as_view(),
        name=views.LectureList.name
    ),
    url(r'^api/lecture/(?P<pk>[0-9]+)/$',
        views.LectureDetail.as_view(),
        name=views.LectureDetail.name
    ),
]
