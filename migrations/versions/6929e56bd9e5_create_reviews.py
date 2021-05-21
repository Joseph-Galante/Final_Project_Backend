"""create-reviews

Revision ID: 6929e56bd9e5
Revises: d1241c6ed4b6
Create Date: 2021-05-21 11:03:41.877309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6929e56bd9e5'
down_revision = 'd1241c6ed4b6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String, nullable=False),
        sa.Column('rating', sa.Integer, nullable=False),
        sa.Column('user_id', sa.Integer)
    )


def downgrade():
    op.drop_table('reviews')
