"""add_employee_table

Revision ID: 37d2096fcacf
Revises: 
Create Date: 2023-10-11 23:32:49.349605

"""
from alembic import op
import sqlalchemy as sa
import app.core


# revision identifiers, used by Alembic.
revision = '37d2096fcacf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', app.core.guid.GUID(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('number_of_leaves', sa.Integer(), nullable=True),
    sa.Column('benefits', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('contract_end_date', sa.Date(), nullable=True),
    sa.Column('project', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    # ### end Alembic commands ###
