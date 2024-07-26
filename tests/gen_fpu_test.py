# Define the file path
file_path = 'tests/FPU/circuits/tests/test_mul_hard.txt'

# List to store the generated macros
test_macros = []

# Open and read the file
with open(file_path, 'r') as file:
    for i, line in enumerate(file):
        line = line.strip()
        # Ignore empty lines and comments
        if line and not line.startswith('#'):
            parts = line.split()
            op, inA, inB, Out, *_ = parts
            macro = f'TEST_MUL_FPU({inA}, {inB}, {Out}, FAIL_MUL_HARD_{i})'
            test_macros.append(macro)

# Print the generated macros
for macro in test_macros:
    print(macro)



