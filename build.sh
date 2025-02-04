set -o errexit
pip install -r requirments.txt
python manage.py collectstatic --no-input
python manage.py migrate
if [[ $CREATESUPERUSER ]];
then 
python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
