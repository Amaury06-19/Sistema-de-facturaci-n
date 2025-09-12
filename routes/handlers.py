from fastapi import FastAPI
from fastapi.responses import JSONResponse
from services import NotFoundError, ConflictError, BadRequestError

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(NotFoundError)
    async def not_found_handler(_, exc: NotFoundError):
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(ConflictError)
    async def conflict_handler(_, exc: ConflictError):
        return JSONResponse(status_code=409, content={"detail": str(exc)})

    @app.exception_handler(BadRequestError)
    async def bad_request_handler(_, exc: BadRequestError):
        return JSONResponse(status_code=400, content={"detail": str(exc)})
