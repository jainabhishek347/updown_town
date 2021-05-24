python manage.py migrate
python manage.py makemigrations
#python manage.py migrate
python manage.py migrate --run-syncdb
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin_test', 'admin@example.com', 'pass123')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000