"""init tables

Revision ID: e21d9dc0a074
Revises: 6cbecb858b07
Create Date: 2020-03-24 10:03:42.882088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e21d9dc0a074'
down_revision = '6cbecb858b07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ih_facility_info')
    op.drop_index('mobile', table_name='ih_user_profile')
    op.drop_index('name', table_name='ih_user_profile')
    op.drop_table('ih_user_profile')
    op.drop_table('ih_house_image')
    op.drop_table('ih_house_info')
    op.drop_table('ih_house_facility')
    op.drop_index('ix_ih_order_info_status', table_name='ih_order_info')
    op.drop_table('ih_order_info')
    op.drop_table('ih_area_info')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ih_area_info',
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.Column('update_time', mysql.DATETIME(), nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('ih_order_info',
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.Column('update_time', mysql.DATETIME(), nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('house_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('begin_date', mysql.DATETIME(), nullable=False),
    sa.Column('end_date', mysql.DATETIME(), nullable=False),
    sa.Column('days', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('house_price', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('amount', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('status', mysql.ENUM('WAIT_ACCEPT', 'WAIT_PAYMENT', 'PAID', 'WAIT_COMMENT', 'COMPLETE', 'CANCELED', 'REJECTED'), nullable=True),
    sa.Column('comment', mysql.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['house_id'], ['ih_house_info.id'], name='ih_order_info_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['ih_user_profile.id'], name='ih_order_info_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_ih_order_info_status', 'ih_order_info', ['status'], unique=False)
    op.create_table('ih_house_facility',
    sa.Column('house_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('facility_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['facility_id'], ['ih_facility_info.id'], name='ih_house_facility_ibfk_1'),
    sa.ForeignKeyConstraint(['house_id'], ['ih_house_info.id'], name='ih_house_facility_ibfk_2'),
    sa.PrimaryKeyConstraint('house_id', 'facility_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('ih_house_info',
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.Column('update_time', mysql.DATETIME(), nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('area_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('price', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('address', mysql.VARCHAR(length=512), nullable=True),
    sa.Column('room_count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('acreage', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('unit', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('capacity', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('beds', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('deposit', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('min_days', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('max_days', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('order_count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('index_image_url', mysql.VARCHAR(length=256), nullable=True),
    sa.ForeignKeyConstraint(['area_id'], ['ih_area_info.id'], name='ih_house_info_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['ih_user_profile.id'], name='ih_house_info_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('ih_house_image',
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.Column('update_time', mysql.DATETIME(), nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('house_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('url', mysql.VARCHAR(length=256), nullable=False),
    sa.ForeignKeyConstraint(['house_id'], ['ih_house_info.id'], name='ih_house_image_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('ih_user_profile',
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.Column('update_time', mysql.DATETIME(), nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('mobile', mysql.VARCHAR(length=11), nullable=False),
    sa.Column('real_name', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('id_card', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('avatar_url', mysql.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'ih_user_profile', ['name'], unique=True)
    op.create_index('mobile', 'ih_user_profile', ['mobile'], unique=True)
    op.create_table('ih_facility_info',
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.Column('update_time', mysql.DATETIME(), nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
