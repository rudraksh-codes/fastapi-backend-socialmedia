"""create posts table

Revision ID: c6a169a5045a
Revises: 
Create Date: 2026-04-22 11:23:35.680560

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6a169a5045a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', 
        sa.Column('id', sa.Integer, nullable=False, primary_key=True), 
        sa.Column('title', sa.String(), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
