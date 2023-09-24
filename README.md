# Blog_App_Repo
I have created a Blog Api to perform the CRUD operations and Token Based Authentication

To run the project please follow the following details
1. First activate the virtual environment using command 'source venv/bin/activate' or 'source venv/Scripts/activate' 
1. Install the requirements.txt file using 'pip install -r requirements.txt'
2. After the successfully installation of the requirements.txt file run the command 'python manage.py migrate'
3. then run the 'python manage.py runserver'

This steps will help you to successfully run the project.
Now open the postman in your local system and run test the API that I have created and I am sharing the api's that I have created below:
1. To create or to get all the blogs => http://127.0.0.1:8000/api/posts/ {get, post}
2. To retrieve , update or delete use this => http://127.0.0.1:8000/api/posts/{id} (patch, put , delete, get)
3. to create the user use this => http://127.0.0.1:8000/register
4. To access the admin panel of the project => http://127.0.0.1:8000/admin and to create the admin use command 'python manage.py createsuperuser'

   Note : When we create the user then Token authentication will create automatically and you will find that in admin panel with your username.
