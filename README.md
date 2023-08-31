# Boat_E-commerce
# CREATING DJANGO PROJECT
(30-08-2023)-Day -1 

Step-1: insatll Vitrual Evinroment

--> Create a new folder for your project(Django_Projects).
--> Go to your folder and Do this all commands :

    # --> insatll Vitrual Evinroment
        1.pip install virtualenv
        2.virtualenv name_of_the_virtualenvionment(My_Django_Projects)
    # After this command django will create one "brand new system"
    
    # --> Inside the folder:
        1.lib
        2. Scripts
        3.enviroment configurationtions
        4.python configurationtions

    # --> installing python package first.
        1.pip install python 

Step-2: Projects

--> Go to that folder and Create new folder for start your project(My_Django_Projects).
    1.cd My_Django_Projects
    2.cd Scripts
    3.activate
    4.pip install django
        
    # after this command dajngo will do all creation process
<!-- Downloading Django-4.2.4-py3-none-any.whl (8.0 MB)
     ---------------------------------------- 8.0/8.0 MB 9.3 MB/s eta 0:00:00
    Collecting asgiref<4,>=3.6.0 (from django)
    Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
    Collecting sqlparse>=0.3.1 (from django)
    Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
    Collecting tzdata (from django)
    Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
    Installing collected packages: tzdata, sqlparse, asgiref, django
    Successfully installed asgiref-3.7.2 django-4.2.4 sqlparse-0.4.4 tzdata-2023.3 -->

    5.If we check the packages and all modules (pip freeze)
<!-- (My_Django_Projects)            
        C:\Users\DreamsTattooing\Desktop\Django_Projects\My_Django_Projects\Scripts>pip freeze
        asgiref==3.7.2
        Django==4.2.4
        sqlparse==0.4.4
        tzdata==2023.3   -->
    
    6.deactivate

Step-3 : Cration of Django projects 
    # --> Here all commands: go to cmd prompt
    --> GO to Scripts.
        1.activate 
        2.django-admin startproject Boat_Ecommerce_Website
        # auto mattcally django will take care of creating project
            1.__init__.py
            2.asgi.py
            3.settings.py
            4.urls.py
            5.wsgi.py

<!-- #C:\Users\Dreams Tattooing\Desktop\Django_Projects\My_Django_Projects\Scripts>activate

(My_Django_Projects) C:\Users\Dreams Tattooing\Desktop\Django_Projects\My_Django_Projects\Scripts>django-admin startproject Boat_Ecommerce_Website

(My_Django_Projects) C:\Users\Dreams Tattooing\Desktop\Django_Projects\My_Django_Projects\Scripts>cd Boat_Ecommerce_Website -->

    # Now what is your requirements of your applicaion,templates files, static files,MDB5 like that....

Step-4: templates
    # we need html pages so we create one templates folder (mkdir templates)
        1. home.html
        2. Collections.html
        3. home.html
        4. home.html

step-5 : Specific static folders
    # We want css,js,images.
