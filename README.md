# python_api

> - python 2.7
> - pymysql 0.8.0
> - Flask 0.12.2
> - flask_restful 0.3.6
> - flask_sqlalchemy 2.3

# Usage

* first import `pytest.sql` to your database
* install libs
* then run the server

~~~
. venv/bin/activate
pip install -r requirements
python index.py
~~~

# Api

~~~
http://localhost:5000/user/reg?username=abc&password=123456
http://localhost:5000/user/login?username= abc&password=123456
~~~

