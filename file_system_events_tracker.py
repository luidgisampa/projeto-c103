import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/BRASIL/Downloads"

# Classe Gerenciadora de Eventos
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"ola, {event.src_path} foi criado!")
    def on_deleted(self, event):
        print(f"opa! {event.src_path} foi excluido!")
    def on_moved(self, event):
        print(f"opa! {event.src_path} foi movido / ou alteraram seu nome")
    def on_modified(self, event):
        print(f"opa! {event.src_path} foi modificado!")

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido")
    observer.stop()
