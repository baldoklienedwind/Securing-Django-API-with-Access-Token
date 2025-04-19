from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
import logging

logger = logging.getLogger(__name__)

class SecureHelloView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logger.info(f"User: {request.user.username}")
        return Response({"message": f"Hello, {request.user.username}!"})
