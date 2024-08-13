from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from integration.services.pg_service import PgService
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def initiate(request):
    logger.debug("Rendering pgform.html template.")
    pg_service = PgService()
    enc_data = pg_service.request()
    return render(request, "pgform.html", {"enc_data": enc_data, "client_code": pg_service.client_code})

@csrf_exempt
def response(request):
    pg_service = PgService()
    response = request.POST['encResponse'].replace(" ", "+")
    dec_data = pg_service.res(response)
    return render(request, "response.html", {"dec_data": dec_data})


