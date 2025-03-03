"""Main app!
Before running the app be sure u completed everything from .env
(sql username and password, email and user password)
and make sure you have sqlite open.
To run streamlit go in the terminal and type <streamlit run main.py>"""

import smtplib
import streamlit as st
from src.get_news import GetNewsData, Path, load_dotenv, os
from src.modules import NewsData, session

# setting working directory
WORKING_DIR = Path(__file__).parent
ENV_PATH = WORKING_DIR / ".env"

# getting all the information we need from .env
load_dotenv(ENV_PATH)
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PW")

# the UI and instructions for the user
st.title("News Sender 5000")
st.write("Please insert your E-mail(username@domain.topdomain, ex: mircea.ionita@gmail.com)")
# email_searchbar for the user to write his/her E-mail,
# select_topic is for selecting what type of news to get,
# send_button is the button to execute everything
email_searchbar, select_topic, send_button = st.columns([5, 5, 5], vertical_alignment="bottom")
with select_topic:
    select_topic = st.selectbox("Your topic", ("war", "politics", "education", "health",
                                "economy", "business","fashion", "sport", "environment"))
# what ever the user is writing the email will be lowercase
with email_searchbar:
    email_searchbar = (st.text_input("e-mail")).lower()
with send_button:
    send_button = st.button("Send", use_container_width=True)

# checking if the email is writen correctly
if send_button and "@" not in email_searchbar:
    # raise error if the email does not contain @
    st.error('You need "@" for a e-mail')
else:
    if send_button and "." not in email_searchbar[email_searchbar.index("@")::]:
        # raise error if the email does not contain a domain or top domain
        st.error('You need a domain and a top domain, '
                 'ex: yahoo.com')

# using GetNewsData to get the news information
news = GetNewsData(select_topic)
# news.valid_data will get the title, author, description and the content
news_data = news.valid_data()
# the number of news based on the topic the user chose and getting only the 10 most popular
NEWS_NR = news.number_of_news()
st.write(f"{NEWS_NR} articles about {select_topic} and here are top 10")

# this code starts when the user presses the button
if send_button:
    server = smtplib.SMTP("smtp.gmail.com", 587) # create SMTP session
    server.starttls() # start tls for security
    server.login(MY_EMAIL, MY_PASSWORD) # loging to the account via .env

    NEWS_TO_SEND = ""

    # iterating through news_data
    for key, values in news_data.items():

        # the subject and the message that will be added to the empty string (news_to_send)
        SUBJECT = "Today's news!!!!!"
        MESSAGE = (f"\n\nTitle: {values['title']}\n\nAuthor: {values['author']}\n\n"
                   f"Description: {values['description']}\n\n"
                   f"Content: {values['content']}\n\nURL: {values['url']}\n\n\n\n")
        NEWS_TO_SEND += MESSAGE

        # adding the title and url to database only if it doesn't exist
        Title = values['title']
        Url = values['url']
        existing_title = session.query(NewsData).filter_by(Title=Title).first()

        if existing_title:
            print(f"{key} already in table")
        else:
            news = NewsData(Title=Title, Url=Url)
            session.add(news)
            session.commit()

        # if the code reaches the 10th article it will stop, send the email and break the loop
        if key == "News10":
            TEXT = f"Subject: {SUBJECT}\n\n{NEWS_TO_SEND}"

            server.sendmail(MY_EMAIL, email_searchbar, TEXT.encode('UTF-8'))
            st.write("Email sent successfully")
            break
