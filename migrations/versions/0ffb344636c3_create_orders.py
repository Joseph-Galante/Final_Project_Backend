"""create-orders

Revision ID: 0ffb344636c3
Revises: 1be378266701
Create Date: 2021-05-21 11:05:41.230325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ffb344636c3'
down_revision = '1be378266701'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('total', sa.Float, nullable=False),
        sa.Column('address', sa.String, nullable=False),
        sa.Column('city', sa.String, nullable=False),
        sa.Column('state', sa.String, nullable=False),
        sa.Column('zip', sa.String, nullable=False),
        sa.Column('card', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('orders')
