from fastapi import FastAPI
from routes.reservation_routes import router as reservation_router
from routes.places_routes import router as places_router
from routes.user_routes import router as user_routes


app = FastAPI()

# Incluir las rutas desde otros archivos
app.include_router(reservation_router, prefix="/reservation", tags=["Reservation"])
app.include_router(places_router, prefix="/setPlaces", tags=["Places"])
app.include_router(user_routes, prefix="/setUser", tags=["Users"])

@app.get("/")
def root():
    return {"message": "API running"}
