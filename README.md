# Frog

This is some code that I wrote to simluate the math(s) problem shown in Matt Parker's (@standupmaths) [video](https://www.youtube.com/watch?v=ZLTyX4zL2Fc).

The code simulates a frog. The frog wants to cross a lake and has an equal chance of hopping to any of the lily-pads along the lake as well as to the other end of the lake. The frog progresses across the lake with an equal chance of jumping onto any of the available spots at each step. Watch the video for a better explanation and a cool game.

There is a python version of the simulation since everyone loves python. It runs in python 3 and using this

```
python3 frog.py <NUMBER_OF_SIMULATION_ROUNDS>
```

It takes about 22 seconds on my laptop to run a simulation of 10,000,000 steps

There is also a C version that is faster (but is harder to run, and runs the risk of overflowing with numbers too high). This can be run by first compiling and then running the executable

with `clang`:
`clang -03 -o frog frog.c -DROUNDS=<NUMBER_OF_ROUNDS>`
then:
`./frog`

with `gcc`:
`gcc -03 -o frog frog.c -DROUNDS=<NUMBER_OF_ROUNDS>`
then
`./frog`

the `-O3` is the highest level of optimization and is not strictly necessary but does speed up the program.
The C version with `-O3` takes about 3.9 seconds to run **100,000,000** steps of the simulation on my laptop.

Changing anything in the C version requires re-doing both steps for the changes to work.
