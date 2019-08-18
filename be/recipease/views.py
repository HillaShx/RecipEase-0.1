# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Recipe



# Create your views here.
def list_recipes(request):
  query = Recipe.objects.all()
  data = {"results": list(query.values())}
  return JsonResponse(data)

def list_filtered_recipes(request, search_query):
  query = Recipe.objects.all()
  query_list = [i.strip() for i in search_query.split(",")]
  exclusion_queries = [x[1:] for x in query_list if x[0] == "-"]
  inclusion_queries = [x for x in query_list if x[0] != "-"]
  for q in inclusion_queries:
    query = query.filter(ingredients__icontains=q)
  for q in exclusion_queries:
    query = query.exclude(ingredients__icontains=q)
  data = {"results": list(query.values())}
  return JsonResponse(data)