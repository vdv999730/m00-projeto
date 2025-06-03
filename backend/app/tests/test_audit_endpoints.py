import pytest
from sqlalchemy import select
from app.services.audit_service import log_event
from app.models.audit import AuditLog


@pytest.mark.asyncio
async def test_log_event_creation(async_session):
    """
    Testa a criação de um log de auditoria usando a função log_event.
    """
    await log_event(
        async_session,
        user_id=123,
        action="TEST_ACTION",
        details="This is a test log entry",
    )

    result = await async_session.execute(
        select(AuditLog).where(AuditLog.action == "TEST_ACTION")
    )
    log_entry = result.scalars().first()

    assert log_entry is not None
    assert log_entry.user_id == 123
    assert log_entry.action == "TEST_ACTION"
    assert log_entry.details == "This is a test log entry"
