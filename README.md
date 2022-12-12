# Flynnt Knapp Code Catalog

## Features

## **WARNING:**

* [Deployment checklist - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/)
  * This template has Django `SECRET_KEY` exposed in both development and production settings files. It is important to create your own separate `SECRET_KEY` for development and production and keep them out of the codebase. This template has `SECRET_KEY` exposed in order to get the user up and running quickly.

## Process

1. [Create Repository from DjangoCustomUserStarter Template](notes/01_create_repository_from_template.md)
1. [Run Application Locally](notes/02_run_application_locally.md)
1. [Create Heroku Application Server Instance](notes/03_create_heroku_application_server_instance.md)
1. [Provision Database Server Instance](notes/04_provision_database_server_instance.md)
1. [Add DJANGO_SETTINGS_MODULE to Config Vars](notes/05_add_django_settings_module_to_config_vars.md)
1. [Add Django SECRET_KEY to Config Vars](notes/06_add_secret_key_to_config_vars.md)
1. [Add Database Settings to Config Vars](notes/07_add_database_settings_to_config_vars.md)
1. [Modify ALLOWED_HOSTS](notes/08_modify_allowed_hosts.md)
1. [Push to Heroku and Create Superuser](notes/09_push_to_heroku_and_createsuperuser.md)

## Excellent resources, this project wouldn't have been possible without these

* CustomUser method: [Django Best Practices: Custom User Model - Will Vincent - learndjango.com](https://learndjango.com/tutorials/django-custom-user-model)
* Docutils: [The Django admin documentation generator - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/)
* DEV and PROD settings: [Configuring Django Settings for Production - thinkster.io](https://thinkster.io/tutorials/configuring-django-settings-for-production)

## Links to this project's pages
