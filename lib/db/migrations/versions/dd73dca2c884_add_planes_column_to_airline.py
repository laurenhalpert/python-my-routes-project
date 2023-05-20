"""add planes column to Airline

Revision ID: dd73dca2c884
Revises: f03129ad87b0
Create Date: 2023-05-20 11:28:18.095708

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String


# revision identifiers, used by Alembic.
revision = 'dd73dca2c884'
down_revision = 'f03129ad87b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('airlines', Column('planes', String()))


def downgrade() -> None:
    op.drop_column('airlines', Column('planes', String()))
