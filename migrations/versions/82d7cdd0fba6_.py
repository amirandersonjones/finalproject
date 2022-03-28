"""empty message

Revision ID: 82d7cdd0fba6
Revises: 
Create Date: 2022-03-27 11:07:02.874762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82d7cdd0fba6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.BIGINT(), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer')
    # ### end Alembic commands ###
