# from graph.models import ItemModel


class GraphRouter:
    def db_for_read(self, model, **hints):
        # if model == ItemModel:
        #     return 'cassandra-items'
        # else:
        #     return None
        return 'cassandra-items'

    def db_for_write(self, model, **hints):
        # if model == ItemModel:
        #     return 'cassandra-items'
        # else:
        #     return None
        return 'cassandra-items'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # print(app_label)
        # if app_label == 'graph':
        #     return True
        # else:
        #     return False
        return True
