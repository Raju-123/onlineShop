# onlineShop
# Tools used
    - Postman
    - Msql
    - Python

# To get project
    clone git url by the command - git clone https://github.com/Raju-123/onlineShop.git

# To run project
    1. Create a conda environment 
        conda create python=3.0 -n onlineShop
    
    2. Install all packages in requirement.txt file
        pip install -r requrement.txt

    1. Make migration of each mode
        python manage.py makemigration
    
    2. Migrate
        python manage.py migrate

    3. Run project
        Python manage.py runserver