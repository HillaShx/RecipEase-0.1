# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.
def index(request):
  if request.method == "POST":
    query_list = request.POST["search_query"].replace(" ","").split(",")
    exclusion_queries = ""
    inclusion_queries = ""
    for query in query_list:
      if query[0] == "-":
        # THIS IS WHERE MY REGEX WILL GO
        # exclusion_queries += "" + query + "%'"
      else:
        pass
      context = {"results": None}
    # Recipe.objects.exclude(ingredients__in=[..exclusion_queries]).filter.raw("SELECT * FROM recipes WHERE ingredients LIKE '%" + inclusion_queries + "%'")
  return render(request, "index.html", context)


# def search(request):
#   query_list = request.POST["search_query"].replace(" ","").split(",")
#   for query in query_list:
#     if query[0] == "-":
#       pass
#     else:
#       pass
  
#   context = {"results": None}
#   return render(request, "index.html", context)