from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

from settings import appsettings


class Authorize:
    def __call__(self, token: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))):
        if token is None:
            raise HTTPException(status_code=401, detail="Unauthorized")

        return self.verify(token.credentials)

    @staticmethod
    def verify(token: str):
        jwks_url = f'https://{appsettings.AUTH_DOMAIN}/.well-known/jwks.json'
        jwks_client = jwt.PyJWKClient(jwks_url)
        try:
            signing_key = jwks_client.get_signing_key_from_jwt(token).key
        except jwt.exceptions.PyJWTClientError as error:
            return {"status": "error", "message": error.__str__()}
        except jwt.exceptions.DecodeError as error:
            return {"status": "error", "message": error.__str__()}

        try:
            payload = jwt.decode(
                token,
                signing_key,
                algorithms='RS256',
                audience=appsettings.AUTH_AUDIENCE,
                issuer=appsettings.AUTH_ISSUER
            )
        except Exception as e:
            return {"status":"error", "message": e.__str__()}

        return payload
