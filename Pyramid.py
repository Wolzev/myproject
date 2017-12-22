from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from jinja2 import FileSystemLoader,Environment
import os
from pyramid.response import Response

assets =[
    'app.js',
    'react.js',
    'leaflet.js',
    'D3.js',
    'moment.js',
    'math.js',
    'main.css',
    'bootstrap.css',
    'normalize.css',
    ]

css = []
js = []

#Распределяем элементы массива assets в соответситвии с расширением
for item in assets:
    (shortname, extension) = os.path.splitext(item)
    if extension == '.css':
        css.append(item)
    elif extension == '.js':
        js.append(item)

def index(request):
    env = Environment(loader=FileSystemLoader('.'))  
    result = env.get_template('/index.html').render({'css1': css, 'js1': js}) 
    return Response(result)

def aboutme(request):
    env = Environment(loader=FileSystemLoader('.'))
    result = env.get_template('aboutme/aboutme.html').render({'css1': css, 'js1': js})
    return Response(result)

if __name__ == '__main__':
    configurator = Configurator()
    configurator.add_route('aboutme', '/aboutme/aboutme.html')
    configurator.add_view(aboutme, route_name='aboutme')
    configurator.add_route('index', '/index.html')
    configurator.add_view(index, route_name='index')
    app = configurator.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
    
_________________________________________
После запуска программы в браузере по адресу http://localhost:8000/index.html будет выведена строка "Index"
Код страницы будет выглядеть следующим образом

<!DOCTYPE html>
<html lang="en">
<head>
    
    
    <link rel="stylesheet" href="/_static/main.css"/>
    
    <link rel="stylesheet" href="/_static/bootstrap.css"/>
    
    <link rel="stylesheet" href="/_static/normalize.css"/>
    

</head>
<body>
    <div id="content">
    <h1>Index</h1>
    <p class="important">
    
         <script src="/_static/app.js></script>
    
         <script src="/_static/react.js></script>
    
         <script src="/_static/leaflet.js></script>
    
         <script src="/_static/D3.js></script>
    
         <script src="/_static/moment.js></script>
    
         <script src="/_static/math.js></script>
    
    </p>
</div>
</body>
</html>
