## Introducción

Este proyecto es una aplicación web desarrollada en Django que permite gestionar un catálogo de productos como quesos, cervezas artesanales, promociones y gin artesanal. Incluye funcionalidades tanto para usuarios comunes como para administradores.

## Requisitos del Sistema

- Python 3.x
- Django 3.x o superior
- SQLite3 (por defecto)
- Navegador web moderno

Funcionalidades generales
Lista las principales funcionalidades del proyecto y cómo acceder a ellas.

-Inicio: Acceder a la página principal del proyecto.
URL: /

-Nosotros: Ver información sobre el emprendimiento
URL: /about/

-Editar Productos: (CRUD) Editar, agregar o borrar productos/categorias de productos presentes en la base de datos. Desde aca se puede modificar la base de datos solo si el LOGIN es una administrador. 
URL: /editar_productos/

-Productos: aca figuran las distintas categorias de productos a las cuales se puede acceder individualmente.
 -Quesos: pruducto/quesos.html
 -Cervezas Artesanales: pruducto/cervezas.html
 -Promociones: pruducto/promociones.html
 -Gin Artesanal: pruducto/gin.html

Funcionalidades de Administrador
El proyecto incluye una interfaz de administrador que permite gestionar los datos del sistema de forma sencilla. Tambien nos permite navegar como administrar por la pagina comunmente si usamos el login, y hacer cambios en los productos desde ahi, pero no de los usuarios

   Acceso al Administrador
   -URL de administración del proyecto: http://localhost:8000/admin/.
   -Ingresar credenciales de superusuario para acceder al panel de administración.

   Funcionalidades Disponibles
   -Productos y categorías: Permite administrar los productos y castegorías disponibles en el sistema
   -Usuarios: Permite gestionar los usuarios registrados en el sistema y ver su información (nombre, apellido, email, etc)
   
   Acceso al Panel de Administración
   -El panel de administración se puede acceder mediante la URL /admin/ del proyecto.

   Credenciales de Superusuario
   Las credenciales predeterminadas del superusuario son:

   -Usuario: admin
   -Contraseña: [123]

estructura del proyecto:

AlejoPardini/
├── manage.py
├── db.sqlite3
├── config/
│   ├── settings.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   └── views.py
│
├── core/
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── models.py
│   ├── __init__.py
│   ├── tests.py
│   ├── views.py
│   ├── forms.py
│   ├── migrations/
│   └── static/core
│   │      └── css/
│   │      │    ├── producto_styles.css
│   │      │    ├── styles.css
│   │      │    ├── titulo_styles.css
│   │      │    └── usuarios_styles.css
│   │      ├── assets
│   │      │    └── favicon.ico
│   │      ├── img
│   │      │    ├── cervezas.webp
│   │      │    ├── nosotros.png
│   │      │    ├── picada.png
│   │      │    ├── quesos.png
│   │      │    ├── tigre.png
│   │      │    └── tigreblanco.png
│   │      └── js
│   │           └── scripts.js
│   └── templates/core
│           ├── components
│           │    ├── card.html
│           │    ├── card2.html
│           │    ├── card3.html
│           │    ├── card4.html
│           │    ├── footer.html
│           │    ├── navbar.html
│           │    └── titulo1.html
│           ├── about.html
│           ├── base.html
│           ├── login.html
│           ├── logout.html
│           ├── producto.html
│           ├── register.html
│           └── index.html
├── producto/
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── models.py
│   ├── __init__.py
│   ├── tests.py
│   ├── views.py
│   ├── forms.py
│   ├── migrations/
│   └── templates/producto
│           ├── cervezas.html
│           ├── editar_producto.html
│           ├── gin.html
│           ├── producto_confirm_delete.html
│           ├── producto_detail.html
│           ├── producto_form.html
│           ├── producto_list.html
│           ├── productocategoria_confirm_delete.html
│           ├── productocategoria_detail.html
│           ├── productocategoria_form.html
│           ├── productocategoria_list.html
│           ├── productocategoria_update.html
│           ├── quesos.html
│           └── promociones.html
└── usuario/
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── urls.py
    ├── models.py
    ├── __init__.py
    ├── tests.py
    ├── views.py
    ├── forms.py
    └── templates/usuario
            ├── editar_perfil.html
            ├── perfil_actualizado.html
            └── index.html
    
