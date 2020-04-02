# shopee-scraper

Shopee data scraping for category

## Requirment

- Python3

## Installation

- Install python module using `pip`

    ```sh
    pip3 install -r requirment.txt
    ```

- Edit `config.yaml` file according to usage

    Example :

    ```yaml
    max-page: 10
    data-per-page: 50
    full-url: 'https://shopee.co.id/Pakaian-Pria-cat.33'
    webdriver-path: path/to/web/driver
    file-store-location: data/
    ```

## Usage

```sh
python3 scrap.py
```
