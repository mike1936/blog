from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Post, Category, Tag, Comment
from .serializers import (
    PostListSerializer, PostDetailSerializer, CategorySerializer,
    TagSerializer, CommentSerializer
)


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'tags']
    search_fields = ['title', 'content', 'excerpt']
    ordering_fields = ['published_at', 'title']
    ordering = ['-published_at']

    def get_queryset(self):
        return Post.objects.filter(status=Post.PUBLISHED).select_related(
            'author', 'category'
        ).prefetch_related('tags')


class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Post.objects.filter(status=Post.PUBLISHED).select_related(
            'author', 'category'
        ).prefetch_related('tags', 'comments')


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_slug = self.kwargs.get('post_slug')
        post = Post.objects.get(slug=post_slug, status=Post.PUBLISHED)
        serializer.save(post=post)


@api_view(['GET'])
def blog_stats(request):
    """API endpoint for blog statistics"""
    stats = {
        'total_posts': Post.objects.filter(status=Post.PUBLISHED).count(),
        'total_categories': Category.objects.count(),
        'total_tags': Tag.objects.count(),
        'recent_posts': PostListSerializer(
            Post.objects.filter(status=Post.PUBLISHED)[:5], many=True
        ).data
    }
    return Response(stats)
