# Generated by Django 4.2.4 on 2023-09-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolesdeSistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('defecto', models.BooleanField(default=False)),
                ('descripcion', models.TextField(blank=True, max_length=60)),
                ('permisos', models.ManyToManyField(blank=True, to='auth.permission')),
            ],
            options={
                'permissions': [('_acceder_al_sistema', 'Acceder al sistema'), ('_crear_usuario', 'Crear usuario'), ('_crear_proyecto', 'Crear Proyecto'), ('_crear_sprint', 'Crear sprint'), ('_crear_us', 'Crear US'), ('_crear_tipos_us', 'Crear tipos de US'), ('_crear_roles', 'Crear roles'), ('_iniciar_proyecto', 'Iniciar un proyecto'), ('_iniciar_sprint', 'Iniciar Sprint'), ('_asignar_miembro_us', 'Asignar miembro a un US'), ('_asignar_roles', 'Asignar roles a usuario dentro del proyecto'), ('_asignar_us', 'Asignar US a un Sprint'), ('_asignar_miembro_sprint', 'Asignar miembro a un Sprint'), ('_asignar_miembro_proyecto', 'Asignar miembro a un Proyecto'), ('_reasignar_miembro_us', 'Reasignar miembro a un US'), ('_eliminar_roles', 'Eliminar roles a usuario'), ('_eliminar_tipoUs', 'Eliminar tipos de US'), ('_eliminar_usuario', 'Eliminar usuario'), ('_eliminar_us_sprint', 'Eliminar Us de un sprint'), ('_cancelar_proyecto', 'Cancelar Proyecto'), ('_cancelar_US', 'Cancelar US'), ('_cancelar_sprint', 'Cancelar Sprint'), ('_finalizar_sprint', 'Finalizar Sprint'), ('_finalizar_proyecto', 'Finalizar Proyecto'), ('_modificar_estado_proyecto', 'Modificar estado del proyecto'), ('_modificar_sprint', 'Modificar sprint'), ('_modificar_estado_sprint', 'Modificar estado de un sprint'), ('_modificar_us', 'Modificar US'), ('_modificar_estado_us', 'Modificar estado de US'), ('_modificar_backlog', 'Modificar Product Backlog'), ('_modificar_sprint_backlog', 'Modificar Sprint Backlog'), ('_modificar_tipos_us', 'Modificar tipos de US'), ('_importar_tipos_us', 'Importar tipos de US'), ('_importar_roles', 'Importar Roles'), ('_cargarHoras_us', 'Cargar Horas de trabajo'), ('_visualizar_historial_us', 'Visualizar historial de un US'), ('_visualizar_sprint', 'Visualizar Sprint'), ('_visualizar_Product_Backlog', 'Visualizar Product Backlog'), ('_visualizar_BurnDown_Chart', 'Visualizar BurnDown Chart'), ('_visualizar_historial_proyecto ', 'Visualizar Historial del Proyecto'), ('_visualizar_kanban', 'Visualizar Tabla Kamban'), ('_visualizar_sprint_backlog', 'Visualizar Sprint Backlog'), ('_visualizar_proyecto', 'Visualizar Proyecto'), ('_visualizar_proyecto_asigando', 'Visualizar Proyecto Asignado'), ('_visualizar_roles', 'Visualizar roles a usuario'), ('_visualizar_usuario', 'Visualizar usuario del Sistema'), ('_visualizar_notificaciones', 'Visualizar notificaciones'), ('_visualizar_tipoUS', 'Visualizar tipos de US')],
            },
        ),
    ]
