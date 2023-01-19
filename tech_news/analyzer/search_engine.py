from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    return [
        (news["title"], news["url"])
        for news in search_news({"title": {"$regex": title, "$options": "i"}})
    ]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        valid_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        return [
            (news["title"], news["url"])
            for news in search_news({"timestamp": {"$eq": valid_date}})
        ]


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    return [
        (news["title"], news["url"])
        for news in search_news({"tags": {"$regex": tag, "$options": "i"}})
    ]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    return [
        (news["title"], news["url"])
        for news in search_news(
            {"category": {"$regex": category, "$options": "i"}})
    ]
