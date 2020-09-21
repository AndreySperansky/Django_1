from authapp.models import ShopUser

super_user = ShopUser.objects.create_superuser( 'django' ,
'django@geekshop.local' , 'geekbrains' , age= 33 )

