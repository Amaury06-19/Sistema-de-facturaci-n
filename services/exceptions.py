class ServiceError(RuntimeError):
    pass

class NotFoundError(ServiceError):
    def __init__(self, entity: str, id_: str | None = None, detail: str | None = None):
        msg = f"{entity} no encontrado"
        if id_:
            msg += f" (id={id_})"
        if detail:
            msg += f": {detail}"
        super().__init__(msg)

class ConflictError(ServiceError):
    def __init__(self, detail: str = "Conflicto de datos (unicidad, integridad referencial, etc.)"):
        super().__init__(detail)

class BadRequestError(ServiceError):
    def __init__(self, detail: str = "Solicitud inválida"):
        super().__init__(detail)
