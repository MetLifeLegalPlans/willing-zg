from willing_zg.email import Email
from willing_zg.simple_jwt import SimpleJWT
from willing_zg.tokens import TokenFile
from willing_zg.deployment import Deployment
from zygoat.components import Component
from .custom_server import CustomServer


class AllComponents(Component):
    pass


all_components = AllComponents(sub_components=[CustomServer(), Deployment(), TokenFile(), SimpleJWT(), Email()])
