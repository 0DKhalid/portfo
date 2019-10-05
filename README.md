# portfolio

### Run and Modify

1. Be sure is a python 3 install on your computer.

2. clone this repo.

3. [install pipenv](https://github.com/pypa/pipenv).

4. run:`pipenv install`.

### \*Project configruation

I use MySQL database hosted in [remotemysql.com](https://remotemysql.com) this website allow you create free hosted database.

##### After You create database:

1. create yaml file and inside it put this config:
   > mysql_host: 'Your_Database_host'\
   > mysql_password: 'Your_Database_Password'\
   > mysql_name: 'Your_Database_name'\
   > mysql_user: 'Your_Database_User'\
   > url_name: 'Any_String' #like 'khalid'\
   > url_password: 'Any_namber' #like 12321

**url_name and url_password**:
To fetch all messages that send through contact page when you visit this path `http://localhost:5000/url_name/url_password`
