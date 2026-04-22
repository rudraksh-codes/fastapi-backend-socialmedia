"""add foreign key to posts table

Revision ID: d1988444122f
Revises: d367f844b91d
Create Date: 2026-04-22 12:13:14.404081

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1988444122f'
down_revision: Union[str, Sequence[str], None] = 'd367f844b91d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass

def downgrade() -> None:
    op.execute("ALTER TABLE posts DROP CONSTRAINT IF EXISTS posts_users_fk")
    op.execute("ALTER TABLE posts DROP COLUMN IF EXISTS owner_id")