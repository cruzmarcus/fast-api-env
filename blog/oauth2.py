from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from . import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token_jwt: str = Depends(oauth2_scheme)):
    crecentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could noit validadte credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token.verify_token(token_jwt, crecentials_exception)

