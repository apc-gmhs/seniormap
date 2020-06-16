"""Add School model

Revision ID: 0b2dde911c33
Revises: 
Create Date: 2020-06-15 21:08:24.440388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b2dde911c33'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schools',
    sa.Column('slug', sa.String(length=16), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('form', sa.String(length=32), nullable=False),
    sa.Column('sheet', sa.String(length=64), nullable=False),
    sa.Column('background', sa.String(length=16), nullable=True),
    sa.Column('light_background', sa.String(length=16), nullable=True),
    sa.Column('lighter_background', sa.String(length=16), nullable=True),
    sa.Column('dark_background', sa.String(length=16), nullable=True),
    sa.Column('accent', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('slug'),
    sa.UniqueConstraint('form'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('sheet')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schools')
    # ### end Alembic commands ###
