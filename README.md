# Batalla Pokémon

Juego de batalla por turnos para la terminal, escrito en Python. Elige un Pokémon,
combate contra un rival aleatorio, usa curaciones y consulta el estado de la batalla.

## Requisitos

- Python 3.10 o superior
- `pip`

## Instalación

Clona este repositorio y entra en la carpeta del proyecto. Se recomienda crear un
entorno virtual:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

Si PowerShell no permite activar el entorno, puedes instalar la dependencia con:

```powershell
py -m pip install -r requirements.txt
```

## Cómo jugar

Desde la carpeta del proyecto, ejecuta:

```powershell
py batallapokemon.py
```

Sigue las opciones que aparecen en pantalla para atacar, curarte, ver el estado o
hacer que tu Pokémon huya.
