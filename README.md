# flareg
 The member registration website using Flask, which is a Python module.

 # requirements
 
 - OS: Ubuntu 18.04 (WSL)
 - browser: Google Chrome 88.0.4324.150
 - language: Python 3.7.9
    - Flask 1.1.2
    - Jinja2 2.11.3
    - SQLAlchemy 1.3.23

 # usage
 
 ### setup db

 Python対話コンソールを起動して、データベースファイルを作成する。（初回のみ）
 ```sh
 $ cd ./flareg
 $ python
 ```

 ```python
 >>> from models.database import init_db
 >>> init_db()
 ```

 ### run app

 ```sh
 $ export FLASK_APP="app.py"
 $ flask run
 ```

 起動したら、http://localhost:5000/ へブラウザからアクセスする。
