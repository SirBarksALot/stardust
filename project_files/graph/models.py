import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class ItemModel(Model):
    class Meta:
        app_label = 'graph'
        db_table = 'items'

    read_repair_chance = 0.05  # optional - defaults to 0.1
    example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    description = columns.Text(required=False)
    # uuid = columns.UUID(primary_key=True, default=uuid.uuid4)
    # name = columns.Text(required=True)
    # unique_name = columns.Text(max_length=100)
    # type = columns.Text(required=False, default='basic material')
    # rarity = columns.Text(default='common')
    # craftable = columns.Boolean(required=False, default=False)
    # enchant = columns.TinyInt(default=0)
    # creation_time = columns.DateTime(required=False)
