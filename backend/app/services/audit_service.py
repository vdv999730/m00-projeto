# backend/app/services/audit_service.py

from app.models.audit import AuditLog
from sqlalchemy.ext.asyncio import AsyncSession


async def log_event(db: AsyncSession, user_id: int, action: str, details: str = None):
    audit_log = AuditLog(user_id=user_id, action=action, details=details)
    db.add(audit_log)
    await db.commit()
    await db.refresh(audit_log)
    return audit_log
