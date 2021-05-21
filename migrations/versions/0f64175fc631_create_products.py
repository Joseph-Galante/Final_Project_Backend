"""create-products

Revision ID: 0f64175fc631
Revises: 6929e56bd9e5
Create Date: 2021-05-21 11:04:13.810168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f64175fc631'
down_revision = '6929e56bd9e5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False),
        sa.Column('user_id', sa.Integer)
    )


def downgrade():
    op.drop_table('products')
