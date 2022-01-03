-module(day1).

-behaviour(day).

-export([
    day/0,
    part1/1,
    part2/1,
    part1_line_parse/1,
    part2_line_parse/1
]).

day() ->
    "1".

part1_line_parse(Line) ->
    list_to_integer(Line).

part1(Data) ->
    part1(Data, 0).

part1([Value, Next|Tail], Sum) when Next > Value ->
    part1([Next|Tail], Sum + 1);
part1([_, Next|Tail], Sum) ->
    part1([Next|Tail], Sum);
part1([_], Sum) ->
    Sum.

part2_line_parse(Line) ->
    list_to_integer(Line).

part2(Data) ->
    part2(Data, 0).

part2([N1, N2, N3, N4 | Tail], Sum) when (N2 + N3 + N4) > (N1 + N2 + N3) ->
    part2([N2, N3, N4] ++ Tail, Sum + 1);
part2([_, N2, N3, N4 | Tail], Sum) ->
    part2([N2, N3, N4] ++ Tail, Sum);
part2(_, Sum) ->
    Sum.