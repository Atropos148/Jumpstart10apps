import csv
import os

try:
    import statistics
except:
    # error code
    import statistics_standin_for_py2 as statistics

from data_types import Purchase


def main():
    write_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def write_header():
    print('-------------------------------')
    print('    REAL ESTATE DATA MINER')
    print('-------------------------------')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


def query_data(data):
    data.sort(key=lambda p: p.price)

    # most expensive house
    high_purchase = data[-1]
    print('Most expensive house is ${:,}'.format(high_purchase.price),
          ' with {} beds and {} baths.'.format(high_purchase.beds, high_purchase.baths))

    # least expensive house
    low_purchase = data[0]
    print('Cheapest house is ${:,}'.format(low_purchase.price),
          ' with {} beds and {} baths.'.format(low_purchase.beds, low_purchase.baths))

    # average house price
    prices = [
        p.price  # projection or items
        for p in data  # set to process
    ]
    avg_price = statistics.mean(prices)
    print('The average price for a house is ${:,}'.format(int(avg_price)))

    # average price of 2 bedroom house
    two_bed_homes = (
        p  # projection or items
        for p in data  # set to process
        if p.beds == 2  # test/condition
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    avg_price = statistics.mean((p.price for p in homes))
    avg_baths = statistics.mean((p.baths for p in homes))
    avg_sqft = statistics.mean((p.sq_ft for p in homes))
    print('Average 2 bedroom home is ${:,}, baths={}, sqft={}'
          .format(int(avg_price), round(avg_baths, 1), round(avg_sqft, 1)))


if __name__ == '__main__':
    main()
