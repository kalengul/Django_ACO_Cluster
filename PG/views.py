from rest_framework import generics
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .serializers import *


class AllAPIList(generics.ListCreateAPIView):
    queryset = ParametricGraph.objects.select_related('user').all()
    serializer_class = AllSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PGAPIList(generics.ListCreateAPIView):
    queryset = ParametricGraph.objects.all()
    serializer_class = PGSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PGAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = ParametricGraph.objects.all()
    serializer_class = PGSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PGAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = ParametricGraph.objects.all()
    serializer_class = PGSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class LayerAPIList(generics.ListCreateAPIView):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class LayerAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class LayerAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class NodeAPIList(generics.ListCreateAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class NodeAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class NodeAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (IsOwnerOrReadOnly, )

