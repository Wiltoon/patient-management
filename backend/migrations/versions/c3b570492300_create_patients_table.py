"""create patients table

Revision ID: c3b570492300
Revises: aca813582bf5
Create Date: 2025-01-16 00:03:13.634587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3b570492300'
down_revision: Union[str, None] = 'aca813582bf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
