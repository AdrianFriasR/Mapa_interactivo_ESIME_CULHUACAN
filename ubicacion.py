import math

def distancia_haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Radio de la Tierra en metros

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (math.sin(delta_phi / 2) ** 2 +
         math.cos(phi1) * math.cos(phi2) *
         math.sin(delta_lambda / 2) ** 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def detectar_edificio_actual(lat, lon, edificios):
    edificio_cercano = None
    distancia_minima = float("inf")

    for edificio in edificios:
        d = distancia_haversine(
            lat, lon,
            edificio.latitud, edificio.longitud
        )

        if d < distancia_minima:
            distancia_minima = d
            edificio_cercano = edificio

    return edificio_cercano, distancia_minima


