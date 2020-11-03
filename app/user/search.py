from elasticsearch_dsl.query import Q, MultiMatch, SF
from user.documents import UserDocument

def get_search_query(phrase):
    query = Q(
        'function_score',
        query=MultiMatch(
            fields=['email'],
            query=phrase
        ),
    )
    return UserDocument.search().query(query)
def search(phrase):
    return get_search_query(phrase).to_queryset()
