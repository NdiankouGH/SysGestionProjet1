"""
Ce module définit l'interface de la stratégie de notification.
"""

from abc import ABC, abstractmethod
from typing import List
from models.membre import Membre

class NotificationStrategy(ABC):
    """
    Interface pour les stratégies de notification.
    """

    @abstractmethod
    def notifier(self, message: str, destinataires: List[Membre]):
        """
        Méthode abstraite pour envoyer une notification à plusieurs destinataires.

        Args:
            message (str): Le message de la notification.
            destinataires (List[Membre]): La liste des membres à notifier.
        """
        pass
