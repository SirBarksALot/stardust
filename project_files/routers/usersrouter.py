from users.models import UserModel


class UsersRouter:
    route_app_labels = {'users'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'cassandra-users'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'cassandra-users'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print(f'usersrouter: app_label = {app_label}, db={db}')
        if app_label in self.route_app_labels:
            return db == 'cassandra-users'
        return None
