import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'loc, condition, temp, scale')


def main():
    print_the_header()

    city = input('What city do you want the weather for?(London) ').lower()

    html = get_html_from_web(city)

    report = get_weather_from_html(html)

    # display forecast
    print('The weather in {} is {} and temperature is {} {}'.format(
        report.loc,
        report.condition,
        report.temp,
        report.scale
    ))


def print_the_header():
    print('-------------------------------')
    print('       WEATHER CLIENT APP')
    print('-------------------------------')


def get_html_from_web(city):
    url = f'https://www.wunderground.com/weather-forecast/sk/{city}'
    response = requests.get(url)
    # print(url)
    # print(response.status_code)

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print(soup.prettify()) used for figuring out what the HTML looks like

    loc = soup.find(id='location').find(class_='city-nav-header').get_text()
    condition = soup.find(class_='small-3 columns').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-data').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-data').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(loc=loc, condition=condition, temp=temp, scale=scale)
    return report


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
