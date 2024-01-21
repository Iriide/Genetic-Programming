import random
from enum import Enum


class TerminalNode:

    COMMA = ','
    DOT = '.'
    QUOTE = '"'
    LBRACE = '{'
    RBRACE = '}'
    LPAREN = '('
    RPAREN = ')'

    PLUS = '+'
    MINUS = '-'
    TIMES = '*'
    DIV = '/'

    ASSIGN = '='
    SEMI = ';'

    LT = '<'
    GT = '>'
    LE = '<='
    GE = '>='
    EQ = '=='
    NE = '!='

    AND = '&&'
    OR = '||'
    NOT = '!'

    READ = 'read'
    WRITE = 'write'
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'

    INT = 'int'
    BOOL = 'bool'
    FLOAT = 'float'
    STRING = 'string'

    TRUE = 'true'
    FALSE = 'false'

    IDENTIFIERS = [f'i_{i}' for i in range(5)]

    def __init__(self, token):
        self.token = token


def printNTree(x, flag, depth, isLast):
    # Condition when node is None


    if x == None:
        return

    # Loop to print the depths of the
    # current node
    for i in range(1, depth):
        # Condition when the depth
        # is exploring
        if flag[i]:
            print("| ", "", "", "", end="")

        # Otherwise print
        # the blank spaces
        else:
            print(" ", "", "", "", end="")

    # Condition when the current
    # node is the root node
    if depth == 0:
        if type(x) != Node:
            print(x)
        else:
            print(x.name)

    # Condition when the node is
    # the last node of
    # the exploring depth
    elif isLast:
        if type(x) != Node:
            print("+---", x)
        else:
            print("+---", x.name)

        # No more childrens turn it
        # to the non-exploring depth
        flag[depth] = False
    else:
        if type(x) != Node:
            print("+---", x)
        else:
            print("+---", x.name)

    if type(x) != Node:
        return

    it = 0
    for i in x.children:
        it += 1

        # Recursive call for the
        # children nodes
        printNTree(i, flag, depth + 1, it == (len(x.children) - 1))
    flag[depth] = True


class Node:

    def __init__(self, name: str):
        self.children = []
        self.name = name


