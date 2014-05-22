First of all, you need pip and virtualenv.
1. Create a new env > virtualenv <name env>
2. Install packages > install -r requirements.txt
3. Config database > /lab/settings.py
4. Sync the database > go back to first lab folder, run it python manage.py syncdb
5. Start the server > python manage.py runserver