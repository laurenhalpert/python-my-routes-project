"""delete plane_id

Revision ID: 20287daca8c1
Revises: 0fe794df69cd
Create Date: 2023-05-20 10:31:19.388600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20287daca8c1'
down_revision = '0fe794df69cd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('passengers', 'plane_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('passengers', sa.Column('plane_id', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
