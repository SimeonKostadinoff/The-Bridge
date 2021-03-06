from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from rest_framework import generics, permissions, filters, views
from rest_framework.response import Response
from organisation import models as organisation_models
from posts import models as posts_models
from . import serializers

##########
# PERMISSIONS are not added when dev
##########

class UserListAPIView(generics.ListAPIView):
    '''List all users'''
    # permission_classes = (permissions.IsAdminUser,) # gives permissions only to Admin user to view the API view
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class OrganisationListAPIView(generics.ListAPIView):
    '''List all organisations'''
    # permission_classes = (permissions.IsAdminUser,) # gives permissions only to Admin user to view the API view
    queryset = organisation_models.Organisation.objects.all()
    serializer_class = serializers.OrganisationSerializer

    # filter organisations based on search_fields
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description', 'category', 'locations',)

class OrganisationRetrieveAPIView(generics.RetrieveAPIView):
    '''Retrive a particular organisation'''
    # permission_classes = (permissions.IsAdminUser,) # gives permissions only to Admin user to view the API view
    queryset = organisation_models.Organisation.objects.all()
    serializer_class = serializers.OrganisationSerializer

class OrganisationCurrUserListAPIView(generics.ListAPIView):
    '''List current user's organisations'''
    # permission_classes = (permissions.IsAdminUser,) # gives permissions only to Admin user to view the API view
    serializer_class = serializers.OrganisationSerializer
    # modify the queryset in order to list only organsiations from the user
    def get_queryset(self):
        queryset_list = organisation_models.Organisation.objects.filter(host=self.request.user)
        return queryset_list

class OrganisationIsCurrUserAPIView(views.APIView):
    '''Customized view to check if the particular organisation is hosted by the current user'''
    # permission_classes = []
    # modify get method
    def get(self, request, *args, **kwargs):
        org = organisation_models.Organisation.objects.filter(pk=self.kwargs['pk'], host=self.request.user)
        if len(org) == 1:
            return Response({"success": True}) # return True if the current user is the host
        else:
            return Response({"success": False}) # return False if the current user is not the host

class OrganisationUpdateBookmarkAPIView(generics.UpdateAPIView):
    '''Retrive a particular organisation'''
    permission_classes = [permissions.IsAuthenticated] # gives permissions only to Admin user to view the API view
    queryset = organisation_models.Organisation.objects.all()
    serializer_class = serializers.OrganisationSerializer

    # update organisation bookmark
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user in instance.bookmark.all():
            instance.bookmark.remove(request.user) # remove relation with user if exists
        else:
            instance.bookmark.add(request.user) # add relation with user 
        instance.save()
        
        data = {}
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        # return empty serialized data
        return Response(serializer.validated_data)

class OrganisationCurrUserBookmarkAPIView(generics.ListAPIView):
    '''List current user's organisations bookmark'''
    # permission_classes = (permissions.IsAdminUser,) # gives permissions only to Admin user to view the API view
    serializer_class = serializers.OrganisationSerializer
    # modify the queryset in order to list only organsiations from the user
    def get_queryset(self):
        queryset_list = organisation_models.Organisation.objects.filter(bookmark__in=[self.request.user])
        return queryset_list

class ReviewListAPIView(generics.ListAPIView):
    '''List all reviews'''
    # permission_classes = (permissions.IsAdminUser,) # gives permissions only to Admin user to view the API view
    serializer_class = serializers.ReviewListSerializer
    # modify the queryset in order to list reviews only for the particular organisation
    def get_queryset(self):
        org_obj = get_object_or_404(organisation_models.Organisation, pk=self.kwargs['pk'])
        queryset_list = organisation_models.Review.objects.filter(organisation=org_obj)
        return queryset_list

class ReviewRetrieveAPIView(generics.RetrieveAPIView):
    '''Retrive a particular review'''
    queryset = organisation_models.Review.objects.all()
    serializer_class = serializers.ReviewListSerializer
    #permission_classes = [permissions.IsOwnerOrReadOnly]

class ReviewCreateAPIView(generics.CreateAPIView):
    '''Create review'''
    queryset = organisation_models.Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    # modify serializer class to return the method for creating a review
    def get_serializer_class(self):
        organisation_id = self.kwargs['pk']
        return serializers.create_review_serializer(organisation_id=organisation_id, request=self.request)

class PostListAPIView(generics.ListAPIView):
    '''List all posts'''
    queryset = posts_models.Post.objects.all()
    serializer_class = serializers.PostListSerializer
    # modify queryset when '?org_id=...' is passed to return posts oly for the particular organisation
    def get_queryset(self):
        queryset_list = posts_models.Post.objects.all()
        organisation_id = self.request.GET.get('org_id') # get the 'org_id' passed as get request
        if organisation_id :
            org_obj = organisation_models.Organisation.objects.get(pk=organisation_id)
            queryset_list = posts_models.Post.objects.filter(organisation=org_obj)

        return queryset_list

class PostRetrieveAPIView(generics.RetrieveAPIView):
    '''Retrive a particular post'''
    queryset = posts_models.Post.objects.all()
    serializer_class = serializers.PostListSerializer
    #permission_classes = [permissions.IsOwnerOrReadOnly]

class PostCreateAPIView(generics.CreateAPIView):
    '''Create post'''
    queryset = posts_models.Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    # modify serializer class to return the method for creating a post
    def get_serializer_class(self):
        organisation_id = self.request.GET.get('org_id') # get the 'org_id' passed as get request
        return serializers.create_post_serializer(organisation_id=organisation_id, request=self.request)

class CommentListAPIView(generics.ListAPIView):
    '''List all posts'''
    queryset = posts_models.Comment.objects.all()
    serializer_class = serializers.CommentListSerializer
    #permission_classes = [permissions.IsOwnerOrReadOnly]
    # modify queryset when '?post=...' is passed to return comments only for the particular organisation
    def get_queryset(self):
        queryset_list = posts_models.Comment.objects.all()
        post = self.request.GET.get('post') # get the 'post' passed as get request
        if post is not None:
            queryset_list = queryset_list.filter(post_id=post)

        return queryset_list

class CommentRetrieveAPIView(generics.RetrieveAPIView):
    '''Retrive a particular comment'''
    queryset = posts_models.Comment.objects.all()
    serializer_class = serializers.CommentListSerializer
    #permission_classes = [permissions.IsOwnerOrReadOnly]


class CommentCreateAPIView(generics.CreateAPIView):
    '''Create comment'''
    queryset = posts_models.Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    # modify serializer class to return the method for creating a comment using passed 'type', 'org_id', 'post_id' values as get request
    def get_serializer_class(self):
        model_type = self.request.GET.get('type')
        organisation_id = self.request.GET.get('org_id')
        post_id = self.request.GET.get('post_id')
        return serializers.create_comment_serializer(
            model_type=model_type,
            organisation_id=organisation_id, 
            post_id=post_id,
            request=self.request)

