"""add airline and route to Plane

Revision ID: f03129ad87b0
Revises: 227396e5f52a
Create Date: 2023-05-20 11:22:57.518759

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String


# revision identifiers, used by Alembic.
revision = 'f03129ad87b0'
down_revision = '227396e5f52a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('planes', Column('airline', String()))
    op.add_column('planes', Column('route', String()))


def downgrade() -> None:
    op.drop_column('planes', Column('airline'))
    op.drop_column('planes', Column('route'))
    op.drop_column('routes', Column('planes'))
