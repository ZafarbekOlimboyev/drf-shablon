from rest_framework.generics import CreateAPIView

from users.serializers import UserSerializer


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
