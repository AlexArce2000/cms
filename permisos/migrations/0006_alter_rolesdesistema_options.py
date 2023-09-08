# Generated by Django 4.2.4 on 2023-09-08 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0005_alter_rolesdesistema_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rolesdesistema',
            options={'permissions': [('_acceder_al_sistema', 'Acceder al Sistema'), ('_administrar_rol', 'Administrar Rol'), ('_crear_rol', 'Crear Rol'), ('_modificar_rol', 'Modificar Rol'), ('_eliminar_rol', 'Eliminar Rol'), ('_editar_perfil', 'Editar Perfil'), ('_administrar_categoria', 'Administrar Categoria'), ('_crear_categoria', 'Crear Categoria'), ('_editar_categoria', 'Editar Categoria'), ('_eliminar_categoria', 'Eliminar Categoria'), ('_configurar_sitio_web', 'Configurar Sitio Web'), ('_administrar_contenido', 'Administrar Contenido'), ('_crear_contenido', 'Crear Contenido'), ('_editar_contenido', 'Editar Contenido'), ('_eliminar_contenido', 'Eliminar Contenido'), ('_publicar_contenido', 'Publicar Contenido'), ('_asignar_categoria_a_contenido', 'Asignar Categoria a Contenido'), ('_ver_estadistica_de_contenido', 'Ver estadistica del contenido'), ('_ver_numero_de_visualizaciones', 'Ver Numero de visualizaciones'), ('_ver_numero_de_likes', 'Ver numero de likes'), ('_ver_numero_de_dislikes', 'Ver numero de dislikes'), ('_comentar_contenido', 'Comentar contenido'), ('_administrar_tipo_de_contenido', 'Administar tipo de contenido'), ('_crear_tipo_de_contenido', 'Crear tipo de contenido'), ('_editar_tipo_de_contenido', 'editar tipo de contenido'), ('_eliminar_tipo_de_contenido', 'Eliminar tipo de contenido'), ('_filtrar_contenidos_por_categoria', 'Filtrar contenidos por categoria'), ('_filtrar_contenidos_por_tipo', 'Filtrar contenidos por tipo'), ('_notificar_eventos', 'Notificar eventos'), ('_notificar_solicitud_de_edicion', 'Notificar solicitud de edicion'), ('_notificar_solicitud_de_publicacion', 'Notificar solicitud de publicacion'), ('_notificar_publicacion_del_contenido', 'Notificar solicitud de contenido'), ('_administrar_estado', 'Administrar estado'), ('_crear_estado', 'Crear Estado'), ('_modificar_estado', 'Modificar estado'), ('_eliminar_estado', 'Eliminar estado'), ('_visualizar_tablero_kanban', 'Visualizar tablero Kanban'), ('_modificar_tablero_kanban', 'Modificar tablero Kanban'), ('_visualizar_historial', 'Visualizar historial'), ('_visualizar_reporte', 'Visualizar reporte')]},
        ),
    ]
