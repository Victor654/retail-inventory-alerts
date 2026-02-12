from fastapi import APIRouter, HTTPException
from app.auth.schemas import RequestCodeSchema
from app.auth.service import generate_otp, store_otp

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/request-code")
def request_code(data: RequestCodeSchema):
    otp = generate_otp()
    store_otp(data.phone_number, otp)

    # Aquí luego enviaremos WhatsApp con Celery
    print(f"OTP para {data.phone_number}: {otp}")

    return {"message": "Código enviado por WhatsApp"}
