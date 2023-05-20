"""drop passengers

Revision ID: eb716b6a9f09
Revises: 20287daca8c1
Create Date: 2023-05-20 11:00:19.288942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb716b6a9f09'
down_revision = '20287daca8c1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('passengers')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('passengers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('passenger_name', sa.VARCHAR(), nullable=True),
    sa.Column('passenger_age', sa.INTEGER(), nullable=True),
    sa.Column('plane_id', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
