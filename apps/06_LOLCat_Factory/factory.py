from os import path, mkdir
from subprocess import call
from platform import system

import cat_service


def main():
    write_header()
    folder = get_or_create_output_folder()
    print(f'Found or created folder: {folder}')
    download_cats(folder)
    display_cats(folder)


def write_header():
    print('-------------------')
    print('    CAT FACTORY')
    print('-------------------')


def get_or_create_output_folder():
    base_folder = path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = path.join(base_folder, folder).replace('\\', '/')

    if not path.exists(full_path) or not path.isdir(full_path):
        print(f'Creating new directory at {full_path}')
        mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Talking to server...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = f'lolcat_{i}'
        print(f'Downloading cat {name}')
        cat_service.get_cat(folder, name)

    print('Done')


def display_cats(folder):
    print('Opening cats in OS window')
    if system() == 'Darwin':
        call(['open', folder])
    elif system() == 'Windows':
        # necessary to make Explorer work
        folder = folder.replace('/', '\\')
        call(['explorer', folder])
    elif system() == 'Linux':
        call(['xdg-open', folder])
    else:
        print(f"Sorry, We don't support your OS:{system}")


if __name__ == '__main__':
    main()
