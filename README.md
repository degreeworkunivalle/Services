Services
===================
[![Build Status](https://travis-ci.org/degreeworkunivalle/Services.svg?branch=master)](https://travis-ci.org/degreeworkunivalle/Services)

#Done
###Sprint 1
  * Users
  * Gropus
  * Authentication

###Sprint 2
* Wiki
* Forum
* Comments

### Sprint 3
* Evaluations
* Activities

### Sprint 4
 * Badges

### Sprint 5
 * Notifications
 * Plataform

### Sprint 6
 * Testing

______________________
###Requeriments
    sudo apt-get install python3.4
    sudo apt-get install python3.4-dev
    sudo apt-get install libjpeg-dev

###Installation

Step 1
Create Date base

    python manage.py syncdb

Step 2
Create default app for (Oauth2) Authentication

	python manage.py Oauth

Step 3
Create default Groups
	
	python manage.py Group
	
Step 4
Create default Degrees 
	
	python manage.py Degrees
