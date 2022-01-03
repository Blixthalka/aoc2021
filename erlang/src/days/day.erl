-module(day).

-callback day() -> string().
-callback part1([any()]) -> any().
-callback part2([any()]) -> any().
-callback part1_line_parse(string()) -> any().
-callback part2_line_parse(string()) -> any().