from django.contrib.auth.models import User

if User.objects.count() == 0:
    admin = User.objects.create_user('username', 'email@example.com', 'password')
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()