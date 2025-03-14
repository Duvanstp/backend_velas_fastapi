import bcrypt


# Password hashing and verification
def verify_password(plain_password: str, hashed_password: str) -> bool:
    hashed_password_bytes = hashed_password.encode()
    return bcrypt.checkpw(plain_password.encode(), hashed_password_bytes)


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
