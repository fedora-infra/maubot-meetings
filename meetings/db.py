from __future__ import annotations

from mautrix.util.async_db import UpgradeTable, Connection

upgrade_table = UpgradeTable()

@upgrade_table.register(description="Initial revision")
async def upgrade_v1(conn: Connection) -> None:
  await conn.execute(
    """CREATE TABLE meetings (
         room_id TEXT PRIMARY KEY,
         meeting_id TEXT NOT NULL
    )"""
  )
  await conn.execute(
    """CREATE TABLE meeting_logs (
         meeting_id TEXT NOT NULL,
         timestamp TEXT NOT NULL,
         sender TEXT NOT NULL,
         message TEXT NOT NULL,
         tag TEXT DEFAULT NULL
    )"""
  )