"""add planes to Route

Revision ID: 227396e5f52a
Revises: d83123a9902a
Create Date: 2023-05-20 11:15:00.347546

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String


# revision identifiers, used by Alembic.
revision = '227396e5f52a'
down_revision = 'd83123a9902a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('routes', Column('planes', String()))


def downgrade() -> None:
    pass
