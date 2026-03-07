## Docker

- `docker build -t analytic-api -f DockerFile.web .`
- `docker run -p 8000:8000 analytic-api`

<!--container auto deletes when stopped -> Very convenient for testing

    docker run --rm -p 8000:8000 analytic-api
-->

becomes

- `docker compose up --watch`
- `docker compose down` or `docker compose down -v` (to remove volumes)
- `docker compose run app /bin/bash` or `docker compose run app python`
