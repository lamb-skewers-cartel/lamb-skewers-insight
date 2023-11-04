from typing import Literal, Optional

from core.models import AuditLog
from core.providers import DartProvider


class GetCompany:
    @classmethod
    def call(cls):
        DartProvider.get_company()

