from rest_framework import mixins, viewsets


class CreateListDestroyMixin(mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet,):

    pass
