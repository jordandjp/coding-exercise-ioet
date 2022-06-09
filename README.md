# Coding Exercise ioet
## Overview of the solution

I developed the solution using the TDD methodology together with a pragmatic approach.

ETC, DRY, SOLID principles and orthogonality were the fundamental concepts on which I based the development of the system.

I decided to create abstractions that represents the interval of time (Timeslot) and the time of the day (DayTime). These are the fundamental abstractions, so I take advantage of the Python data model to allow higher abstractions to operate with these easily.

As well I put the data of the company table of pay rates in an external format and used an abstraction in code to represent it.

The program has the following single responsabilities:
- Present/Emit the total that the company has to pay an employee (`Handler`)
- Parse the schedule of the employees (`TimeslotParser`)
- Format the message to send (`Formatter`)
- Read the text file containing the employees' schedule (`read_txt_employee_data`)
- The domain model (`abstractions within model, daytime and timeslot modules`)
- CLI (`parse_args and main`)

In general terms I divided in a modular way the business logic, the interface, the presentation and the data.

The program interface is a CLI (main.py).


## Instructions to run locally
Requirements: python 3.7+

To run the program just run from the console:
```
python main.py
```
### Run the tests
If you are using Linux or macOS, run with the following command:
```
make test
```

For Windows users run:
```
python -m unittest discover -s tests

# If you want to run the doctests, then run
python -m doctest docs/daytime.doctest;
python -m doctest docs/timeslot.doctest
```
