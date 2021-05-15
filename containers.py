from dependency_injector import providers, containers

from client import Client
#from consumer import Consumer
from object_manager import ObjectManager


#
# Dependency injection classes
#


class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')


# class Consumers(containers.DeclarativeContainer):
#     consumer = providers.Factory(Consumer, Configs.config)


class Clients(containers.DeclarativeContainer):
    client = providers.Singleton(Client)


class Managers(containers.DeclarativeContainer):
    object_manager = providers.Singleton(ObjectManager, Clients.client)
