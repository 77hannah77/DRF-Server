from django.shortcuts import render
from django.http import Http404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,mixins

from .models import Post
from .serializers import PostSerializer

# APIView 이용

# class PostListCreateAPIView(APIView):
    
#     def get(self,request,formate=None):
#         posts=Post.objects.all()
#         serializer=PostSerializer(posts,many=True)
#         return Response(serializer.data)
    
#     def post(self,request,format=None):
#         serializer=PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class PostRetrieveUpdateDestoryAPIView(APIView):
#     def get_object(self,pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404
#     def get(self,request,pk,format=None):
#         post=self.get_object(pk)
#         serializer=PostSerializer(post)
#         return Response(serializer.data)
    
#     def put(self,request,pk,format=None):
#         post=self.get_object(pk)
#         serializer=PostSerializer(post,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk,format=None):
#         post=self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# GenericAPIView 와 Mixins 이용
class PostListCreateAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class PostRetrieveUpdateDestoryAPIView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
    
    
  