from abc import ABC, abstractmethod

# Abstração para envio de mensagens
class IMessageSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Implementação concreta: envia email
class EmailSender(IMessageSender):
    def send(self, message: str):
        print(f"Enviando email: {message}")

# Implementação concreta: envia SMS
class SmsSender(IMessageSender):
    def send(self, message: str):
        print(f"Enviando SMS: {message}")

# Classe de alto nível depende da abstração, não da implementação concreta
class NotificationService:
    def __init__(self, sender: IMessageSender):
        self.sender = sender

    def notify(self, message: str):
        self.sender.send(message)

# Uso
if __name__ == "__main__":
    email_service = NotificationService(EmailSender())
    email_service.notify("Olá por email!")

    sms_service = NotificationService(SmsSender())
    sms_service.notify("Olá por SMS!")