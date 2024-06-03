"""
Ce module définit la stratégie de notification par email.
"""

from typing import List
from models.membre import Membre
from Strategies.notificationStrategy import NotificationStrategy

class EMailNotificationStrategy(NotificationStrategy):
    """
    Stratégie de notification par email.
    """

    def notifier(self, message: str, destinataires: List[Membre]):
        """
        Envoie une notification par email à une liste de destinataires.

        Args:
            message (str): Le message de la notification.
            destinataires (List[Membre]): La liste des membres à notifier.
        """
        for destinataire in destinataires:
            print(f"Notification envoyée à {destinataire.nom} par email : {message}")
