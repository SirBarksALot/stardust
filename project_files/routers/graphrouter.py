# from graph.models import ItemModel


class GraphRouter:
    route_app_labels = {'graph'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'cassandra-items'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'cassandra-items'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print(f'graphrouter: app_label = {app_label}, db={db}')
        if app_label in self.route_app_labels:
            return db == 'cassandra-items'
        return None
