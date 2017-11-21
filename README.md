# 需要安装Flask-wtf，mysql-python
```
pip install Flask-wtf
pip install mysql-python
```
如果你是windows安装mysql-python非常的费事，因此你只需要安装
项目里的两个EXE即可先安装VCForPython27.msi

wtf = what's the fuck ???

引用
```
from wtforms import Form
```

建表语句
```
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `passwd` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8
```