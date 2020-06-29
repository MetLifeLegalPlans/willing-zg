from zygoat.components import Component

from .custom_server import custom_server
from .deployment import deployment
from .email import email
from .simple_jwt import simple_jwt
from .tokens import token_util


class AllComponents(Component):
    pass


# excluding custom_server for now - causes the github workflow to fail to due calling 'eb init'
all_components = AllComponents(sub_components=[deployment, email, simple_jwt, token_util])
