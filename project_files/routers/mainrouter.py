class MainRouter:
    default_labels = {'auth', 'contenttypes'}
    cassandra_items_labels = {'graph-data'}
    cassandra_users_labels = {'users-data'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.cassandra_users_labels:
            return 'cassandra-users'
        elif model._meta.app_label in self.cassandra_items_labels:
            return 'cassandra-items'
        else:
            return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.cassandra_users_labels:
            return 'cassandra-users'
        elif model._meta.app_label in self.cassandra_items_labels:
            return 'cassandra-items'
        else:
            return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.default_labels or
            obj2._meta.app_label in self.default_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print(f'app_label = {app_label}, db={db}')
        if app_label in self.cassandra_users_labels:
            return db == 'cassandra-users'
        elif app_label in self.cassandra_items_labels:
            return db == 'cassandra-items'
        else:
            return None
