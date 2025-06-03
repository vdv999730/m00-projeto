import pytest
from app.services.audit_service import log_event
from sqlalchemy import select
from app.models.audit import AuditLog


@pytest.mark.asyncio
async def test_log_event(async_session):
    # Chama diretamente o log_event para garantir que a função está coberta
    await log_event(
        async_session, user_id=1, action="TEST_ACTION", details="Test details"
    )

    result = await async_session.execute(
        select(AuditLog).where(AuditLog.action == "TEST_ACTION")
    )
    log_entry = result.scalars().first()

    assert log_entry is not None
    assert log_entry.action == "TEST_ACTION"
    assert log_entry.details == "Test details"
