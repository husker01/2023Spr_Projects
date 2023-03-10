# 2023Spr_Projects

Each project from this semester is a public fork linked from this repository.  This is just one of the many assignments students worked on for the course, but this is the *only* one they are permitted to publish openly.

## Final Project Expectations:

You have considerable flexibility about specifics and you will publish your project openly (as a fork from here) to allow making it part of your portfolio if you choose.  You may work alone or in a team of two students. 

Regardless of topic, it must involve notable amounts of original work of your own, though it can of course use existing libraries or be inspired by or built upon some other published work(s). 

PLAGIARISM IS NOT ACCEPTABLE. From the first commit through all production of documentation and code, it must be crystal clear which, if any, parts of the project were based on or duplicated from any other source(s) all of which must be cited. This should be so specific that any evaluator can tell which lines of code are original work and which aren't. Same for all written narrative, documentation, images, significant algorithms, etc.

## Project Types you may choose:

(Making original _variations_ of puzzles and games isn't as difficult as it may seem -- we have already done this in class. _Though admittedly, making *good* game variations -- that are well-balanced, strategically interesting, with good replay value_ can take expertise or luck and play-testing with revisions.  Such balanced elegance is desirable but might not be achievable here, given the short time you have.)

1. Devise your own new _original_ type of logic puzzle or an _original variation_ of existing puzzle type. Like with previous homework, your program should be able to randomly generate new puzzles of your type and automatically verify that all puzzles generated comply with the standard meta-rule that only one valid solution exists. It needs to output the _unsolved_ puzzles in a way that a human can print or view them conveniently to try solving them and to somehow output (to file?) or display the solution for each puzzle when requested, so as not to spoil the challenge. An interactive UI to "play" the puzzles interactively is very nice but *not* required. 

2. OR develop an AI game player for an _original variation_ of some existing strategy game.  If you do this, it needs to be set up so it can either play computer-vs-computer and/or against human players with a reasonable text or graphical UI. 2B. If two teams want to independently develop AI players for the same type of game variant as each other (but using different algorithms, strategies, and/or data structures) so they can compete, that is okay.  A sub-variation is to enable this game type on our course game server, discuss with the instructor if this is of interest.

3. OR Computationally 'Solve' a game.  _Background: Some strategic games, especially those of perfect information are known to be "solved". See https://en.wikipedia.org/wiki/Solved_game, which we discussed in class._  Sometimes these proofs are done through mathematical analysis, other times through exhaustive computational verification. If you choose this option, you can either write your own code or modify some existing code that plays a game, to exhaustively analyze a game to attempt to prove if it is "solved" in this way for certain configurations. Changes to rules or conditions of a known solved game can alter this outcome and require reanalysis.


## Deliverables and other Requirements:

* Have some fun!
* In your own fork, please replace this README.md file's contents with a good introduction to your own project. 
* Targeted Algorithm Analysis:  Regardless of which option you choose, you need to _describe the performance characteristics of some critical parts of your program and explain why you chose the data structures and core algorithm(s) you did_. Examples, if you chose Type #1, what's the Big-O, Big-Theta, or Big-Omega run-time complexity of your puzzle solver? Or the puzzle generator? If you're doing Type #2 and using minimax or negamax, what's the complexity of your _heuristic evaluation function_? ...and of the function that finds all legal moves from a game state? 
* Performance Measurement: Supplement the analysis above with run-time measurements of multiple iterations of the game or puzzles as discussed in class. Sample results from a run-time profiler is a good idea at least as part of the measurements.
* If your team has more than one student, see that everyone makes substantial git commits. In addition, your README documentation should include a summary of how you shared the work.
* Live in-class presentation & demonstration of your work.
