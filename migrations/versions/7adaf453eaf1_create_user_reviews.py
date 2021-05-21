"""create-user_reviews

Revision ID: 7adaf453eaf1
Revises: 0f64175fc631
Create Date: 2021-05-21 11:04:39.879037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7adaf453eaf1'
down_revision = '0f64175fc631'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_reviews',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('review_id', sa.Integer),
    )


def downgrade():
    op.drop_table('user_reviews')
