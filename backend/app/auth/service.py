import random
import hashlib
from datetime import timedelta
from app.core.redis import redis_client

OTP_EXPIRATION_SECONDS = 300  # 5 minutos

def generate_otp():
    return str(random.randint(100000, 999999))

def hash_otp(otp: str):
    return hashlib.sha256(otp.encode()).hexdigest()

def store_otp(phone_number: str, otp: str):
    otp_hash = hash_otp(otp)
    redis_key = f"otp:{phone_number}"
    redis_client.setex(redis_key, OTP_EXPIRATION_SECONDS, otp_hash)
