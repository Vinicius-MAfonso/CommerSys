set -o errexit

echo "Iniciando script de inicialização..."

echo "Aplicando migrações (python manage.py migrate)..."
python manage.py migrate

echo "Coletando estáticos (python manage.py collectstatic)..."
python manage.py collectstatic --no-input

echo "Iniciando Gunicorn..."
gunicorn commersys.wsgi:application