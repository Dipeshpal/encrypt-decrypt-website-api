from typing import Union
from fastapi import FastAPI
from encrypt_text import start_encryption
from decrypt_text import start_decryption
from fastapi import Form
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
import os

unlock_sentence = os.environ.get('unlock_sentence', "some sentence")
default_secret_number = os.environ.get('default_secret_number', 5)

templates = Jinja2Templates(directory="templates")


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/encrypt")
def encrypt_text(text_to_encrypt: str = Form()):
    encrypted_text, shape = start_encryption(text_to_encrypt.strip())
    return {"encrypted_text: ": encrypted_text, "secret_number": shape}


@app.get("/decrypt")
def decrypt_text(text_to_decrypt: Union[str, None] = None, secret_number: Union[int, None] = default_secret_number):
    res = start_decryption(text_to_decrypt.strip(), secret_number)
    return {"decrypted_text: ": res.strip()}


@app.post("/validate")
def validate_input(input_text: str = Form()):
    if unlock_sentence.strip() == input_text.strip():
        return "success"
    else:
        return "failed"


@app.get("/")
async def home(request: Request):
    if default_secret_number is None:
        return "Please set the default_secret_number environment variable"
    if unlock_sentence is None:
        return "Please set the unlock_sentence environment variable"
    return templates.TemplateResponse("home.html", {"request": request})
