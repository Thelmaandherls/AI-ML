# Secure coding/auth implementation

import jwt 

def verify_token(token: str):
    payload = jwt.decode(token, "secret", algorithms=["HS256"])
    return payload
