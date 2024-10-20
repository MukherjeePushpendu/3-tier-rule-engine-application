class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left  # Left child Node
        self.right = right  # Right child Node
        self.value = value  # Value for operand nodes

def create_rule(rule_string):
    # Parsing the rule_string and constructing the AST
    pass  # Implement parsing logic here

def combine_rules(rules):
    # Combining multiple AST rules into one
    pass  # Implement combination logic

def evaluate_rule(ast, data):
    # Traverse AST and evaluate rule based on user data
    pass  # Implement evaluation logic
