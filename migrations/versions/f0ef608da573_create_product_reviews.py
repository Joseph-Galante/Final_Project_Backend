"""create-product_reviews

Revision ID: f0ef608da573
Revises: 7adaf453eaf1
Create Date: 2021-05-21 11:04:57.562377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0ef608da573'
down_revision = '7adaf453eaf1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'product_reviews',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('review_id', sa.Integer),
        sa.Column('product_id', sa.Integer)
    )


def downgrade():
    op.drop_table('product_reviews')
