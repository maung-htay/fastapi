# model -> sqlalchemy
# scheme -> pydantic

# pip install "passlib[bcrypt]"

# pip install "python-jose[cryptography]"

# https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-joins/

# https://alembic.sqlalchemy.org/en/latest/

# for migration tool 
# pip install alembic
# alembic init alembic
# alembic revision -m "create post"
# alembic revision --autogenerate -m "auto generate"
# alembic revision --autogenerate -m "auto generate1
# alembic upgrade head  
# eg ->  op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False))

# Git 
# git hub issue
# https://qiita.com/takapon21/items/13f00cb2e48d8c1cc115

# heroku
# heroku --version
# heroku login
# heroku create --help
# heroku create fastapi-mghtay

# git remote
# git push heroku main
# heroku logs -t
# https://devcenter.heroku.com/articles/heroku-postgresql -> for .env file
# heroku addons:create heroku-postgresql:hobby-dev

# after that 
# heroku ps:restart
# heroku apps:info fastapi-mghtay

# heroku run "alembic upgrade head"

# set up project on ubuntu
sudo apt update & sudo apt upgrade -y
choose -> Install the maintance version
sudo apt install python3-pip
sudo pip install virtuallen

# Installation postgres
sudo apt install postgresql postgresql-contrib -y 
psql --version
sudo cat /etc/passwd
su - postgres 
psql -U postgres
\password postgres
exit

cd /etc/postgres/12/main
sudo vi postgres.conf
At ### Connection and Authentication
√ Insert listen_addresses='*'
:wq
sudo vi pg_hba.conf
Change => 
local all postgres peer -> local all postgres md5
local all all      pear -> local all all      md5
host all all 127.0.0.0/32 -> host all all 0.0.0.0/0 
at ipv6 -> ::/0 
systemctl restart postgresql
psql -U postgres

Creating user 
adduser mghtay
type password 
usermod -aG sudo mghtay
Enter with username -> ssh 
mkdir app
virtuallen venv
source /venv/bin/activate
mkdir src 
cd src 
git clone rep_git_path .
cd ..
activate venv again
pip install -r requirements.txt
# create .env file
paste data into .env file
set -o allexport; source /home/mghtay/.env; set +0 allexport
cd ~
ls -al
vi .profile
insert -> set -o allexport; source /home/mghtay/.env; set +0 allexport

do alembic
uvicorn --host 0.0.0.0 app.main:app

pip install gunicorn 
pip install httptools 
pip install uvtools 
pip install uvloop 
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000

check from other terminal 
ps -aef | grep -i gunicorn

With stystemctl start or restart 
cd /etc/systemd/system/
sudo vi api.service

-> Create api.service

[Unit]
Description=gunicorn instance to server api
After=network.target

[Service]
User=david
Group=www-data
WorkingDirectory=/home/david/mywebsite
Environment="PATH=venv_path/bin"
EnvironmentFile=/home/mghtay/.env
ExecStart=/home/david/mywebsite/venv/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000

[Install]
WantedBy=multi-user.target

###############
api.service -> api

systemctl deamon-reload
systemctl start api
systemctl status api 
systemctl restart api
sudo systemctl enable api

Nginx Section
sudo apt install nginx -y
systemctl start nginx
cd /etc/nginx/sites-availabel/
sudo vi default
insert -> in location
location / {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $http_host;
        proxy_set_header X-NginX-Proxy true;
        proxy_redirect off;
    }

systemctl restart nginx


For https
https://certbot.eff.org/
Geg cerbot insturction
Select Software and system

see => default Section
Step 6 is ok 

Firewall
sudo ufw status
-> inactive is ok
sudo ufw allow http
sudo ufw allow https 
sudo ufw allow ssh 
sudo ufw allow 5432
sudo ufw enable
sudo ufw status
if you want to delete -> sudo ufw delete allow http


# Docker 
postgress sql backup and restory 
https://stackoverflow.com/questions/24718706/backup-restore-a-dockerized-postgresql-database