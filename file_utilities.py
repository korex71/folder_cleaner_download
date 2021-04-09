import shutil
import os


def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]


def is_text_file(event):
    if extension_type(event) == 'txt':
        return True
    return False


def is_pdf_file(event):
    if extension_type(event) == 'pdf':
        return True
    return False


def is_mp3_file(event):
    if extension_type(event) == 'mp3':
        return True
    return False


def is_image_file(event):
    if extension_type(event) in ('png', 'jpg', 'bmp', 'gif', 'raw', 'jpeg'):
        return True
    return False


def is_video_file(event):
    if extension_type(event) in ('mov', 'mp4', 'avi', 'flv'):
        return True
    return False


def is_doc_file(event):
    if extension_type(event) in ('doc', 'docx'):
        return True
    return False


def is_spreadsheet_file(event):
    if extension_type(event) in ('xls', 'xlsx'):
        return True
    return False


def is_presentation_file(event):
    if extension_type(event) in ('ppt', 'pptx'):
        return True
    return False


def is_code_file(event):
    if extension_type(event) in ('py', 'cs', 'js', 'php', 'html', 'sql', 'css'):
        return True
    return False


def is_executable_file(event):
    if extension_type(event) in ('exe', 'msi'):
        return True
    return False


def is_compressed_file(event):
    if extension_type(event) in ('rar', 'zip', '7z', 'iso', 'bz2'):
        return True
    return False


def is_aleatory_file(event):
    if extension_type(event) in ('tmp', 'crdownload'):
        return False
    return True


def make_folder(foldername):
    os.chdir('C:\\Users\\gabri\\Downloads')
    if os.path.exists(foldername) == True:
        print('Pasta já existe, pulando criação...')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
        print('*** [MODIFIED] -> Movendo arquivo\n',
              event.src_path + '->' + path_to_new_folder)
    except:
        print('Arquivo já existente na pasta de destino')
        pass
