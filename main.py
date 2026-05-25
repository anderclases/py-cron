import schedule
import time
import subprocess
import logging
import os

# Configuración de logs para que veas todo en 'docker logs'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_script(script_path):
    logging.info(f"Ejecutando: {script_path}")
    try:
        # Ejecutamos el .sh y capturamos la salida
        result = subprocess.run(['sh', script_path], capture_output=True, text=True)
        if result.stdout:
            logging.info(f"Salida: {result.stdout.strip()}")
        if result.stderr:
            logging.error(f"Error en script: {result.stderr.strip()}")
    except Exception as e:
        logging.error(f"Error al lanzar el proceso: {e}")

# --- PROGRAMACIÓN (Sustituye tu crontab aquí) ---
schedule.every(5).minutes.do(run_script, "/app/scripts/duck.sh")
#schedule.every(10).seconds.do(run_script, "/app/scripts/check.sh")

logging.info("Orquestador de tareas iniciado...")

while True:
    schedule.run_pending()
    time.sleep(1)