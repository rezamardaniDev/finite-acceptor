class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def is_dfa(self):
        for state in self.states:
            for symbol in self.alphabet:
                if (state, symbol) not in self.transitions:
                    return False
        return True

    def accept_input(self, input_string):
        current_state = self.start_state
        sequence = [current_state]

        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
                sequence.append(current_state)
            else:
                return False, sequence

        return current_state in self.final_states and len(sequence) == len(input_string) + 1, sequence


def read_transition_file(file_path):
    transitions = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            current_state = parts[0]
            symbol = parts[1]
            next_state = parts[2]
            transitions[(current_state, symbol)] = next_state
    return transitions


def main():
    states = {'q0', 'q1', 'q2'}
    alphabet = {'a', 'b'}
    start_state = 'q0'
    final_states = {'q2'}

    # خواندن نام فایل انتقالات از کاربر
    file_path = 'transitions.txt'
    transitions = read_transition_file(file_path)

    automaton = FiniteAutomaton(states, alphabet, transitions, start_state, final_states)

    if automaton.is_dfa():
        print("The automaton is a DFA.")
    else:
        print("The automaton is not a DFA.")

    input_string = input("Enter a string: ")
    accepted, sequence = automaton.accept_input(input_string)

    if accepted:
        print("Accepted")
    else:
        print("Not Accepted")

    print("State sequence:", sequence)


if __name__ == "__main__":
    while True:
        main()
