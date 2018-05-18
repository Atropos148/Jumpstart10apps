import movie_svc
import requests.exceptions


def main():
    write_header()
    search_request_loop()


def write_header():
    print('------------------------------')
    print('        MOVIE SEARCH')
    print('------------------------------')


def search_request_loop():
    search = 'ONE-TIME-LOOP'

    while search != 'x':
        try:
            search = input('What movie do you want to search for?(x to exit) ')
            if search != 'x':
                results = movie_svc.find_movies(search)

                print('Found {} results'.format(len(results)))
                for r in results:
                    print('{} - {}'.format(r.year, r.title))
                print()

        except requests.exceptions.ConnectionError:
            print("Error! Your network is down!")
        except ValueError as error:
            print(error)
        except Exception as x:
            print('Unexpected error. Details:\n{}'.format(x))

    print('Exiting...')


if __name__ == '__main__':
    main()
