import jwt

secret_key = "A0dL$2#7k$r28ehmYoi3Sz1W!Dya"


def login_encode(client_id, phone_number):
    # Here, you would typically check the username and password against a database.
    # For the sake of this example, we will assume any username and password combination is valid.

    if client_id and phone_number:
        # The payload contains the user info and an expiration time
        payload = {
            'client_id': client_id,
            'phone_number': phone_number
        }

        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token


def decode_verify_token(token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        # If the token is valid and not expired, the payload will be returned
        return payload
    except jwt.ExpiredSignatureError:
        # The token has expired
        return None
    except jwt.InvalidTokenError:
        # The token is invalid
        return None



# login_encode(1, '6382502960')