"""add content column

Revision ID: 54089d9e8b9e
Revises: c6a169a5045a
Create Date: 2026-04-22 11:40:57.289112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54089d9e8b9e'
down_revision: Union[str, Sequence[str], None] = 'c6a169a5045a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String() ,nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    
