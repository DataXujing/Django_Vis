## 美迪康AI项目可视化


### 1.项目介绍

整个项目主要包含四部分:

+ index页面:主页包含Medicon AI Lab的介绍

+ 项目列表页： 以炫酷的table形式展示目前Medicon AI Lab相关的AI项目

+ 项目详情页： 该页面主要包含三个tab页面，第一个tab页面命名为：项目介绍，主要包括项目名称，合作单位，项目介绍，数据介绍，评价指标介绍；第二个tab页面命名为：项目进展，主要包括： 排行榜（以下拉列表选取A,B,C榜单，每个榜单包括，排名，提交人，分数，提交时间）、评价指标可视化，以可视化的形式展示得分的折线图等；第三个tab命名为：DEMO, 主要展示了炫酷的产品效果，比如以视频片段或识别图像为展示效果。

+ 管理界面，主要是后台管理，以富文本编辑器的形式或markdown的形式管理提交的项目

+ 数据库方面我们采用sqlite3,使用Django==2.1.5 Web框架开发

### 2.完成主要是借助空余时间和下班后回家的时间

1.新建项目

django-admin startproject MedAIIndex

项目中的文件结构：

```
settings.py: 这个是整个项目的配置文件
urls.py:     路由的总控制文件
wsgi.py:     和web服务(如apache,wsgi)配合使用的配置文件

manage.py   django项目的管理文件,很多命令号的操作在这里
```

settting中的结构：

```
setting:

DATABASES: 数据库的设置，默认sqlite3数据库没有用户名和密码
STATIC_URL:静态资源文件路径
TEMPLATES: 模板页面文件路径,html
MIDDLEWARE_CLASSES:中间件，添加功能
INSTALLED_APPS: 项目的模块
ALLOWED_HOSTS: 访问服务的IP地址

时区及语言
	LANGUAGE_CODE = 'zh-Hans'
	TIME_ZONE = 'Asia/Shanghai'
```

新建APP

```
python manage.py startapp AiDes
```



AiDes的App的组成

```
admin.py:把数据库注册到这个文件后，可以在admin界面下使用
models.py:数据库文件，ORM映射关系，数据库创建语句
views.py:具体功能文件，是一个又一个的函数组成
urls.py:APP下的路由控制文件

```

开启一个APP之后，要记得把他在setting.py下写入到INSTALLED_APPS中



```
1: python manage.py makemigrations 根据你对数据库的修改，策略迁移文件
2: python manage.py migrate 生成对应的SQL语句
3: python manage.py createsuperuser
```

