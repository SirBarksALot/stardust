import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from django_cassandra_engine.models import DjangoCassandraModel


class UserModel(DjangoCassandraModel):
    class Meta:
        app_label = 'users-data'
        db_table = 'users-table'

    read_repair_chance = 0.05  # optional - defaults to 0.1
    uuid = columns.UUID(primary_key=True, default=uuid.uuid4)
    username = columns.Text(required=True)
