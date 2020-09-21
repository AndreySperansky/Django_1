from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from .forms import ProductCategoryForm
# список объектов
from django.views.generic.list import ListView
# 1 объект
from django.views.generic.detail import DetailView
# создание, изменение, удаление
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin


def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', content)


def user_create(request):
    pass


def user_update(request, pk):
    pass


def user_delete(request, pk):
    pass


class CaptionMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['caption'] = 'Мой заголовок страницы'
        return context


class CategoryListView(ListView, CaptionMixin):
    model = ProductCategory
    template_name = 'adminapp/categories.html'
    paginate_by = 20
    context_object_name = 'categories'

    def get_queryset(self):
        categories_list = ProductCategory.objects.filter(name__contains='о')
        return categories_list


class CategoryDetailView(DetailView):
    model = ProductCategory
    template_name = 'adminapp/category.html'



def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.filter(is_active=True)

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)





def category_detail(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    return render(request, 'adminapp/category.html', {'category': category})


class CategoryCreateView(CreateView, CaptionMixin):
    model = ProductCategory
    template_name = 'adminapp/category_edit.html'
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'


def category_create(request):
    #  1 view обрабатывает 2 типа запроса
    #  get - ?
    # get - отрисовка страницы
    if request.method == 'POST':
        # заполнить форму данными
        form = ProductCategoryForm(request.POST, files=request.FILES)
        # заполнили правильно
        if form.is_valid():
            form.save()
            # надо сделать редирект
            return HttpResponseRedirect(reverse('admin:categories'))
        else:
            return render(request, 'adminapp/category_edit.html', {'form': form})
    else:
        # get
        form = ProductCategoryForm()
        return render(request, 'adminapp/category_edit.html', {'form': form})


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_edit.html'
    success_url = reverse_lazy('admin:categories')
    form_class = ProductCategoryForm


def category_update(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        # заполнить форму данными
        form = ProductCategoryForm(request.POST, files=request.FILES, instance=category)
        # заполнили правильно
        if form.is_valid():
            form.save()
            # надо сделать редирект
            return HttpResponseRedirect(reverse('admin:categories'))
        else:
            return render(request, 'adminapp/category_edit.html', {'form': form})
    else:
        form = ProductCategoryForm(instance=category)
        return render(request, 'adminapp/category_edit.html', {'form': form})


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete_confirm.html'
    success_url = reverse_lazy('admin:categories')


def category_delete(request, pk):
    # удаление гет запросом - не очень хорошо
    # уязвимость которую трудно экслуатировать
    # category = get_object_or_404(ProductCategory, pk=pk)
    # category.delete()
    # return HttpResponseRedirect(reverse('admin:categories'))
    # post запрос
    # if request.method == 'POST':
    #     category = get_object_or_404(ProductCategory, pk=pk)
    #     category.delete()
    #     return HttpResponseRedirect(reverse('admin:categories'))
    # else:
    #     raise Http404
    # удаление с подтверждением
    # category = get_object_or_404(ProductCategory, pk=pk)
    # if request.method == 'POST':
    #     category.delete()
    #     return HttpResponseRedirect(reverse('admin:categories'))
    # else:
    #     # рисуем страницу с подтверждением
    #     return render(request, 'adminapp/category_delete_confirm.html', {'category': category})
    # удаление с подтверждением без удаления из базы данных
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))
    else:
        # рисуем страницу с подтверждением
        return render(request, 'adminapp/category_delete_confirm.html', {'category': category})


def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


def product_create(request, pk):
    pass


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass
