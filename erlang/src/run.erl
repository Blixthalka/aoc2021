-module(run).

-define(DAYS, [
    day1,
    day2,
    day3
]).

-export([
    all/0
]).

all() ->
    lists:map(fun(Day) ->
        Data1 = readlines("files/d" ++ Day:day() ++ "p1.txt", fun Day:part1_line_parse/1),
        Data2 = readlines("files/d" ++ Day:day() ++ "p2.txt", fun Day:part2_line_parse/1),

        P1 = Day:part1(Data1),
        P2 = Day:part2(Data2),

        {Day, P1, P2}
    end, ?DAYS).

readlines(FileName, TransformFun) ->
    {ok, Device} = file:open(FileName, [read]),
    get_all_lines(Device, [], TransformFun).

get_all_lines(Device, Accum, TransformFun) ->
    case io:get_line(Device, "") of
        eof  -> file:close(Device), Accum;
        Line -> get_all_lines(Device, Accum ++ [TransformFun(string:trim(Line))], TransformFun)
    end.
