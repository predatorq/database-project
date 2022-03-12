# database-project

## 运行指令

```shell
python manage.py runserver
```

## 项目介绍

构建一个web程序，实现对图书借阅数据库系统JY的图书表的增删改查。

本项目使用SQL server + Django构建。

在目录下使用代码创建项目：

```powershell
django-admin startproject database
```

这样就会生成目录如下所示：

```python
database/
    manage.py
    database/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

这些目录和文件的用处为：

- 最外层的 `database/` 根目录是项目的容器
- `manage.py`: 一个让你用各种方式管理 Django 项目的命令行工具。
- 里面一层的 `database/` 目录包含你的项目，它是一个纯 Python 包。
- `database/__init__.py`：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python 初学者，阅读官方文档中的 [更多关于包的知识](https://docs.python.org/3/tutorial/modules.html#tut-packages "(在 Python v3.10)")。
- `database/settings.py`：Django 项目的配置文件。
- `database/urls.py`：Django 项目的 URL 声明，就像你网站的“目录”。
- `database/asgi.py`：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口。
- `database/wsgi.py`：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。

然后使用命令创建books应用

```powershell
python manage.py startapp books
```

这样会创建一个books目录，里面的目如下所示：

```powershell
books/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

创建主视图，更改views.py，在其中新建函数index

```python
def index(request):
    return render(request, "index.html")
```

并在urls.py中加入：

```python
urlpatterns = [
    path('', views.index),
]
```

index书写方式如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="{% url 'check' %}" method="post">
    {% csrf_token %}
    欢迎访问JY数据库，您想要做什么：<br />
    <input name="action" id="add" type="radio" value="add" />
    <label for="add">增加项目</label>
    <input name="action" id="delete" type="radio" value="delete" />
    <label for="delete">删除项目</label>
    <input name="action" id="change" type="radio" value="change" />
    <label for="change">更改项目</label>
    <input name="action" id="check" type="radio" value="check" />
    <label for="check">查询项目</label></br>
    <input type="submit" value="提交" />
</form>
<h1>{{ hello }}</h1>
</body>
</html>
```

因为是单人项目，就没有对网页进行美化，只是使用了基础的html语言，而没有使用CSS更改style，界面显示实例在报告后段。

接下来设置动作，在主页选择项目并按下提交后，应当跳转到相应页面，在urlpatterns中添加：

```python
path('reg/', views.reg, name='check'),
```

在view中添加函数：

```python
def reg(request):
    if request.method == 'POST':
        action=request.POST.get('action')
        if action == "add":
            return HttpResponseRedirect("/add")
        if action == "delete":
            return HttpResponseRedirect("/delete")
        if action == "change":
            return HttpResponseRedirect("/change")
        if action == "check":
            return HttpResponseRedirect("/check")
    return render(request,'index.html')
```

调取index中action的值来判断，进行页面跳转。

跳转后即进行数据库的增删改查。

连接设置存放于settings中，对应代码如下：

```python
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "JY",
        "USER": "temp",
        "PASSWORD": "temp",
        "HOST": "localhost",
        "PORT": "53535",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",
                    },
    },
}
```

ms sql有对应的插件可以支持django，设置较为容易。数据库样式定义如下：

```python
class Book(models.Model):
    book_id = models.CharField(primary_key=True, max_length=8)
    book_name = models.CharField(max_length=50)
    book_isbn = models.CharField(max_length=17)
    book_author = models.CharField(max_length=10)
    book_publisher = models.CharField(max_length=50)
    book_price = models.DecimalField(max_digits=19, decimal_places=4)
    interview_times = models.SmallIntegerField()

    class Meta:
        db_table = 'book'
```

经过如上设置即可访问数据库了。下面再依次设置add，delete，change，check的函数和html。

以上几个页面url如下：

```python
urlpatterns = [
    path('', views.index),
    path('reg/', views.reg, name='check'),
    path('add/', views.add),
    path('delete/', views.delete),
    path('change/', views.change),
    path('check/', views.check),
]
```

设置完即可使用以下命令开启本地http服务：

```powershell
python manage.py runserver
```
