"""updates time

Revision ID: 1e14ee56fce8
Revises: 8e781c266eb6
Create Date: 2018-09-15 16:50:00.694502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e14ee56fce8'
down_revision = '8e781c266eb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_comments_date_created'), 'comments', ['date_created'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_date_created'), table_name='comments')
    # ### end Alembic commands ###
