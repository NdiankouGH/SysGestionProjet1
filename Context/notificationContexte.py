from typing import List

from Strategies.NotificationStrategy import NotificationStrategy
from models.Membre import Membre


class NotificationContext:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def notifier(self,message:str, destinataires: List[Membre]):
        for destinataire in destinataires:
            self.strategy.envoyer(message,destinataire)