import yaml
import click


class Project(yaml.YAMLObject):
    """Class corresponding to a Project.

    :param name: The name of the project.
    :type name: str
    :param description: The description of the project.
    :type description: str
    :param website: The url of the project.
    :type website: str
    """

    yaml_tag = u"Project"

    def __init__(self, name, description, website):
        self.name = name
        self.description = description
        self.website = website

    @staticmethod
    def ask():
        """Interacively create the Projects section of a resume.

        :returns: A list of Project objects

        """
        projects = []
        continue_adding = True
        correct = False
        while not correct:
            while continue_adding:
                name = click.prompt("Name")
                description = click.prompt("Description")
                website = click.prompt("URL (optional)", default="")
                projects.append(Project(name, description, website))
                continue_adding = click.confirm("Add a new project?")
            correct = click.confirm("Is this correct?")
        return projects

    @staticmethod
    def load(data):
        """Load dictionary and returns a Project object.

        :param data: A dictionary loaded from a yaml file.
        :type data: dict[]
        :returns: A Project object.

        """
        return Project(data.get("name"), data.get("description"), data.get("website"))
