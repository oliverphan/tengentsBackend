from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from . import eliza

therapist = eliza.eliza()



@api_view(http_method_names=['POST'])
def talk(request):
    msg = request.data.get("message")
    reply = therapist.respond(msg)
    return Response({"reply": reply},status=HTTP_200_OK)