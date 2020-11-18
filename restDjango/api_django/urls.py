from django.urls import path
from .import views

urlpatterns = [
    path("", views.apiListView, name="apiView"),
    path("detail/<int:pk>/", views.apiDetailView, name="apiDetailView"),
    path("class/", views.apiClassListView.as_view(), name="apiClassView"),
    path("class/detail/<int:pk>/", views.apiClassDetailView.as_view(), name="apiClassDetailView"),
    path("generic/", views.apiGenericListView.as_view(), name="apiGenericView"),
    path("generic/detail/<int:pk>/", views.apiGenericDetailView.as_view(), name="apiGenericDetailView"),
    


]
