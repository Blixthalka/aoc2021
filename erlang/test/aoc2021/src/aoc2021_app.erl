%%%-------------------------------------------------------------------
%% @doc aoc2021 public API
%% @end
%%%-------------------------------------------------------------------

-module(aoc2021_app).

-behaviour(application).

-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    aoc2021_sup:start_link().

stop(_State) ->
    ok.

%% internal functions
