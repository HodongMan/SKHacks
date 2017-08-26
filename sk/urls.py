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
    url(r'^api/professor/$',
        views.ProfessorList.as_view(),
        name=views.ProfessorList.name
    ),
    url(r'^api/professor/(?P<pk>[0-9]+)/$',
        views.ProfessorDetail.as_view(),
        name=views.ProfessorDetail.name
    ),
    url(r'^api/chapter/$',
        views.ChapterList.as_view(),
        name=views.ChapterList.name
    ),
    url(r'^api/chapter/(?P<pk>[0-9]+)/$',
        views.ChapterDetail.as_view(),
        name=views.ChapterDetail.name
    ),
    url(r'^api/attendence/$',
        views.AttendenceList.as_view(),
        name=views.AttendenceList.name
    ),
    url(r'^api/attendence/(?P<pk>[0-9]+)/$',
        views.AttendenceDetail.as_view(),
        name=views.AttendenceDetail.name
    ),
]
