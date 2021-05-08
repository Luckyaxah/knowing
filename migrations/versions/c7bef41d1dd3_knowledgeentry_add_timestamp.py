"""KnowledgeEntry add timestamp

Revision ID: c7bef41d1dd3
Revises: b77a8d710827
Create Date: 2021-05-08 13:59:37.415349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7bef41d1dd3'
down_revision = 'b77a8d710827'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('knowledge_entry', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('knowledge_entry', 'create_time')
    # ### end Alembic commands ###
