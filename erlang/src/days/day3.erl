-module(day3).

-behaviour(day).

-export([
    day/0,
    part1/1,
    part2/1,
    part1_line_parse/1,
    part2_line_parse/1
]).

day() ->
    "3".

part1_line_parse(Line) ->
    Line.

part1(Data) ->
    Map = create_value_map(Data, init_sum(length(hd(Data)), #{})),
    construct(Map, gamma) * construct(Map, epsilon).


construct(Map, Value) ->
    Binary = maps:fold(fun(_, V, Acc) ->
        case {V, Value} of
            {{Zeroes, Ones}, gamma} when Zeroes > Ones -> Acc ++ "0";
            {{Zeroes, Ones}, epsilon} when Zeroes < Ones -> Acc ++ "0";
            _ -> Acc ++ "1"
        end
    end, "", Map),
    list_to_integer(Binary, 2).

init_sum(0, Sum) ->
    Sum;
init_sum(Length, Sum) ->
    Sum1 = maps:put(Length - 1 , {0,0}, Sum),
    init_sum(Length - 1, Sum1).

create_value_map([Value|Tail], Sum) ->
    create_value_map(Tail, update_sum(0, Value, Sum));
create_value_map([], Sum) ->
    Sum.

update_sum(_, [], Sum) ->
    Sum;
update_sum(Index, [Value | Tail], Sum) ->
    {Zeroes, Ones} = maps:get(Index, Sum),
    Updated = case Value of
        48 -> {Zeroes + 1, Ones};
        49 -> {Zeroes, Ones + 1}
    end,
    UpdatedSum = maps:put(Index, Updated, Sum),
    update_sum(Index + 1, Tail, UpdatedSum).

part2(Data) ->
    Oxygen = part2_search(0, Data, oxygen),
    Co2 = part2_search(0, Data, co2),
    Oxygen * Co2.

part2_line_parse(Line) ->
    Line.

filter(Index, CurrIndex, [Value | _], Expected) when Index =:= CurrIndex ->
    Value =:= Expected;
filter(Index, CurrIndex, [_ | Tail], Expected) ->
    filter(Index, CurrIndex + 1, Tail, Expected).

part2_search(_, [Value], _) ->
    list_to_integer(Value, 2);
part2_search(Index, Data, Value) ->
    Map = create_value_map(Data, init_sum(length(hd(Data)), #{})),
    {Zeroes, Ones} = maps:get(Index, Map),
    case {{Zeroes, Ones}, Value} of
        {{Zeroes, Ones}, oxygen} when Zeroes > Ones ->
            Data1 = lists:filter(fun(Number) -> filter(Index, 0, Number, 48) end, Data);
        {{Zeroes, Ones}, co2} when Zeroes =< Ones ->
            Data1 = lists:filter(fun(Number) -> filter(Index, 0, Number, 48) end, Data);
        _ ->
            Data1 = lists:filter(fun(Number) -> filter(Index, 0, Number, 49) end, Data)
    end,
    part2_search(Index + 1, Data1, Value).

