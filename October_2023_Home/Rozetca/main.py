from Hellel.October_2023_Home.Rozetca import scraping


def main():
    products = scraping.collect_products()
    print(products)


if __name__ == '__main__':
    main()