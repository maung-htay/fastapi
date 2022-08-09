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
