import csv
import random
from time import sleep
import sqlite3

import requests
from bs4 import BeautifulSoup


def random_sleep():
    sleep(random.randint(1, 5))


def get_page_content(page: int, size: int = 100) -> str:
    query_parameters = {
        'indexName': 'auto,order_auto,newauto_search',
        'country.import.usa.not': '-1',
        'price.currency': '1',
        'abroad.not': '-1',
        'custom.not': '-1',
        'page': page,
        'size': size
    }
    base_url = 'https://auto.ria.com/uk/search/'
    response = requests.get(base_url, params=query_parameters)
    response.raise_for_status()
    return response.text


def get_ticket_details(model_title: str) -> list:
    url = f'https://auto.ria.com/uk{model_title}'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, features="html.parser")
    technical_info = soup.find("div", {"class": "technical-info"})
    arguments = technical_info.find_all("span", {"class": "argument"})[:3]
    details_list = [argument.get_text() for argument in arguments]
    return details_list


def export_data_from_csv_to_sqlite3(csv_file, db_file, table):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table}
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       car_id TEXT,
                       data_link_to_view TEXT,
                       details TEXT)''')

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute(f"INSERT INTO {table} (car_id, data_link_to_view, details) VALUES (?, ?, ?)", row)

    connection.commit()
    connection.close()


class CSVWriter:
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

        with open(self.filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)

    def write(self, row: list):
        with open(self.filename, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)


# class StdOutWriter:
#
#     def write(self, row: list):
#         print(row)


def main():
    writers = (
        CSVWriter('cars.csv', ['car_id', 'data_link_to_view', 'details']),
        CSVWriter('cars2.csv', ['car_id', 'data_link_to_view', 'details']),
        # StdOutWriter()
    )

    page = 2512
    csv_file = 'cars.csv'
    db_file = 'cars.db'
    table = 'cars'

    while True:

        print(f'Page: {page}')  # noqa: T201

        page_content = get_page_content(page)

        page += 1

        soup = BeautifulSoup(page_content, features="html.parser")

        search_results = soup.find("div", {"id": "searchResults"})
        ticket_items = search_results.find_all("section", {"class": "ticket-item"})

        if not ticket_items:
            break

        for ticket_item in ticket_items:
            car_details = ticket_item.find("div", {"class": "hide"})
            car_id = car_details['data-id']
            data_link_to_view = car_details['data-link-to-view']
            details_list = get_ticket_details(data_link_to_view)
            details = ' '.join(details_list)

            for writer in writers:
                writer.write([car_id, data_link_to_view, details])

        export_data_from_csv_to_sqlite3(csv_file, db_file, table)

        random_sleep()


if __name__ == '__main__':
    main()
