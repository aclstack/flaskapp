# 需要安装Flask-wtf，mysql-python
```
pip install Flask-wtf
pip install mysql-python
pip install Flask-SQLAlchemy==2.1
pip install flask-restful
pip install Flask-Migrate
pip install Flask-Script
python migrater.py db init 数据库初始化并保留版本
python migrater.py db migrate 更新数据库字段
```
如果你是windows安装mysql-python非常的费事，因此你只需要安装
项目里的两个EXE即可先安装VCForPython27.msi
最新版本的Flask-SQLAlchemy存在bug因此选用2.1

wtf = what's the fuck ???

引用
```
from wtforms import Form
```
