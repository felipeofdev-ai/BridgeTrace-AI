import json
import uuid
from datetime import datetime
from typing import Dict, Any


class AuditLogger:
    """
    Centralized audit logger for traceability, explainability and compliance.
    """

    def __init__(self, output_path: str = "logs/audit.log"):
        self.output_path = output_path

    def log_event(
        self,
        event_type: str,
        entity_id: str,
        payload: Dict[str, Any]
    ) -> str:
        """
        Logs an auditable event.

        :param event_type: Type of event (trace, score, link, warning)
        :param entity_id: Related entity identifier
        :param payload: Arbitrary event data
        :return: Event UUID
        """

        event_id = str(uuid.uuid4())

        record = {
            "event_id": event_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event_type": event_type,
            "entity_id": entity_id,
            "payload": payload
        }

        self._write(record)
        return event_id

    def _write(self, record: Dict[str, Any]):
        with open(self.output_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
