import smtplib
from src.get_news import Path, load_dotenv, os
WORKING_DIR = Path(__file__).parent
ENV_PATH = WORKING_DIR / ".env"

load_dotenv(ENV_PATH)
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PW")
receiver_mail = "darkwolfggg@gmail.com"

subject = "test1"
message = "test mesaj 123"

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(MY_EMAIL, MY_PASSWORD)

server.sendmail(MY_EMAIL, receiver_mail, text)
print("sent!")