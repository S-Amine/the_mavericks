from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import *
from django.utils.html import format_html
from django.templatetags.static import static
from wagtail import hooks

# I have to change the location of the files
@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('css/the_mavericks.css'))

class ServicesAdmin(ModelAdmin):
    model = Service
    base_url_path = 'ServicesAdmin' # customise the URL from default to admin/bookadmin
    menu_label = 'Services'  # ditch this to use verbose_name_plural from model
    menu_icon = 'cogs'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    # list_display = ('title', 'author')
    # list_filter = ('author',)
    # search_fields = ('title', 'author')

class ProjectsAdmin(ModelAdmin):
    model = Project
    base_url_path = 'ProjectsAdmin' # customise the URL from default to admin/bookadmin
    menu_label = 'Projects'  # ditch this to use verbose_name_plural from model
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    # list_display = ('title', 'author')
    # list_filter = ('author',)
    # search_fields = ('title', 'author')


class CategoriesAdmin(ModelAdmin):
    model = Category
    base_url_path = 'CategoriesAdmin' # customise the URL from default to admin/bookadmin
    menu_label = 'Categories'  # ditch this to use verbose_name_plural from model
    menu_icon = 'tag'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    # list_display = ('title', 'author')
    # list_filter = ('author',)
    # search_fields = ('title', 'author')

class TeamMemberAdmin(ModelAdmin):
    model = TeamMember
    base_url_path = 'TeamMemberAdmin' # customise the URL from default to admin/bookadmin
    menu_label = 'TeamMembers'  # ditch this to use verbose_name_plural from model
    menu_icon = 'user'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    # list_display = ('title', 'author')
    # list_filter = ('author',)
    # search_fields = ('title', 'author')

class ServicesGroup(ModelAdminGroup):
    menu_label = 'Our team'
    menu_icon = 'snippet'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ServicesAdmin ,CategoriesAdmin, TeamMemberAdmin, ProjectsAdmin)

modeladmin_register(ServicesGroup)
