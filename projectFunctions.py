class ProjectAssistant:
    def __init__(self):
        self.projects = {}

    def create_project(self, name, description):
        self.projects[name] = description

    def list_projects(self):
        return self.projects.keys()

    def view_project(self, name):
        return self.projects.get(name, "Project not found")

    def update_project(self, name, description):
        if name in self.projects:
            self.projects[name] = description
        else:
            return "Project not found"

    def delete_project(self, name):
        if name in self.projects:
            del self.projects[name]
        else:
            return "Project not found"