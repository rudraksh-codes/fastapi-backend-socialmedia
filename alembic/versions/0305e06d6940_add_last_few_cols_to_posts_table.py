"""add last few cols to posts table

Revision ID: 0305e06d6940
Revises: d1988444122f
Create Date: 2026-04-22 12:37:57.638888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0305e06d6940'
down_revision: Union[str, Sequence[str], None] = 'd1988444122f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'), )
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')), )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published') 
    op.drop_column('posts', 'created_at')
    pass
