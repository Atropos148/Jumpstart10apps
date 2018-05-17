from requests import get
from os import path
from shutil import copyfileobj


def get_cat(folder, name):
    url = 'https://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    response = get(url, stream=True)
    return response.raw


def save_image(folder, name, data):
    file_name = path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout:
        copyfileobj(data, fout)
