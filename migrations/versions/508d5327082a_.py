"""coluna consult_date adicionada a tabela de associação consult

Revision ID: 508d5327082a
Revises: 0afb2788c532
Create Date: 2024-07-29 12:50:11.447331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '508d5327082a'
down_revision = '0afb2788c532'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('consultations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('consult_date', sa.String(length=10), nullable=False))
        batch_op.create_foreign_key(None, 'medic', ['medic_id'], ['id'])
        batch_op.create_foreign_key(None, 'patient', ['patient_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('consultations', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('consult_date')

    # ### end Alembic commands ###
