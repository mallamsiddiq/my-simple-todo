MY-TODO-TEST

# Instruction On Running Locally:
 make sure pip is installed locally with python. 
 on your local machine while inside this directory run

1.	pip install -r requirements.txt
2.	python manage.py makemigrations
3. 	python manage.py migrate
4.	python manage.py runserver

# testing:

The app is locally hosted on port: 8000, ( with your app running locally) kindly visit  http://127.0.0.1:8000/todos/ to view the list of all your schedules listed with the date expected for execution. This page serves as the home page for this app. There are two icons on this home page, the home button and the plus-sign icon, I made this home button available on all page in this app so navigating back to the home page won’t be a stress for the user. But the add icon on the bottom right corner is there to pop-up a form so you can easily create a new task or schedule.

Click on a specific schedule to redirect to a page that details all attributes of that schedule i.e http://127.0.0.1:8000/todos/details/8 for details of of the schedule with unique id 8.  while on this detail page you’ll a notice a pen icon on the bottom right corner indicating edit or update . Click this icon to go to edit page I.e http://127.0.0.1:8000/todos/update/8   where you can edit, update and make changes to this particular schedule. Also on this update page you’ll notice a bin icon on the bottom right corner, click this icon to permanently delete this particular schedule. On the top right corner of the update page is a return icon to go back if you change your mind on to not edit,update or delete the clicked schedule.

#note:
This is a test app and expected to run locally, if for a reason you decide to push this to production kindly contact the developer @ mallamsiddiq@gmail.com  to make necessary changes on security and other advanced issues.



Thanks,
Akinyemi sodiq


