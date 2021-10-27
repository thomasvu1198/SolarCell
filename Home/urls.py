from django.urls import path
from .views import *
urlpatterns = [
    path('Manage', ManageView.as_view(), name='Manage'),
    # path('Supervise', DefaultSuperviseView.as_view(), name='Supervise'),
    path('Default-Combine-Caculate', DefaultCombineCaculateView.as_view(),
         name='DefaultCombineCaculate'),
    path('Auto-Combine-Calculate', AutoCombineCalculateView.as_view(),
         name='AutoCombineCalculate'),
    path('Maintain', MaintainView.as_view(), name='Maintain'),
    path('AutoCombine', AutoCombineView.as_view(), name='AutoCombine'),
    path('DefaultCombine', DefaultCombineView.as_view(), name='DefaultCombine'),
    path('Config', ConfigView.as_view(), name='Config'),
    path('', HomeView.as_view(), name='Home'),
]
