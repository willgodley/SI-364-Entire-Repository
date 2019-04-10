from django.views import View
from django.views import generic
from django.shortcuts import render

# Create your views here.

from unesco.models import Site, Iso, Region, States, Category

class SiteListView(generic.ListView):
    model = Site

class SiteDetailView(generic.DetailView):
    model = Site

class IsoListView(generic.ListView):
    model = Iso

class IsoDetailView(generic.DetailView):
    model = Iso

class RegionListView(generic.ListView):
    model = Region

class RegionDetailView(generic.DetailView):
    model = Region

class StatesListView(generic.ListView):
    model = States

class StatesDetailView(generic.DetailView):
    model = States

class CategoryListView(generic.ListView):
    model = Category

class CategoryDetailView(generic.DetailView):
    model = Category
