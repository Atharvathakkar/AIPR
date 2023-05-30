% Flights
flight(flight1, 'Source1', 'Destination1', '10:00', '12:00').
flight(flight2, 'Source2', 'Destination2', '14:30', '16:45').
flight(flight3, 'Source3', 'Destination3', '09:15', '11:20').
flight(flight4, 'Source4', 'Destination4', '17:00', '19:30').

% Cargo
cargo(cargo1, 'Source1', 'Destination1', '08:00').
cargo(cargo2, 'Source2', 'Destination2', '13:45').
cargo(cargo3, 'Source3', 'Destination3', '10:30').
cargo(cargo4, 'Source4', 'Destination4', '16:15').

scheduled_flight(Flight) :-
    flight(Flight, _, _, _, _),
    write_flight_details(Flight),
    nl,
    fail.
scheduled_flight(_) :- true.

scheduled_cargo(Cargo) :-
    cargo(Cargo, _, _, _),
    write_cargo_details(Cargo),
    nl,
    fail.
scheduled_cargo(_) :- true.

write_flight_details(Flight) :-
    flight(Flight, Source, Destination, StartTime, EndTime),
    write('Flight: '), write(Flight),
    write(', Source: '), write(Source),
    write(', Destination: '), write(Destination),
    write(', StartTime: '), write(StartTime),
    write(', EndTime: '), write(EndTime).

write_cargo_details(Cargo) :-
    cargo(Cargo, Source, Destination, StartTime),
    write('Cargo: '), write(Cargo),
    write(', Source: '), write(Source),
    write(', Destination: '), write(Destination),
    write(', StartTime: '), write(StartTime).


% Example rule: Get flights between given source and destination
flight_between(Source, Destination, Flight) :-
    flight(Flight, Source, Destination, _, _).

% Example rule: Get cargo shipments between given source and destination
cargo_between(Source, Destination, Cargo) :-
    cargo(Cargo, Source, Destination, _).

% Example rule: Get flights departing after a given time
flights_departing_after(Time, Flight) :-
    flight(Flight, _, _, DepartureTime, _),
    time_greater_than(DepartureTime, Time).

% Example rule: Get cargo shipments starting after a given time
cargo_starting_after(Time, Cargo) :-
    cargo(Cargo, _, _, StartTime),
    time_greater_than(StartTime, Time).

% Auxiliary rule: Compare two times in HH:MM format
time_greater_than(Time1, Time2) :-
    time_string(Time1, Time1HHMM),
    time_string(Time2, Time2HHMM),
    Time1HHMM @> Time2HHMM.

