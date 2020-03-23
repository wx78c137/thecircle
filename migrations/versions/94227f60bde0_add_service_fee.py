"""add service fee

Revision ID: 94227f60bde0
Revises: 9dfa14784b1b
Create Date: 2020-03-22 19:31:45.283273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94227f60bde0'
down_revision = '9dfa14784b1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('service_fee', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_post', 'service_fee')
    # ### end Alembic commands ###