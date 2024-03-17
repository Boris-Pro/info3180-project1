"""empty message

Revision ID: 24b4b633620a
Revises: cd023c1c0113
Create Date: 2024-03-17 12:00:40.788440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24b4b633620a'
down_revision = 'cd023c1c0113'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.alter_column('property_title',
               existing_type=sa.VARCHAR(length=300),
               type_=sa.String(length=400),
               existing_nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=400),
               type_=sa.String(length=800),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=800),
               type_=sa.VARCHAR(length=400),
               existing_nullable=True)
        batch_op.alter_column('property_title',
               existing_type=sa.String(length=400),
               type_=sa.VARCHAR(length=300),
               existing_nullable=True)

    # ### end Alembic commands ###