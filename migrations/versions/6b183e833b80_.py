"""empty message

Revision ID: 6b183e833b80
Revises: 
Create Date: 2024-05-13 01:20:39.984514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b183e833b80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hotel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('descripcion', sa.String(length=250), nullable=False),
    sa.Column('duracion', sa.String(length=250), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('imageURL', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paquete',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('destino', sa.String(length=500), nullable=False),
    sa.Column('descripcion', sa.String(length=500), nullable=False),
    sa.Column('duracion', sa.String(length=500), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('imageURL', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tour',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('descripcion', sa.String(length=500), nullable=False),
    sa.Column('duracion', sa.String(length=500), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('imageURL', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('reserva',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fecha_inicio', sa.DateTime(), nullable=False),
    sa.Column('fecha_final', sa.DateTime(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_tour', sa.Integer(), nullable=True),
    sa.Column('id_paquete', sa.Integer(), nullable=True),
    sa.Column('id_hotel', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_hotel'], ['hotel.id'], ),
    sa.ForeignKeyConstraint(['id_paquete'], ['paquete.id'], ),
    sa.ForeignKeyConstraint(['id_tour'], ['tour.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reserva')
    op.drop_table('user')
    op.drop_table('tour')
    op.drop_table('paquete')
    op.drop_table('hotel')
    # ### end Alembic commands ###
