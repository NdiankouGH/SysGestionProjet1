"""
Ce module définit la stratégie de notification par SMS.
"""

from typing import List
from models.membre import Membre
from Strategies.notification_strategy import NotificationStrategy

class SMSNotificationStrategy(NotificationStrategy):
    """
    Stratégie de notification par SMS.
    """

    def notifier(self, message: str, destinataires: List[Membre]):
        """
        Envoie une notification par SMS à une liste de destinataires.

        Args:
            message (str): Le message de la notification.
            destinataires (List[Membre]): La liste des membres à notifier.
        """
        for destinataire in destinataires:
            print(f"Notification envoyée à {destinataire.nom} par SMS : {message}")
