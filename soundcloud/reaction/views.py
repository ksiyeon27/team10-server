from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from set.models import Set
from track.models import Track
from user.models import User
from reaction.models import Like, Repost
from .serializers import LikeService, RepostService
from user.serializers import SimpleUserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view


class BaseReactionView(GenericAPIView):

    serializer_class = None
    queryset = None
    lookup_field = 'id'
    lookup_url_kwarg = None

    def get_serializer_context(self):
        context = super(BaseReactionView, self).get_serializer_context()
        context['target'] = self.get_object()

        return context

    def post(self, request, *args, **kwargs):
        service = self.get_serializer()
        status, data = service.create()

        return Response(status=status, data=data)

    def delete(self, request, *args, **kwargs):
        service = self.get_serializer()
        status, data = service.delete()

        return Response(status=status, data=data)


class LikeTrackView(BaseReactionView):

    serializer_class = LikeService
    queryset = Track.objects.all()
    lookup_url_kwarg = 'track_id'


class LikeSetView(BaseReactionView):

    serializer_class = LikeService
    queryset = Set.objects.all()
    lookup_url_kwarg = 'set_id'


class RepostTrackView(BaseReactionView):

    serializer_class = RepostService
    queryset = Track.objects.all()
    lookup_url_kwarg = 'track_id'


class RepostSetView(BaseReactionView):

    serializer_class = RepostService
    queryset = Set.objects.all()
    lookup_url_kwarg = 'set_id'
