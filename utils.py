import requests

from config import NEWS_API_BASE_URL
from models import Article


class NewsFetcher:
    base_url = NEWS_API_BASE_URL
    image_media_types = ['image', 'media']

    def fetch_articles(self):
        articles = []
        articles_url = f"{self.base_url}/data/list.json"
        response = requests.get(articles_url)
        articles_data = response.json()
        for article_data in articles_data:
            image_media_data = {}
            details_data = self.fetch_article_details(article_data.get('id'))
            if details_data:
                sections = details_data.get('sections')
                image_media_data = self.get_image_media_date(sections)
                article_data.update(details_data)

            if image_media_data:
                media_data = self.fetch_article_media(article_data.get('id'))
                for section in media_data:
                    section_id = section.get('id')
                    section_index = image_media_data[section_id]
                    article_data['sections'][section_index] = section

            articles.append(Article(**article_data))

        return articles

    def fetch_article_details(self, article_id: str):
        article_detail_url = f"{self.base_url}/data/articles/{article_id}.json"
        response = requests.get(article_detail_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {}

    def fetch_article_media(self, article_id: str):
        article_media_url = f"{self.base_url}/data/media/{article_id}.json"
        response = requests.get(article_media_url)
        if response.status_code == 200:
            return response.json()
        else:
            return []

    def get_image_media_date(self, sections):
        image_media_dict = {}
        for index, section in enumerate(sections):
            if section.get('type') in self.image_media_types:
                image_media_dict[section.get('id')] = index

        return image_media_dict
