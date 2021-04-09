import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from file_utilities import *


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        print('*** [CREATED] ', event.src_path)
        pass

    @staticmethod
    def on_modified(event):
        if os.path.isdir(event.src_path):  # is a directory |?|
            return
        if is_code_file(event) == True:
            path_to_folder = make_folder('code')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_text_file(event) == True:
            path_to_folder = make_folder('text')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_pdf_file(event) == True:
            path_to_folder = make_folder('pdf')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_mp3_file(event) == True:
            path_to_folder = make_folder('audio')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_image_file(event) == True:
            path_to_folder = make_folder('images')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_video_file(event) == True:
            path_to_folder = make_folder('videos')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_doc_file(event) == True:
            path_to_folder = make_folder('word documents')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_spreadsheet_file(event) == True:
            path_to_folder = make_folder('spreadsheets')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_presentation_file(event) == True:
            path_to_folder = make_folder('presentation files')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_executable_file(event) == True:
            path_to_folder = make_folder('executable files')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_compressed_file(event) == True:
            path_to_folder = make_folder('compressed files')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

            # Default
        elif is_aleatory_file(event) == True:
            path_to_folder = make_folder('unlisted files')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

    @staticmethod
    def on_deleted(event):
        pass

    @staticmethod
    def on_moved(event):
        print('*** [MOVED] ', event.src_path)
        pass


file_change_handler = Handler()
observer = Observer()
os.chdir('C:\\Users\\gabri\\Downloads')  # Changing CWD
print('Atuando em: ', os.getcwd())
observer.schedule(file_change_handler, os.getcwd(), recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
