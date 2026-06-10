#!/bin/bash
# Contabo Debian VPS — Portfolio deployment script
# Run as root: bash setup.sh

set -e

PROJECT_DIR="/home/portfolio/Portfolio"
DOMAIN="yourdomain.com"   # <-- o'zgartiring

echo "==> System update"
apt update && apt upgrade -y
apt install -y python3 python3-pip python3-venv postgresql postgresql-contrib nginx certbot python3-certbot-nginx git

echo "==> Create system user"
id -u portfolio &>/dev/null || useradd -m -s /bin/bash portfolio

echo "==> Setup PostgreSQL"
sudo -u postgres psql -c "CREATE DATABASE portfolio_db;" 2>/dev/null || true
sudo -u postgres psql -c "CREATE USER portfolio_user WITH PASSWORD 'CHANGE_THIS_PASSWORD';" 2>/dev/null || true
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE portfolio_db TO portfolio_user;" 2>/dev/null || true

echo "==> Clone & setup project"
sudo -u portfolio git clone https://github.com/YOUR_USERNAME/Portfolio.git $PROJECT_DIR
cd $PROJECT_DIR
sudo -u portfolio python3 -m venv venv
sudo -u portfolio venv/bin/pip install -r requirements.txt

echo "==> Create log directory"
mkdir -p /var/log/portfolio
chown portfolio:www-data /var/log/portfolio

echo "==> Configure .env  (edit manually!)"
cat > $PROJECT_DIR/.env << 'EOF'
SECRET_KEY=GENERATE_A_SECURE_KEY_HERE
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_NAME=portfolio_db
DB_USER=portfolio_user
DB_PASSWORD=CHANGE_THIS_PASSWORD
DB_HOST=localhost
DB_PORT=5432
EOF

echo "==> Migrate & collectstatic"
sudo -u portfolio venv/bin/python manage.py migrate
sudo -u portfolio venv/bin/python manage.py collectstatic --noinput

echo "==> Install systemd service"
cp deploy/portfolio.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable portfolio
systemctl start portfolio

echo "==> Configure Nginx"
cp deploy/nginx.conf /etc/nginx/sites-available/portfolio
sed -i "s/yourdomain.com/$DOMAIN/g" /etc/nginx/sites-available/portfolio
ln -sf /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl reload nginx

echo "==> SSL certificate (Let's Encrypt)"
certbot --nginx -d $DOMAIN -d www.$DOMAIN --non-interactive --agree-tos -m admin@$DOMAIN

echo ""
echo "✓ Deployment complete!"
echo "  Site: https://$DOMAIN"
echo "  Admin: https://$DOMAIN/admin/"
echo ""
echo "  Create superuser: cd $PROJECT_DIR && sudo -u portfolio venv/bin/python manage.py createsuperuser"
