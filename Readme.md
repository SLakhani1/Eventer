1. Creating Virtual Environment

sudo apt-get install python3-venv
python3 -m venv veventer

2. Starting the Virtual environemnt

source veventer/bin/activate

3. Install Django 

python -m pip install Django

4. Install Postgres

sudo apt-get install postgresql postgresql-contrib
pip install psycopg2

5. Setting up Postgres

sudo -u postgres psql
	ALTER USER postgres PASSWORD 'myPassword';

6. Installing psycopg2

sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
pip install psycopg2

7. Installing allauth

pip install django-allauth

8. pip install google-api-python-client
pip install oauth2client


9. Inside templates/eventerapp folder

npm install -g @vue/cli
npm install
npm run serve