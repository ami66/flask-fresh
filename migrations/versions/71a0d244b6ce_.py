"""empty message

Revision ID: 71a0d244b6ce
Revises: 6464d6f2bbcb
Create Date: 2019-10-20 13:28:57.594114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71a0d244b6ce'
down_revision = '6464d6f2bbcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('df_order_info',
    sa.Column('id', sa.String(length=125), nullable=False),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('addr', sa.Integer(), nullable=True),
    sa.Column('pay_method', sa.SmallInteger(), nullable=True),
    sa.Column('total_count', sa.Integer(), nullable=True),
    sa.Column('total_price', sa.DECIMAL(), nullable=True),
    sa.Column('transit_price', sa.DECIMAL(), nullable=True),
    sa.Column('order_status', sa.SmallInteger(), nullable=True),
    sa.Column('trade_no', sa.String(length=125), nullable=True),
    sa.ForeignKeyConstraint(['addr'], ['df_address.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('df_order_goods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order', sa.String(length=125), nullable=True),
    sa.Column('sku', sa.Integer(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('price', sa.DECIMAL(), nullable=True),
    sa.Column('comment', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['order'], ['df_order_info.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sku'], ['df_goods_sku.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('df_order_goods')
    op.drop_table('df_order_info')
    # ### end Alembic commands ###
