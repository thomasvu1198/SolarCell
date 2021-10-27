from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from datetime import datetime
# Create your views here.


class HomeView(TemplateView):
    template_name = 'Home.html'


class ConfigView(TemplateView):
    template_name = 'Config.html'


class DefaultCombineView(TemplateView):
    template_name = 'DefaultCombine.html'


class AutoCombineView(TemplateView):
    template_name = 'AutoCombine.html'


class MaintainView(TemplateView):
    template_name = 'Maintain.html'


# class DefaultSuperviseView(TemplateView):
#     template_name = 'DefaultSupervise.html'


class AutoCombineCalculateView(TemplateView):
    template_name = 'AutoCombineCalculate.html'


class DefaultCombineCaculateView(TemplateView):
    template_name = 'DefaultCombineCaculate.html'


class ManageView(TemplateView):
    template_name = 'Manage.html'
