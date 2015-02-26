#!/usr/bin/env python
import logging
import time

import requests
from lxml.html import fromstring
from pync import Notifier

ENDPOINT = 'http://obmenka.kharkov.ua/'
TIMEOUT = 60
XPATH = '/html/body/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[5]'
TITLE = 'UAH per USD'


def main():
    last_currency = None

    while True:
        try:
            html = requests.get(ENDPOINT).text
            tree = fromstring(html)
            el = tree.xpath(XPATH)[0]
            value = float(el.text.replace(',', '.'))
        except Exception as e:
            logging.exception(e)
        else:
            if last_currency != value:
                try:
                    Notifier.notify(
                        TITLE,
                        open=ENDPOINT,
                        title=str(value)
                    )

                    last_currency = value
                except Exception as e:
                    logging.exception(e)
        finally:
            time.sleep(TIMEOUT)


if __name__ == '__main__':
    main()
