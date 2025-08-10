from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('tenants',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('domains', sa.JSON, nullable=False, server_default='[]'),
        sa.Column('currency', sa.String, server_default='ARS'),
        sa.Column('locale', sa.String, server_default='es-AR'),
        sa.Column('timezone', sa.String, server_default='America/Argentina/Buenos_Aires'),
        sa.Column('theme', sa.String, server_default='default')
    )
    op.create_table('users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('password_hash', sa.String, nullable=False),
        sa.Column('role', sa.String, server_default='customer'),
        sa.Column('tenant_id', sa.Integer, sa.ForeignKey('tenants.id')),
        sa.Column('is_active', sa.Boolean, server_default='t')
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('tenants')
