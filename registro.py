import json


ARCHIVO_EVENTOS = "eventos.jsonl"


def guardar_evento(evento):
    with open(ARCHIVO_EVENTOS, "a", encoding="utf-8") as archivo:
        archivo.write(
            json.dumps(evento, ensure_ascii=False) + "\n"
        )