from rest_framework.response import Response
from rest_framework.decorators import api_view
import boto3
import json
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from PIL import Image
import requests
from io import BytesIO
import io

from . import eliza

therapist = eliza.eliza()


@api_view(http_method_names=['POST'])
def talk(request):
    msg = request.data.get("message")
    reply = therapist.respond(msg)

    #analysis
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    r = comprehend.detect_sentiment(Text=msg, LanguageCode='en')

    return Response({"reply": reply, "Sentiment" : r["Sentiment"]},status=HTTP_200_OK)

@api_view(http_method_names=['POST'])
def picture_label(request):
    url = request.data.get("image")
    client=boto3.client('rekognition')

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()

    client=boto3.client('rekognition')
    
    
    response = client.detect_labels(Image={'Bytes': imgByteArr} , MaxLabels=5)
           
    retval = [label['Name']  for label in response['Labels']]
    return Response(retval,status=HTTP_200_OK)

