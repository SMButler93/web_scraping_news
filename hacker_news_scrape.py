"""A web scraping script that shows articles from Hacker news,
only if they have recieved 100 or more points. This is then presented
in order with the article with the most points being shown first."""

import pprint
import requests
from bs4 import BeautifulSoup

# create response:
res = requests.get('https://news.ycombinator.com/news')
# soup object:
soup = BeautifulSoup(res.text, 'html.parser')
# select the links and the subtext which contains the points.
links = soup.select('.titlelink')
subtext = soup.select('.subtext')


def sort_by_vote(news_list):
    """sorts the news from highest to lowest points."""
    return sorted(news_list, key=lambda k: k['votes'], reverse=True)


def create_custom_news(link_list, subtext_list):
    """iterates through articles and collates data on them and then displays
    this data if it meets requirements set."""
    news = []
    # iterate through links:
    # enumerate used to link items in different lists together:
    for index, item in enumerate(link_list):
        title = item.getText()
        # collect href if there is one:
        href = item.get('href', None)
        # gather score on each article:
        vote = subtext_list[index].select('.score')
        # if a score exists, run i through conditional statement:
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                news.append({'title': title, 'link': href, 'votes': points})
    # return the info through the sort_by_vote function to organise in a clean logical way:
    return sort_by_vote(news)


# use pretty print to display data in a clean and readable way.
pprint.pprint(create_custom_news(links, subtext))
