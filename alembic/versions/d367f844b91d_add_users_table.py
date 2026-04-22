"""add users table

Revision ID: d367f844b91d
Revises: 54089d9e8b9e
Create Date: 2026-04-22 12:02:43.599535

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd367f844b91d'
down_revision: Union[str, Sequence[str], None] = '54089d9e8b9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable = False), 
                    sa.Column('email', sa.String(), nullable= False), 
                    sa.Column('password', sa.String(), nullable=False), 
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable = False),
                    sa.PrimaryKeyConstraint('id'), 
                    sa.UniqueConstraint('email')
                    ) 

    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
