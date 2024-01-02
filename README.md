# Finite Automaton

This Python script implements a Finite Automaton class capable of handling Deterministic Finite Automata (DFA). The `FiniteAutomaton` class is defined with methods to check if the automaton is a DFA and to determine if a given input string is accepted.

## Usage

### FiniteAutomaton Class

The `FiniteAutomaton` class is initialized with the following parameters:
- `states`: Set of states in the automaton.
- `alphabet`: Set of symbols in the input alphabet.
- `transitions`: Dictionary representing the transitions between states based on input symbols.
- `start_state`: The initial state of the automaton.
- `final_states`: Set of final/accepting states.

#### Methods

1. `is_dfa()`: Checks if the automaton is a Deterministic Finite Automaton (DFA).

2. `accept_input(input_string)`: Accepts an input string and determines if it is accepted by the automaton. Returns a tuple of acceptance status and the sequence of visited states.

### Reading Transition File

The script includes a function `read_transition_file(file_path)` to read transition information from a file and convert it into a dictionary used by the `FiniteAutomaton` class.

## Example

To use the script, create an instance of the `FiniteAutomaton` class with the necessary parameters, and interactively test input strings.

```bash
python main.py
The script prompts the user to enter a string and outputs whether the string is accepted or not, along with the sequence of visited states.

File Structure
main.py: The main Python script containing the FiniteAutomaton class and the main() function for interactive testing.
transitions.txt: Example file containing transition information.
Feel free to modify the automaton parameters and transition file to suit your specific use case.
