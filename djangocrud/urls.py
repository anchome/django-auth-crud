"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    ESPAÑOL
La lista `urlpatterns` enruta URLs a vistas. Para más información, consulte:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Ejemplos:
Vistas de funciones
    1. Añade una importación: from mi_app import vistas
    2. Añade una URL a urlpatterns: path('', views.home, name='home')
Vistas basadas en clases
    1. Añade una importación: from otra_app.vistas import Home
    2. Añadir una URL a urlpatterns: path('', Home.as_view(), name='home')
Incluir otra URLconf
    1. Importar la función include(): from django.urls import include, path
    2. Añade una URL a urlpatterns: path('blog/', include('blog.urls'))


"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('tasks/create_task/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete',
         views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('signin/', views.signin, name='signin'),
]
