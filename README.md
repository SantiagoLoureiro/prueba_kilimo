# Kilimo - Rest Api


## Installation

First, install requeriments.

```bash
pip install -r requeriment.txt
```

For initialize database

```bash
python manage.py migrate
```


## Load Data in DB

```bash
python manage.py loaddata settings/fixture/data.json
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
field.tests.test_field_rain_view.test
```


Objetive 2

```bash
Listado de campos donde la lluvia acumulada es mayor a N, donde N
es un número en milímetros.
```

Test

```bash
field.tests.test_field_rain_view.test
```

Objetive 3

```bash
Listado de lluvias por campo.
```

Test

```bash
rain.test_rain_view.test
```

Objetive 4

```bash
Creación de lluvia por campo.
```

Test

```bash
rain.test_rain_view.test
```

