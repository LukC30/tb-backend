from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['sha256_crypt'], deprecated="auto")

def password_encript(password: str):
    return pwd_context.hash(password)