class Generator:

    def __init__(self):
        self.starting_node = Node('program')
        # Unterminated nodes are nodes that are not yet terminated by a terminal node
        self.unterminated_nodes = [self.starting_node]

        # Extendable nodes are nodes that can have children added to them
        self.extendable_nodes = [self.starting_node]
        self._handle_program_node(self.starting_node)
        printNTree(self.starting_node, [True] * 500, 0, True)
        self.walk_node(self.starting_node)


    def walk_node(self, node):
        if type(node) != Node:
            print(node)
        else:
            for child in node.children:
                self.walk_node(child)

    def _handle_program_node(self, program_node: Node):
        statement = Node('statement')
        program_node.children = [statement]
        self.unterminated_nodes.append(statement)

        self.extendable_nodes.append(program_node)
        self._handle_statement_node(statement)

        self.unterminated_nodes.remove(program_node)

    def _extend_program_node(self, program_node: Node):
        self.unterminated_nodes.append(program_node)




    """
    statement   : assignmentStatement SEMI
            | declStatement
            | loopStatement
            | ifStatement
            | read
            | write
            | block
            ;
            """

    def _handle_statement_node(self, statement_node: Node):
        choice = random.randint(0, 6)
        match choice:
            case 0:
                assignment_statement = Node('assignmentStatement')
                statement_node.children = [assignment_statement, TerminalNode.SEMI]
                self.unterminated_nodes.append(assignment_statement)
                self._handle_assignment_statement_node(assignment_statement)
            case 1:
                decl_statement = Node('declStatement')
                statement_node.children = [decl_statement]
                self.unterminated_nodes.append(decl_statement)
                self._handle_decl_statement_node(decl_statement)
            case 2:
                loop_statement = Node('loopStatement')
                statement_node.children = [loop_statement]
                self.unterminated_nodes.append(loop_statement)
                self._handle_loop_statement_node(loop_statement)
            case 3:
                if_statement = Node('ifStatement')
                statement_node.children = [if_statement]
                self.unterminated_nodes.append(if_statement)
                self._handle_if_statement_node(if_statement)
            case 4:
                read = Node('read')
                statement_node.children = [read]
                self.unterminated_nodes.append(read)
                self._handle_read_node(read)
            case 5:
                write = Node('write')
                statement_node.children = [write]
                self.unterminated_nodes.append(write)
                self._handle_write_node(write)
            case 6:
                block = Node('block')
                statement_node.children = [block]
                self.unterminated_nodes.append(block)
                self._handle_block_node(block)

        self.unterminated_nodes.remove(statement_node)

    def _handle_assignment_statement_node(self, assignment_statement_node: Node):
        identifier = Node('identifier')
        assignment_statement_node.children = [identifier, TerminalNode.ASSIGN]
        self.unterminated_nodes.append(identifier)
        self._handle_identifier_node(identifier)

        expression = Node('expression')
        assignment_statement_node.children.append(expression)
        self.unterminated_nodes.append(expression)
        self._handle_expression_node(expression)

        self.unterminated_nodes.remove(assignment_statement_node)

    def _handle_decl_statement_node(self, decl_statement_node: Node):
        type_specifier = Node('typeSpecifier')
        decl_statement_node.children = [type_specifier]
        self.unterminated_nodes.append(type_specifier)
        self._handle_type_specifier_node(type_specifier)

        decl_with_optional_assignment = Node('declWithOptionalAssignment')
        decl_statement_node.children.append(decl_with_optional_assignment)
        decl_statement_node.children.append(TerminalNode.SEMI)
        self.unterminated_nodes.append(decl_with_optional_assignment)
        self._handle_decl_with_optional_assignment_node(decl_with_optional_assignment)

        self.unterminated_nodes.remove(decl_statement_node)

    def _handle_loop_statement_node(self, loop_statement_node: Node):
        expression = Node('expression')
        loop_statement_node.children = [TerminalNode.WHILE,
                                        TerminalNode.LPAREN, expression]
        self.unterminated_nodes.append(expression)
        self._handle_expression_node(expression)

        loop_statement_node.children.append(TerminalNode.RPAREN)

        statement = Node('statement')
        loop_statement_node.children.append(statement)
        self.unterminated_nodes.append(statement)
        self._handle_statement_node(statement)

        self.unterminated_nodes.remove(loop_statement_node)

    def _handle_if_statement_node(self, if_statement_node: Node):
        expression = Node('expression')
        if_statement_node.children = [TerminalNode.IF,
                                      TerminalNode.LPAREN, expression]
        self.unterminated_nodes.append(expression)
        self._handle_expression_node(expression)

        if_statement_node.children.append(TerminalNode.RPAREN)

        statement = Node('statement')
        if_statement_node.children.append(statement)
        self.unterminated_nodes.append(statement)
        self._handle_statement_node(statement)

        self.unterminated_nodes.remove(if_statement_node)

    def _handle_read_node(self, read_node: Node):
        identifier = Node('identifier')
        read_node.children = [TerminalNode.READ,
                                TerminalNode.LPAREN, identifier]
        self.unterminated_nodes.append(identifier)
        self._handle_identifier_node(identifier)

        read_node.children.append(TerminalNode.RPAREN)
        self.unterminated_nodes.remove(read_node)

    def _handle_write_node(self, write_node: Node):
        expression = Node('expression')
        write_node.children = [TerminalNode.WRITE,
                                TerminalNode.LPAREN, expression]
        self.unterminated_nodes.append(expression)
        self._handle_expression_node(expression)

        write_node.children.append(TerminalNode.RPAREN)
        self.unterminated_nodes.remove(write_node)

    def _handle_block_node(self, block_node: Node):
        statement = Node('statement')
        block_node.children = [TerminalNode.LBRACE, statement]
        self.unterminated_nodes.append(statement)
        self._handle_statement_node(statement)

        block_node.children.append(TerminalNode.RBRACE)
        self.unterminated_nodes.remove(block_node)

    def _handle_decl_with_optional_assignment_node(self, decl_with_optional_assignment_node: Node):
        identifier = Node('identifier')
        decl_with_optional_assignment_node.children = [identifier]
        self.unterminated_nodes.append(identifier)
        self._handle_identifier_node(identifier)

        if random.randint(0, 1) == 0:
            decl_with_optional_assignment_node.children.append(TerminalNode.ASSIGN)
            expression = Node('expression')
            decl_with_optional_assignment_node.children.append(expression)
            self.unterminated_nodes.append(expression)
            self._handle_expression_node(expression)

        self.unterminated_nodes.remove(decl_with_optional_assignment_node)

    def _handle_expression_node(self, expression_node: Node):
        logical_or_expression = Node('logicalOrExpression')
        expression_node.children = [logical_or_expression]
        self.unterminated_nodes.append(logical_or_expression)
        self._handle_logical_or_expression_node(logical_or_expression)

        self.unterminated_nodes.remove(expression_node)

    def _handle_logical_or_expression_node(self, logical_or_expression_node: Node):
        logical_and_expression = Node('logicalAndExpression')
        logical_or_expression_node.children = [logical_and_expression]
        self.unterminated_nodes.append(logical_and_expression)
        self._handle_logical_and_expression_node(logical_and_expression)

        if random.randint(0, 10) == 0:
            logical_and_expression_2 = Node('logicalAndExpression')
            logical_or_expression_node.children.append(TerminalNode.OR)
            logical_or_expression_node.children.append(logical_and_expression_2)
            self.unterminated_nodes.append(logical_and_expression_2)
            self._handle_logical_and_expression_node(logical_and_expression_2)

        self.unterminated_nodes.remove(logical_or_expression_node)

    def _handle_logical_and_expression_node(self, logical_and_expression_node: Node):
        equality_expression = Node('equalityExpression')
        logical_and_expression_node.children = [equality_expression]
        self.unterminated_nodes.append(equality_expression)
        self._handle_equality_expression_node(equality_expression)

        if random.randint(0, 10) == 0:
            equality_expression_2 = Node('equalityExpression')
            logical_and_expression_node.children.append(TerminalNode.AND)
            logical_and_expression_node.children.append(equality_expression_2)
            self.unterminated_nodes.append(equality_expression_2)
            self._handle_equality_expression_node(equality_expression_2)

        self.unterminated_nodes.remove(logical_and_expression_node)

    def _handle_equality_expression_node(self, equality_expression_node: Node):
        relational_expression = Node('relationalExpression')
        equality_expression_node.children = [relational_expression]
        self.unterminated_nodes.append(relational_expression)
        self._handle_relational_expression_node(relational_expression)

        if random.randint(0, 10) == 0:
            equality_relation = Node('equalityRelation')
            equality_expression_node.children.append(equality_relation)
            self.unterminated_nodes.append(equality_relation)
            self._handle_equality_relation_node(equality_relation)

            relational_expression_2 = Node('relationalExpression')
            equality_expression_node.children.append(relational_expression_2)
            self.unterminated_nodes.append(relational_expression_2)
            self._handle_relational_expression_node(relational_expression_2)

        self.unterminated_nodes.remove(equality_expression_node)

    def _handle_relational_expression_node(self, relational_expression_node: Node):
        additive_expression = Node('additiveExpression')
        relational_expression_node.children = [additive_expression]
        self.unterminated_nodes.append(additive_expression)
        self._handle_additive_expression_node(additive_expression)

        if random.randint(0, 10) == 0:
            relation = Node('relation')
            relational_expression_node.children.append(relation)
            self.unterminated_nodes.append(relation)
            self._handle_relation_node(relation)

            additive_expression_2 = Node('additiveExpression')
            relational_expression_node.children.append(additive_expression_2)
            self.unterminated_nodes.append(additive_expression_2)
            self._handle_additive_expression_node(additive_expression_2)

        self.unterminated_nodes.remove(relational_expression_node)

    def _handle_additive_expression_node(self, additive_expression_node: Node):

        multiplicative_expression = Node('multiplicativeExpression')
        additive_expression_node.children = [multiplicative_expression]
        self.unterminated_nodes.append(multiplicative_expression)
        self._handle_multiplicative_expression_node(multiplicative_expression)

        if random.randint(0, 10) == 0:
            multiplicative_expression_2 = Node('multiplicativeExpression')
            additive_expression_node.children.append(TerminalNode.PLUS)
            additive_expression_node.children.append(multiplicative_expression_2)
            self.unterminated_nodes.append(multiplicative_expression_2)
            self._handle_multiplicative_expression_node(multiplicative_expression_2)

        self.unterminated_nodes.remove(additive_expression_node)

    def _handle_multiplicative_expression_node(self, multiplicative_expression_node: Node):
        unary_expression = Node('unaryExpression')
        multiplicative_expression_node.children = [unary_expression]
        self.unterminated_nodes.append(unary_expression)
        self._handle_unary_expression_node(unary_expression)

        if random.randint(0, 10) == 0:
            unary_expression_2 = Node('unaryExpression')
            multiplicative_expression_node.children.append(TerminalNode.TIMES)
            multiplicative_expression_node.children.append(unary_expression_2)
            self.unterminated_nodes.append(unary_expression_2)
            self._handle_unary_expression_node(unary_expression_2)

        self.unterminated_nodes.remove(multiplicative_expression_node)

    def _handle_unary_expression_node(self, unary_expression_node: Node):
        choice = random.randint(0, 20)
        match choice:
            case 0:
                unary_operator = Node('unaryOperator')
                unary_expression_node.children = [unary_operator]
                self.unterminated_nodes.append(unary_operator)
                self._handle_unary_operator_node(unary_operator)

                primary_expression = Node('primaryExpression')
                unary_expression_node.children.append(primary_expression)
                self.unterminated_nodes.append(primary_expression)
                self._handle_primary_expression_node(primary_expression)
            case _:
                primary_expression = Node('primaryExpression')
                unary_expression_node.children = [primary_expression]
                self.unterminated_nodes.append(primary_expression)
                self._handle_primary_expression_node(primary_expression)

        self.unterminated_nodes.remove(unary_expression_node)

    def _handle_primary_expression_node(self, primary_expression_node: Node):

        choice = random.randint(0, 1)
        match choice:
            case 0:
                identifier = Node('identifier')
                primary_expression_node.children.append(identifier)
                self.unterminated_nodes.append(identifier)
                self._handle_identifier_node(identifier)
            case 1:
                literal = Node('literal')
                primary_expression_node.children.append(literal)
                self.unterminated_nodes.append(literal)
                self._handle_literal_node(literal)
            case 2:
                primary_expression_node.children.append(TerminalNode.LPAREN)
                # TODO: EXPRESSION

        self.unterminated_nodes.remove(primary_expression_node)

    def _handle_identifier_node(self, identifier_node: Node):
        identifier_node.children = [random.choice(TerminalNode.IDENTIFIERS)]
        self.unterminated_nodes.remove(identifier_node)

    def _handle_literal_node(self, literal_node: Node):
        choice = random.randint(0, 3)

        match choice:
            case 0:
                # BOOL_LITERAL
                literal_node.children = [random.choice([TerminalNode.TRUE, TerminalNode.FALSE])]
            case 1:
                # INT_LITERAL
                literal_node.children = [random.randint(0, 100)]
            case 2:
                # FLOAT_LITERAL
                literal_node.children = [random.uniform(0, 100)]
            case 3:
                # STRING_LITERAL
                literal_node.children = [random.choice(['abc', 'bcd', 'cde'])]

        self.unterminated_nodes.remove(literal_node)

    def _handle_type_specifier_node(self, type_specifier_node: Node):
        type_specifier_node.children = [random.choice([TerminalNode.INT, TerminalNode.FLOAT, TerminalNode.BOOL, TerminalNode.STRING])]
        self.unterminated_nodes.remove(type_specifier_node)

    def _handle_unary_operator_node(self, unary_operator_node: Node):
        unary_operator_node.children = [TerminalNode.MINUS]
        self.unterminated_nodes.remove(unary_operator_node)

    def _handle_equality_relation_node(self, equality_relation_node: Node):
        equality_relation_node.children = [random.choice([TerminalNode.EQ, TerminalNode.NE])]
        self.unterminated_nodes.remove(equality_relation_node)

    def _handle_relation_node(self, relation_node: Node):
        relation_node.children = [random.choice([TerminalNode.GE, TerminalNode.GT, TerminalNode.LT, TerminalNode.LE])]
        self.unterminated_nodes.remove(relation_node)

g = Generator()
