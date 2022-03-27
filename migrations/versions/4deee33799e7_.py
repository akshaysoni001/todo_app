"""empty message

Revision ID: 4deee33799e7
Revises: 268bb7f87621
Create Date: 2022-03-25 20:01:31.224203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4deee33799e7'
down_revision = '268bb7f87621'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo_projects', sa.Column('content', sa.String(length=800), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo_projects', 'content')
    # ### end Alembic commands ###
