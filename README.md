#News app

##How to run the app

>clone the repository using git clone (GitHub url here)
>
>If you want to use the app go to terminal and type "streamlit run main.py"
> remember to have sql lite running 

##Requirements

To get all the requirements go in the terminal and run
"- pip install -r requirements.txt"
You also need to have sqlite open and create the database news using
"CREATE DATABASE news;" and use it with "USE news;"

##How to get user password for sending the email
>First you need to have 2-step verification turned on
to do that you need to go to your account, to security and click 2-step verification
> Next you need to go to https://myaccount.google.com/apppasswords?rapt=AEjHL4Opsf1ffRL3aVHCQp5acDQacv-2uuhF84HtV6zhnRSzcyibnqwNWpZ2_-rMqGOl1ZIuj85UsPBC3Ma1FQR9fpl2xF97GMVcSwi7PDi5NOZyl0GCzbo
name your app and then copy the password.
> Paste the password in .env at MY_PW
> If you have spaces between the password make sure to delete them.
