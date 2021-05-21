"""create-users

Revision ID: d1241c6ed4b6
Revises: 
Create Date: 2021-05-21 11:03:06.050896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1241c6ed4b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('users')
