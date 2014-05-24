First of all, you need have installed pip and virtualenv.
1. Create a new virtual environment ==> virtualenv <name env>
2. Install packages ==> pip install -r requirements.txt
3. Edit the settings.py file and set the default database ==> /lab/settings.py
4. Head back the root folder of the project and sync the database ==> python manage.py syncdb
5. To run test of code coverage ==> python manage.py test
6. To run web service, start the web server ==> python manage.py runserver

Primeiro de tudo, você precisa ter instalado pip e virtualenv.
1. Crie um novo virtual environment ==> virtualenv <name env>
2. Instale os pacotes ==> pip install -r requirements.txt
3. Edite o arquivo settings.py e defina o banco de dados padrão ==> /lab/settings.py
4. Volte a pasta raiz do projeto e sincronize o banco de dados ==> python manage.py syncdb
5. Para executar o teste de cobertura de código ==> python manage.py test
6. Para executar o web service, inicie o servidor web ==> python manage.py runserver