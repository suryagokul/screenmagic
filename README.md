## screenmagic Assignment 2  send_mail from csv and schedule

requirements :

      python >=3.x        download python versions from https://www.python.org/downloads/


HowToRun the project

pip install requirements.txt

python run.py        give input sender mail and password..

run.py takes all the data and it will done all validations,then send mails..

for scheduling mails : 
 
     open run.py 

     uncomment 44,45,68,69,70,71

     comment out 47,74 line

     then open terminal and type
   
           python run.py

     it Schedule messages for future date, if date is added in Schedule On column, if not then sends immediately


if you want to create virtual environment for this and run the project then do :

For Linux 
    
     pip install virtualenv

     virtualenv --python=/usr/bin/python3 env_name

     source env_name/bin/activate

    move to project directory  and run 

          pip install requirements.txt

          python run.py

For Windows

   pip install virtualenv 

   virtualenv myenv

   myenv\Scripts\activate      (You can explicitly specify your path too.)

   pip install requirements.txt

   python run.py

    









