from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_1_0_3 = routers.DefaultRouter()
router_1_0_3.register('v1/posts', PostViewSet, basename='posts')
router_1_0_3.register('v1/groups', GroupViewSet, basename='groups')
router_1_0_3.register(
    r'^v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_1_0_3.register('v1/follow', FollowViewSet, basename='follows')
