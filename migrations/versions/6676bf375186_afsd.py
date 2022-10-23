"""afsd

Revision ID: 6676bf375186
Revises: 20a4c424baa3
Create Date: 2022-10-04 17:16:00.325418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6676bf375186'
down_revision = '20a4c424baa3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rubric',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.Column('rubric_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rubric_id'], ['rubric.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tags', sa.String(length=120), nullable=False),
    sa.Column('rubric_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['rubric_id'], ['rubric.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skill_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['skill_id'], ['skill.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('skill_category')
    op.drop_table('skill')
    op.drop_table('category')
    op.drop_table('rubric')
    # ### end Alembic commands ###
