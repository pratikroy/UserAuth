from django_elasticsearch_dsl import Document, Index
from core.models import User



users = Index('users')
users.settings(number_of_shards=1, number_of_replicas=0)


@users.doc_type
class UserDocument(Document):
    class Django:
        model = User
        fields = ('email',)
