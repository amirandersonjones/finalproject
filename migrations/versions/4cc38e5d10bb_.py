"""empty message

Revision ID: 4cc38e5d10bb
Revises: 697d16a95bda
Create Date: 2022-03-28 15:40:23.805358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cc38e5d10bb'
down_revision = '697d16a95bda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('username', sa.String(length=50), nullable=False))
    op.alter_column('customer', 'first_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.create_unique_constraint(None, 'customer', ['username'])
    op.drop_column('customer', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'customer', type_='unique')
    op.alter_column('customer', 'first_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.drop_column('customer', 'username')
    # ### end Alembic commands ###
