from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'award', views.AwardViewSet)
router.register(r'lesson', views.LessonViewSet)
router.register(r'quiz', views.QuizViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'subject', views.SubjectViewSet)
router.register(r'subjectCategory', views.SubjectCategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]