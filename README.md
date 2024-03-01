# piScan
Flask based wrapper for SANE (in this case scan-image tool)

---

### Features:
- Getting connected devices + supported devices scanning options.
- Performing scans (with tracking operation progress).
- Scanned files management (download, preview, update, etc.).
- Easy setup via docker compose.
- Minimalist Flask application without usage of 3rd party plugins (adapters).
- Swagger documentation.
- Gunicorn errors/access logging.

### How to use it:
1. Setup project according to `Production Setup`.
2. Connect scanner / printer with scanner to host device USB port.
3. Use bare API requests (api docs accessible at `/docs` if `HOST_DOCS` set to `1`) or [web app](https://github.com/zNitche/piScanUI) to interact with connected devices.

### Project Goals:
The main goals of the project was to: 
- setup complete Flask app without 3rd party plugins (like `Flask-SQLAlchemy` or `Flask-Migrate`).
- add some core features like data serialization and swagger docs.
- test my own approach to flask project structure.

In the end, getting a working and functional app was a nice bonus.


### Dev Setup
1. Clone this repo.
2. Create `.env` and set needed variables.
```
cp .env.template .env
```

3. Start app services
```
docker compose -f docker-compose-dev.yml up
```

##### Extra Steps (needed during development)
- Generate swagger docs.
```
python3 generate_swagger_docs.py
```

- Run database migration.
```
python3 migrate.py
```

### Production Setup
1. Clone this repo.
2. Create `.env` and set needed variables.
```
cp .env.template .env
```

3. Run docker container.
```
sudo docker compose up -d
```

### Tests
App contains basic tests suit. To run them:
```
pytest -v tests/
```
