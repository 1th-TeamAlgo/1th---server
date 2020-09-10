from config.settings.secret import SECRET_KEY, ALGORITHM

import jwt

def jwt_get_payload(request):

    user_jwt = request.META['HTTP_X_JWT_TOKEN']
    user_payload = jwt.decode(user_jwt, SECRET_KEY, algorithm=ALGORITHM)
    return user_payload