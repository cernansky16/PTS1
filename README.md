# PTS1
TASK 
Assignment 1
Your task is to develop the core of a simplified "Sleeping Queens" game. You can find the rules of the game here. To make things a bit easier, we modify rules as follows:
No "Jester" card.
No queen special effects.
Upon playing "Knight" or "Sleeping potion", if targeted player has the corresponding defensive card, then the game plays it automatically. This makes the game state machine much more simple.
I prepared a design outline (previous iteration). Note that this is not a full design. The point is to specify what are the responsibilities of each class. It is up to you add all necessary constructors, interfaces, etc. to make the design good for the purpose. Note also, that there are probably some flaws, I have done only limited amount of exploratory testing of the design as of now. If you encounter some issue, write me a message (use the ordinary address, not the one used to submit solutions).

To implement the solution you can use Java or Python. If you use Python, YOU HAVE TO USE TYPE ANNOTATIONS (integrate mypy into your development). Use last year assignment 1 materials as a template for your project.


Further requirements
Your code should be accompanied with automated tests with a reasonable structure. The tests should be deterministic (you may need to make design adjustments to achieve this). To make things easier for you, it is OK to do only very minimal tests of GameObservable class and observation aspect of the assignment in general.
Solitary unit tests for Player class. You can use both solitary and sociable unit tests for other classes.
You have to use git and produce a reasonable commit history.
Implement two versions of how the situation when deck is empty is handled. In one solution, when there are not enough cards, the player throws his cards, draws what he can and then shuffles the discard pile and draw remaining cards. In the second solution, if there are not enough cards in the deck, shuffle the discard pile and put it under the deck, then discard used cards and draw cards. Make your design so that it is possible to add new behaviours of this type without modifying existing code (OCP). Focus on good unit tests for these classes.
