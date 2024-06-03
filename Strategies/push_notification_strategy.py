from  Strategies.notification_strategy import NotificationStrategy
from models.membre import Membre


class PushNotificationStrategy(NotificationStrategy):
    """
    Stratégie de notification pour envoyer des notifications push.

    Methods:
        notifier(message, destinataire): Envoie une notification push.
    """

    def envoyer(self, message: str, destinataire: Membre):
        """
        Envoie une notification push.

        Args:
            message (str): Le message de notification.
            destinataire (Membre): Le destinataire de la notification.
        """
        print(f"Notification envoyée à {destinataire.nom} par push : {message}")
