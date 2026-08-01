import json
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType


file_path="src/data/products.json"

def get_all_products():
    with open(file_path, 'r') as p:
        return json.load(p)


def create_product(products):
    with open(file_path, 'w') as p:
        json.dump(products, p)

email_conf=ConnectionConfig(
    MAIL_USERNAME="rockrockrocky.787@gmail.com",
    MAIL_PASSWORD="ugie omld oxur pzgs",
    MAIL_FROM="rockrockrocky.787@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="FASTAPI Tutorial",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

async def simple_send(email: str):
    body="""<p>Hi , Your order has beenn placed successfullly</p> """

    message=MessageSchema(
            subject="Order Confirmation",
            recipients=[email],
            body=body,
            subtype=MessageType.html
        )
    
    fm=FastMail(email_conf)
    await fm.send_message(message)