from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"message": "Login riuscito", "username": user.username})
        return Response({"error": "Credenziali non valide"}, status=400)

class UpdateFavoriteTeamView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        team_name = request.data.get("favorite_team")
        if not team_name:
            return Response({"error": "Nessuna squadra fornita"}, status=status.HTTP_400_BAD_REQUEST)
        request.user.favorite_team = team_name
        request.user.save()

        return Response({"message": "Squadra preferita aggiornata", "favorite_team": team_name})
    
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)