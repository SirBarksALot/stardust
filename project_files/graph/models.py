import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class ItemModel(DjangoCassandraModel):
    class Meta:
        app_label = 'graph-data'
        db_table = 'items-table'

    read_repair_chance = 0.05  # optional - defaults to 0.1
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text(required=True)
    unique_name = columns.Text(max_length=100)
    rarity = columns.Text(default='common')
    type = columns.Text(required=False, default='basic material')
    craftable = columns.Boolean(required=False, default=False)
    description = columns.Text(required=False)
    creation_time = columns.DateTime(required=False)
