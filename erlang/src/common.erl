-module(common).

-export([
    readlines/2
]).

readlines(FileName, TransformFun) ->
    {ok, Device} = file:open(FileName, [read]),
    get_all_lines(Device, [], TransformFun).

get_all_lines(Device, Accum, TransformFun) ->
    case io:get_line(Device, "") of
        eof  -> file:close(Device), Accum;
        Line -> get_all_lines(Device, Accum ++ [TransformFun(string:trim(Line))], TransformFun)
    end.
