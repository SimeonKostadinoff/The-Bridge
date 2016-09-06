from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'organisations/$', views.OrganisationListAPIView.as_view(), name="organisations_api"),
    url(r'organisations/currentUser/$', views.OrganisationCurrUserListAPIView.as_view(), name="organisations_curr_user_api"),
    url(r'posts/$', views.PostListAPIView.as_view(), name="posts_list_api"),
    url(r'posts/create/$', views.PostCreateAPIView.as_view(), name="posts_create_api"),
    url(r'comments/$', views.CommentListAPIView.as_view(), name="comments_list_api"),
    url(r'comments/create/$', views.CommentCreateAPIView.as_view(), name="comments_create_api"),
]