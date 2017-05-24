"""empty message

Revision ID: 62483dc66a43
Revises: fad5638d207c
Create Date: 2017-05-22 20:00:57.962509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62483dc66a43'
down_revision = 'fad5638d207c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
