# Ejercicio: Top shows de Netflix (rating >= 90) desde 01netflix.csv

from csv import DictReader

CSV_PATH = "./data/01netflix.csv"
RATING_THRESHOLD = 90

# Buenas prácticas: usar 'with' para manejar el archivo
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    reader = DictReader(f)

    total_rows = 0
    kept_rows = 0
    log_lines = []  # simularemos el "log" como un conjunto de líneas en memoria

    # Encabezado del "log" simulado
    log_header = f"# LOG: Mejores shows Netflix (rating >= {RATING_THRESHOLD})\n"
    log_lines.append(log_header)

    for row in reader:
        total_rows += 1

        # Tomamos específicamente estas columnas
        title = row.get("title")
        rating_raw = row.get("user rating score")

        # Limpieza simple: quitar espacios, porcentajes o formatos tipo '92/100'
        title = title.strip()
        rating_str = rating_raw.strip().replace("%", "").split("/")[0].strip()
        numeric_check = rating_str.replace(".", "", 1)
        if not numeric_check.isdigit():
            # Si no parece número, lo saltamos sin romper el flujo
            continue

        rating = float(rating_str)

        # Condicional clave del ejercicio
        if rating >= RATING_THRESHOLD:
            kept_rows += 1
            # “f-string” para nuestro "log" simulado
            log_lines.append(f"[TOP] title='{title}'  rating={rating:.1f}")

    # Resumen final al "log"
    log_lines.append("")  # línea en blanco
    log_lines.append(f"# Total filas leídas: {total_rows}")
    log_lines.append(f"# Total con rating >= {RATING_THRESHOLD}: {kept_rows}")

# “Mostrar el log”: sólo un print, nada de escribir a archivo en esta práctica
print("\n".join(log_lines))