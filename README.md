# kibblepi

This project is ...
Internship project ...

It is splited in several part...
Architecture schema...

## Raspberry server

### Setup env
Install pyenv, python 3.10.2 and pyenv virtualenv.
Then create a venv:
```
pyenv virtualenv venv_kibblepi
pyenv activate venv_kibblepi
pip install -e pi_server/.[dev]
```
Run the test with:
```
make test
```
Launch the server
```
run_server
```

## Streamlit webapp

## TODO


# Some example of md template:

# *[short title of solved problem and solution]*

**User Story:** *[ticket/issue-number]* <!-- optional -->

*[context and problem statement]*
*[decision drivers | forces]* <!-- optional -->

## Considered Alternatives

* *[alternative 1]*
* *[alternative 2]*
* *[alternative 3]*
* *[...]* <!-- numbers of alternatives can vary -->

## Decision Outcome

* Chosen Alternative: *[alternative 1]*
* *[justification. e.g., only alternative, which meets KO criterion decision driver | which resolves force force | ... | comes out best (see below)]*
* *[consequences. e.g., negative impact on quality attribute, follow-up decisions required, ...]* <!-- optional -->

## Pros and Cons of the Alternatives <!-- optional -->

### *[alternative 1]*

* `+` *[argument 1 pro]*
* `+` *[argument 2 pro]*
* `-` *[argument 1 con]*
* *[...]* <!-- numbers of pros and cons can vary -->

### *[alternative 2]*

* `+` *[argument 1 pro]*
* `+` *[argument 2 pro]*
* `-` *[argument 1 con]*
* *[...]* <!-- numbers of pros and cons can vary -->

### *[alternative 3]*

* `+` *[argument 1 pro]*
* `+` *[argument 2 pro]*
* `-` *[argument 1 con]*
* *[...]* <!-- numbers of pros and cons can vary -->