import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class UserModel(Model):
    class Meta:
        app_label = 'users'
        db_table = 'users'

    read_repair_chance = 0.05  # optional - defaults to 0.1
    uuid = columns.UUID(primary_key=True, default=uuid.uuid4)
    username = columns.Text(required=True)
    # password = columns.Text()
    # email = columns.Text(required=True)
