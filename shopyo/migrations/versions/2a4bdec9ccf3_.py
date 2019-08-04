"""empty message

Revision ID: 2a4bdec9ccf3
Revises: 
Create Date: 2019-08-04 11:59:44.996042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a4bdec9ccf3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.String(length=100), nullable=True),
    sa.Column('about', sa.String(length=100), nullable=True),
    sa.Column('social_media', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('people')
    # ### end Alembic commands ###