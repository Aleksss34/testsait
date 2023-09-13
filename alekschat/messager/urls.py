from django.urls import path, register_converter
from . import views
#определение пути сайта
from . import converters
register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [

    path('', views.index, name='home'),
    path('profile/', views.profile),
    path('categories/<int:cat_id>/', views.categories_int, name='category'),
    path('categories/<slug:cat_slug>/', views.categories_slug),
    path("archive/<year4:year>/", views.archive_year),
    path('archive/', views.archive),
    path('anketa/', views.anketa),
    path('registration/', views.registration)

]