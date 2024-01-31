# piScan-Backend
web server for scanning system

### Dev

#### Services
```
docker compose -f docker-compose-dev.yml up
```

#### Database migrations
```
python3 migrate.py
```

#### Tests
App contains some basic tests. To run them:
```
pytest -v tests/
```
