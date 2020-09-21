from django.shortcuts import render


def add_my_var(context):
    context['my_var'] = 'Общая переменная1'


def add_menu(context):
    context['menu'] = [
        {'name': 'главная', 'href': '/'},
        {'name': 'продукты', 'href': '/product_list'},
        {'name': 'контакты', 'href': '/contact'}
    ]
    # context['menu'] = [
    #     ('главная', '/'),
    #     ('продукты', '/'),
    #     ('контакты', '/')
    # ]


def main(request):
    title = 'Мои стулья'
    # title = title.upper()
    context = {'caption': title, 'sub': 'What?'}
    add_my_var(context)
    add_menu(context)
    return render(request, 'mainapp/index.html', context)


def products(request):
    product_list = ['стул', 'стол', 'диван']
    context = {'products': product_list}
    add_my_var(context)
    add_menu(context)
    return render(request, 'mainapp/products.html', context)


def contact(request):
    video_href = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xhS6Khb5Dzw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>'
    context = {'video_href': video_href}
    add_menu(context)
    return render(request, 'mainapp/contact.html', context)
