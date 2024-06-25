import requests  
from bs4 import BeautifulSoup  

def get_volumes(base):
    # get and parse the main page to extract volume links
    page = requests.get(base).content
    page_soup = BeautifulSoup(page, 'html.parser')
    volume_holders = page_soup.find_all('div', class_='card-header bold')
    # construct full URLs for each volume link
    links = [f'{base}' + str(volume.find_all('a')[1]['href'])[1:] for volume in volume_holders]
    return links

def get_issues(base):
    # get and parse each volume page to extract issue links
    issues_list = []
    for volume in get_volumes(base):
        volume_page = BeautifulSoup(requests.get(volume).content, 'html.parser')
        issue_holders = volume_page.find_all('div', class_='issue_dv')
        # extract the issue links from each volume page
        issues_list.extend([issue.find('a').get('href') for issue in issue_holders])
    # construct full URLs for each issue link
    issues_list = [f'{base}' + '/' + str(i) for i in issues_list]
    return issues_list

def save_links_to_file(links, filename):
    # save the list of links to a file in the assets folder
    links_text = '\n'.join(links)
    with open(f'assets/{filename}', 'w') as file:
        file.write(links_text)

def read_links_from_file(filename):
    # read links from a file in the assets folder
    with open(f'assets/{filename}', 'r') as file:
        links = [line.strip() for line in file]
    return links

def find_article(links):
    # get and parse each issue page to extract article links
    articles_list = []
    for link in links:
        issue_page = requests.get(link).content
        issue_soup = BeautifulSoup(issue_page, 'html.parser')
        print(link)  # print the current link being processed
        current_articles_links = issue_soup.find_all('h5', class_='margin-bottom-6 list-article-title rtl')
        # extract the article links from each issue page
        articles_list.extend([article.find('a').get('href') for article in current_articles_links])
    # construct full URLs for each article link
    articles_list = [f'{base}' + '/' + str(i) for i in articles_list]
    return articles_list

if __name__ == '__main__':
    base = 'https://jte.ut.ac.ir'  # base URL of the website
    list_text = 'links.txt'  # filename for saving issue links
    save_links_to_file(get_issues(base), list_text)  # get issues and save to file
    issues_file_name = 'links.txt'  # filename for reading issue links
    links = read_links_from_file(issues_file_name)  # read issue links from file
    articles_file_name = 'article_links.txt'  # filename for saving article links
    save_links_to_file(find_article(links), articles_file_name)  # find articles and save to file
