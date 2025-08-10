# Webecommers SaaS

Proyecto monorepo de eCommerce multi-tenant. Incluye backend FastAPI, storefront y panel admin en Next.js, base de datos PostgreSQL, Redis, Meilisearch y Nginx para archivos estáticos.

## Requisitos
- Docker y Docker Compose
- Make

## Uso

Copiar `.env.example` a `.env` y modificar según necesidad.

```bash
make bootstrap
make migrate
make seed
make up
```

Backend disponible en `http://localhost:8000`. Storefront en `http://localhost:3000`. Admin en `http://localhost:3001`.

### Subdominios
Para correr en local se usa `{tenant}.localhost`. Agregar entradas en `/etc/hosts`:
```
127.0.0.1 demo.localhost
```

### Nginx en VPS
El archivo `infra/nginx/nginx.conf` contiene ejemplo de configuración para servir archivos estáticos desde `/var/app/static` y `/var/app/media`.

### Backups
- DB: `docker exec -t db pg_dump -U postgres webecommers > backup.sql`
- Media: copiar volumen `app_media`

### Flujo básico
1. Crear producto desde el panel admin
2. Subir imágenes
3. Publicar en la tienda
4. Cliente compra y se genera orden
5. Exportar reporte desde admin

