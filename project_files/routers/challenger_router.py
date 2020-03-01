class ChallengerRouter:
    route_app_labels = {'challenger'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            print(model._meta.app_label)
            return 'challenger_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            print(model._meta.app_label)
            return 'challenger_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            print(app_label)
            return db == 'challenger_db'
        return None
