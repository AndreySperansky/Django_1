from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from .forms import ProductCategoryForm


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
