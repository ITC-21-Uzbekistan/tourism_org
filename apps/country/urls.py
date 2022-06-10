from django.urls import path
from .views import ListCountryViewForAdmin, RetrieveUpdateDestroyCountryViewForAdmin, ListCountryViewForAll, RetrieveCountryViewForAll

urlpatterns = [
    # for user
    path('', ListCountryViewForAll.as_view()),
    path('<int:pk>/', RetrieveCountryViewForAll),

    # for admin
    path('admin/', ListCountryViewForAdmin.as_view()),
    path('admin/<int:pk>/', RetrieveUpdateDestroyCountryViewForAdmin.as_view()),
]
