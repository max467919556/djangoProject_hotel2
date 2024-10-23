from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item

# ListView для отображения списка объектов
class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'

# DetailView для отображения деталей одного объекта
class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'

# CreateView для создания нового объекта
class ItemCreateView(CreateView):
    model = Item
    template_name = 'item_form.html'
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('item-list')

# UpdateView для обновления существующего объекта
class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'item_form.html'
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('item-list')

# DeleteView для удаления объекта с подтверждением
class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('item-list')
