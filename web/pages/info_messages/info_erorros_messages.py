# Ошибки или информационные сообщения на страницах
from dataclasses import dataclass, field


@dataclass(frozen=True)
class AuthorizationPageMessages:
    error_user_blocked: str = "Epic sadface: Sorry, this user has been locked out."


@dataclass(frozen=True)
class Messages:
    auth_page: AuthorizationPageMessages = field(
        default_factory=AuthorizationPageMessages
    )


messages = Messages()
