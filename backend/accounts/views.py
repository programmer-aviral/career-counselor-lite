from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer, UserSerializer


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """
    POST /api/auth/register/

    Public endpoint.
    Creates a new user and immediately returns JWT tokens.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "user": UserSerializer(user).data,
                "tokens": {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                },
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(TokenObtainPairView):
    """
    POST /api/auth/login/

    Public endpoint.
    Authenticates the user and returns JWT access and refresh tokens.
    """

    permission_classes = [permissions.AllowAny]


class MeView(APIView):
    """
    GET /api/auth/me/

    Protected endpoint.
    Returns the currently authenticated user's information.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request) -> Response:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class LogoutView(APIView):
    """
    POST /api/auth/logout/

    Protected endpoint.
    Blacklists the supplied refresh token.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request) -> Response:
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {"detail": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            return Response(
                {"detail": "Invalid or expired token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"detail": "Successfully logged out."},
            status=status.HTTP_200_OK,
        )
