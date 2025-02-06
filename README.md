# Event Organizing Project

## Description
This project helps in organizing events efficiently, allowing users to create, manage, and participate in various events. Built with Django, it leverages MySQL for database management and Cloudinary for media storage.

## Requirements
To run this project, you'll need the following dependencies:

```bash
pip install -r requirements.txt
```

## Setting Up MySQL on Railway
1. Deploy MySQL on Railway using the following steps:
   - Go to Railway and create a new project.
   - Deploy a MySQL instance using the Railway template.
   - Use the environment variables provided by Railway to connect to your MySQL instance.

2. Update your `settings.py` in Django to use the MySQL database:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'your_db_host',
           'PORT': 'your_db_port',
       }
   }
   ```

## Integrating Cloudinary with Django
1. Install the Cloudinary Django SDK:
   ```bash
   pip install django-cloudinary-storage
   ```

2. Add `cloudinary_storage` and `cloudinary` to your `INSTALLED_APPS` in `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'cloudinary_storage',
       'cloudinary',
       ...
   ]
   ```

3. Configure Cloudinary settings in your `settings.py`:
   ```python
   CLOUDINARY_STORAGE = {
       'CLOUD_NAME': 'your_cloud_name',
       'API_KEY': 'your_api_key',
       'API_SECRET': 'your_api_secret',
   }

   DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
   os.environ["CLOUDINARY_URL"] = "cloudinary://your_api_key:your_api_secret@your_cloud_name"
   ```

4. Use Cloudinary for image uploads in your Django models:
   ```python
   from django.db import models
   from cloudinary.models import CloudinaryField

   class Event(models.Model):
       title = models.CharField(max_length=100)
       description = models.TextField()
       date = models.DateField()
       image = CloudinaryField('image')
   ```

## Running the Project
1. Migrate the database:
   ```bash
   python manage.py migrate
   ```

2. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Contributing
We welcome contributions to the Event Organizing project! If you'd like to contribute, please follow these guidelines:
1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and ensure all tests pass.
4. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute this project as long as you include the original license.
