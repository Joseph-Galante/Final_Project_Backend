"""create-cart_items

Revision ID: 1be378266701
Revises: f0ef608da573
Create Date: 2021-05-21 11:05:16.652834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1be378266701'
down_revision = 'f0ef608da573'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cart_items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('product_id', sa.Integer),
        sa.Column('order_id', sa.Integer),
        sa.Column('complete', sa.Boolean, nullable=False),
    )


def downgrade():
    op.drop_table('cart_items')
