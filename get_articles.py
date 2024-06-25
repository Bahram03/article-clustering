import csv
import requests
from bs4 import BeautifulSoup
from find_articles_links import read_links_from_file

def get_fields(links, base: str, writer):
    for i, link in enumerate(links):
        soup = BeautifulSoup(requests.get(link).content, 'html.parser')
        print(f"Processing article {i+1}/{len(links)}")
        # Extracting title
        try:
            title = soup.find('span', class_='article_title bold').text.strip()

            # Extracting authors
            list_a = soup.find('ul', class_='list-inline list-inline-seprator margin-bottom-6 rtl') \
                .find_all('li', class_='padding-3')
            authors = [a.find('a').text for a in list_a]

            # Extract abstract
            abstract = soup.find('div', class_='padding_abstract justify rtl').text.strip()

            # Extract keywords
            keywords = [keyword.text.strip() for keyword in
                        soup.find('ul', class_='block list-inline list-inline-seprator margin-bottom-6 rtl').find_all('li')]

            # Extract link
            link = soup.find('ul', class_='list-group list-group-bordered list-group-noicon nomargin').find_all('a')[1].get(
                'href')
            link = f'{base}{link[1:]}'
        except AttributeError:
            print(f"Skipping article {i+1} due to missing information")
            continue
        
        article_crawled = {
            'Title': title,
            'Authors': authors,
            'Link': link,
            'Abstract': abstract,
            'Keywords': keywords
        }
        writer.writerow(article_crawled)

if __name__ == '__main__':
    csv_filename = 'assets/crawled_articles.csv'
    article_links_filename = 'assets/article_links.txt'
    
    with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Authors', 'Link', 'Abstract', 'Keywords']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        base_url = "https://jte.ut.ac.ir"
        articles_links = read_links_from_file(article_links_filename)
        get_fields(articles_links, base_url, writer)
