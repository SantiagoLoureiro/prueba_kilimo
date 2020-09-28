# Kilimo - Rest Api


## Installation

Install requeriments.

```bash
pip install -r requeriments.txt
```

For initialize database

```bash
python manage.py migrate
```


## Load Data in DB

```bash
python manage.py loaddata settings/fixtures/data.json
```


## Test


The tests demonstrate the application objetives.
For run test use:
```bash
pytest
```

Objetive 1 

```bash
Listado de campos con su promedio de lluvia en los últimos N días,
donde N puede ser cualquier cantidad de días con un tope de 7.
```

Test

```bash
field.tests.views.test_field_rain_view.test_rain_by_days_ago_rain_200
field.tests.views.test_field_rain_view.test_rain_get_by_days_ago_rain_400
```


Objetive 2

```bash
Listado de campos donde la lluvia acumulada es mayor a N, donde N
es un número en milímetros.
```

Test

```bash
field.tests.views.test_field_rain_view.test_rain_get_none_by_quantity_200
field.tests.views.test_field_rain_view.test_rain_by_quantity_200
```

Objetive 3

```bash
Listado de lluvias por campo.
```

Test

```bash
rain.tests.views.test_rain_view.test_rain_view_get_status_200
```

Objetive 4

```bash
Creación de lluvia por campo.
```

Test

```bash
rain.tests.views.test_rain_view.test_rain_view_post_status_200
rain.tests.views.test_rain_view.test_rain_view_post_status_400
```

## Authentication

For admin panel, te default user is: (if before run loaddata command)

  - Username: Admin
  - Password: 1
  
## CI

Proyect have CI for run test and validate pep8 in

```bash
.github/workflows/pytest.yml
```
