-module(day2).

-behaviour(day).

-export([
    day/0,
    part1/1,
    part2/1,
    part1_line_parse/1,
    part2_line_parse/1
]).

day() ->
    "2".

part1_line_parse(Line) ->
    line_parse(Line).

part1(Data) ->
    part1(Data, 0, 0).

part1([{<<"forward">>, Units} | Tail], Horizontal, Depth) ->
    part1(Tail, Horizontal + Units, Depth);
part1([{<<"down">>, Units} | Tail], Horizontal, Depth) ->
    part1(Tail, Horizontal, Depth + Units);
part1([{<<"up">>, Units} | Tail], Horizontal, Depth) ->
    part1(Tail, Horizontal, Depth - Units);
part1([], Horizontal, Depth) ->
    Horizontal * Depth.

part2_line_parse(Line) ->
    line_parse(Line).

part2(Data) ->
    part2(Data, 0, 0, 0).

part2([{<<"forward">>, Units} | Tail], Horizontal, Depth, Aim) ->
    part2(Tail, Horizontal + Units, Depth + Aim * Units, Aim);
part2([{<<"down">>, Units} | Tail], Horizontal, Depth, Aim) ->
    part2(Tail, Horizontal, Depth, Aim + Units);
part2([{<<"up">>, Units} | Tail], Horizontal, Depth, Aim) ->
    part2(Tail, Horizontal, Depth, Aim - Units);
part2([], Horizontal, Depth, _) ->
    Horizontal * Depth.

line_parse(Line) ->
    Split = binary:split(list_to_binary(Line), <<" ">>, [global]),
    {hd(Split), binary_to_integer(hd(tl(Split)))}.
