# Austin Nguyen
# Qubit Project
# QCB (Quantum Computing at Berkeley)
# Start Date: February 23, 2018
<<<<<<< HEAD
=======

"""
- State: up = 0, down = 1
- Looking at ONE qubit
    - |psi> = a|^> + b|v>
- 2^N basis states (N qubits)
- General quantum state of a 3-qubit register is superposition of the eight
  basis states:
    - |psi> = a|000> + b|001> + ... + g|110> + h|111>
- The quantum state is stored in the computer as a column vector of the
  eight complex numbers
- Stages of quantum computation:
    - Initialization
            - Initialize to definite quantum state
    - Series of quantum gate operations applied
    - Qubits are measured
- IMPORTANT: to simulate a quantum computer, carry out each of the stages on
 a quantum state represented in the computer form of the column vector of quantum
 state
 - For initialiation:
        - Initialize the N-qubit register to its 2^N basis states
 - For measurement:
        - The probability of measuring each basis state is given by the square
            magnitude of the corresponding amplitude
"""


>>>>>>> 0e6620a... my cool ass project
#Project1

#Part 1:

# Allocates a column vector with 2^qubits complex entries, assigns to psi
# and return psi
<<<<<<< HEAD
import random, math
import numpy

class state ():
    def __init__ (self, number_qubits):
        self.coefs = [] #list of coefficietns of initialized state
        for i in range(0, number_qubits):
            print ('Inputs for qubit number', i + 1, ':')
            print('')
            instance = qubit()
            coefs(self, instance) #fill in the coefficients of the new state
        self.collapsed = False

    def measure_state(self, basis):
        #basis is a LISTS of LISTS of values
        #number of elements in basis and the number of elements in each element of basis should be equal to number of vectors in state
        assert len(basis) == len(self.coefs), 'Invalid number of basis elements'

        ran_num = random.uniform (0,1)
        q, flag, tracker = 0, 0, 0
        probabilities = [inner_prod(self.coefs, base) for base in basis]
        print ('Probabilities:')
        for i in list(range(len(basis))):
            print('Basis', i, ':', probabilities[i])
        print ('Random number chosen to decide winning state:' , ran_num)

        while flag == 0 and tracker < len(basis):
            q += probabilities[tracker] #determining the "winning" state
            if q > ran_num:
                flag = 1
            else:
                tracker += 1

        print('The state has collasped to basis number', tracker, ' (with index starting at 0)')
        self.coefs = basis[tracker]
        print('')

    def default_measure(self):
        #takes a state instance and returns a specific state for the qubits to collapse to
        #uses the probabilities of the coefficients in the state
        ran_num = random.uniform(0,1)
        q = 0
        i = 0 #tracker. also represents the index in which the state will collapse to

        if self.collapsed == True:
            print('')
            print('The state has already collapsed. The state is forever:', self.forever_state)
            print('')
            return None #short circuit

        while q > (self.coefs[i]) **2: #select a state according to probability
            q += (self.coefs[i])**2
            i += 1

        print ('')
        print ('The basis vectors are simply 0 and 1')
        print ('')
        print ('Random number to determine state: ', ran_num)
        print ('')

        #DISPLAY FORMATTING
        new_state ="{0:b}".format(i+1) #the winning state is in the form of binary
        # but new_state does not include preceding zeros
        num_qubits = int(math.log (len(self.coefs), 2))

        for _ in range(num_qubits - int(new_state)): #include the preceding zeros
            new_state = '0' + new_state

        print ('The state has collapsed to: ', new_state)
        print ('')

        tracker = 0
        while tracker < len(self.coefs): #resetting the list of coefficients to 0 except for the one winner
            if tracker != i:
                self.coefs[tracker] = 0
            else:
                self.coefs[tracker] = 1
            tracker += 1
        tracker = 0

        self.collapsed = True #it's been collapsed
        self.forever_state = new_state

    def apply_gates (self):
        print('This applies an n number of gates at ONE CERTAIN POINT IN TIME')
        print('Please enter gates in order of qubit being applied to')
        print('')
        gate_number = int(input('Number of gates being applied (integer): ')) #returns int
        tracker = 0

        print ('')
        print ('Options: [H] Hadamard, [Z] Z-Gate, [X] X-Gate, [C] C-Not, [S] Swap')

        all_names = []
        all_numbers = []

        while tracker < gate_number:
            print('Enter name of gate number ',tracker)
            gate_name = input()
            all_names += [gate_name]

            if gate_name == 'C': #the description of the c not gate consists of three things:
                # control qubit, what type of target it is, where the target is
                print('Indexes are 0 to', int(math.log (len(self.coefs), 2)) - 1)
                control = input('Control:')
                type = input("Type of gate you're controlling (type in 1 if N/A):")
                print('')
                qubit_number = [control, type]
                #this will be stored as one element describing the specifics
                #of the c not gate
            else:
                print('On which qubit? Pick number from 0 to',int(math.log (len(self.coefs), 2)) - 1, ': ')
                qubit_number = input()

            all_numbers += [qubit_number]
            tracker += 1
            print('')

        self.coefs = execute_gates (all_names, all_numbers, self.coefs)

    def grover (self, correct_state):
            #method that takes in the index of the correct state ie. 7 in superposition of 3 qubits => 110
        tracker = 0
        #first, apply hadamard gate on all qubits
        num_qubits = int(math.log(len(self.coefs), 2))
        names, numbers = get_hada(num_qubits)
        self.coefs = execute_gates(names, numbers, self.coefs) #applies hadamards on all of them initially
        #then, apply the oracle, 3 hadamards, j operator, and 3 hadamards a certain number of times until you get the correct_state

        while tracker < ((3.14159265/4)*((2**num_qubits)**(1/2))):
            #oracle
            oracle = oracle_maker(correct_state, self.coefs)
            self.coefs = matrix_mult(self.coefs, oracle)
            #hadamards
            names, numbers = get_hada(num_qubits) #reassign names and numbers
            self.coefs = execute_gates(names, numbers, self.coefs)
            #j operator
            j_operator = j_maker(self.coefs)
            self.coefs = matrix_mult(self.coefs, j_operator)
            #hadamards
            names, numbers = get_hada(num_qubits)
            self.coefs = execute_gates(names, numbers, self.coefs)
            tracker += 1

def get_hada (num_qubits):
    #returns a list of H's and list of numbers
    numbers = list(range(num_qubits))
    return (['H' for elem in range(num_qubits)], [str(elem) for elem in numbers])

def coefs (state, qubit):
    #takes in a state instance and a new qubit to add in
    #mutates the the coefficients of the inititlized state

    if not state.coefs: #if coefs is empty
        state.coefs.extend([qubit.a, qubit.b])
    else:
        factors = [qubit.a, qubit.b] #just to make things easier when traversing
        new = []
        for old in state.coefs: #looking through old coefficients
            for factor in factors: #multiplying by new coefficients
                new.append(old*factor)
        state.coefs = new #reassigning to the new coefficients
        #should be in proper order ie 000 001 010 011 etc.

class qubit (): #just for representation purposes

    def __init__(self):
        self.a = eval(input('Enter value of coefficient of zero vector: ')) #0 #do these have to be complex numbers???
        print('')
        self.b = eval(input ('Enter value of coefficient of one vector: ')) #1
        print('')
        normal(self)

def normal (qubit):
    #should be receiving a qubit instance
    total = qubit.a**2 + qubit.b**2
    qubit.a = qubit.a / total**(1/2)
    qubit.b = qubit.b / total**(1/2)


def execute_gates(all_names, all_numbers, coefficients):
        matrix = matrix_maker (all_names, all_numbers, coefficients)
        #this function returns the proper matrix to multiply the state by
        coefficients = matrix_mult(coefficients, matrix)
        print('New coefficients:')
        print(coefficients)
        print('')
        return coefficients

def oracle_maker(correct_state, coefficients):
        #correct state is the number of the coefficient that is deemeed "correct"
        names = []
        numbers = []
        oracle = matrix_maker(names, numbers, coefficients)
        oracle [correct_state][correct_state] = -1
        return oracle

def j_maker (coefficients):
        names = []
        numbers = []
        j_operator = matrix_maker(names,numbers, coefficients)
        j_operator [0][0] = -1
        return j_operator


def matrix_maker(names, numbers, coefficients):
    #names contains a list of strings that contains the gates in which user wants to execute
    # numbers contains corresponding index of qubit that each gate should be applied
    #coefficients contains a list of the coefficients of the current state

    dictionary = {'H': hadamard, 'Z': z_gate, 'X': x_gate, 'C': cnot_gate, 'S': swap_gate, 'I': identity}
    #dictionary contains a dictionary of all the gate names and first letters as keys

    tracker, matrix = 0, []
    num_qubits = int(math.log (len(coefficients), 2)) #number of qubits
    while tracker < num_qubits: #for every qubit
        name = 0
        if str(tracker) in return_first(numbers): #return_first takes care of special case with CNot gates...returns a list of
            #the qubits in which  are either being put through a gate or is a control for CNot

            #if the user wants to apply something to that qubit
            name = names.pop(0)
            if name == 'C': #i'll only handle Cnot gates for now
                if tracker == 0:
                    matrix = dictionary[name](numbers[0][1], dictionary) #target, type, dict
                else:
                    applied_gate = dictionary[name](numbers[0][1], dictionary)
                    matrix = tensor_product(matrix, applied_gate)
            else: #not a CNot gate
                if tracker == 0: #if first time
                    matrix = dictionary[name]()
                else:
                    applied_gate = dictionary[name]()
                    matrix = tensor_product(matrix, applied_gate) #add in gate to matrix
            numbers.pop(0)
        else: #if the user does not want ot do anything with that qubit, put in identity matrix
            if tracker == 0: #if first time
                matrix = identity()
            else:
                matrix = tensor_product(matrix, identity())
        if name == 'C' or name == 'S': #must offset the fact that C and S affect TWO QUBITS
            tracker += 2
        else:
            tracker += 1
    return matrix

def hadamard ():
    return [[1/(2**(1/2)), 1/(2**(1/2))], [1/(2**(1/2)), -1/(2**(1/2))]]

def x_gate ():
    return [[0,1], [1,0]]

def z_gate ():
    return [[1, 0], [0, -1]]

def identity():
    return [[1,0], [0, 1]]

def cnot_gate(type, dictionary):
    if type == '1': #if not controlling a gate but controlling a qubit
        return [[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]]
    else:
        insert = dictionary[type]()
        return [[1,0,0,0], [0, 1, 0,0], [0,0,insert[0][0], insert[0,1],], [0,0,insert[1][0], insert[1][1]]]

def swap_gate():
    return [[1,0,0,0], [0,0,1,0], [0,1,0,0], [0,0,0,1]]


def return_first(array):
    new = []
    for element in array:
        if isinstance(element, list):
            new += [element[0]] #control of the cnot
        else:
            new += [element]
    return new

def inner_prod (current, project_onto):
    #takes the components of two vectors and returns the inner product (the probability)
    #state1 and state 2 are lists that represent the components of a vector (just its coefficients)
    #probability is the square of the projection onto the basis vectors

    sum, i, num_comp = 0, 0, len(current)

    while i < num_comp:
        sum += current[i]*project_onto[i]
        i += 1

    probability = sum ** 2

    return probability

def matrix_mult (state, mat):
    #takes a state and matrix (list of lists) and returns resulting matrix
    #every element in mat is a row
    #all elements in state are already in one single column\
    relisted_state = [[coef] for coef in state] #represents a column matrix
    result = numpy.matmul(mat, state)
    result = result.tolist()

    return result #returns a n by 1 matrix of all the coefficients...fixed up
def tensor_product(mat1, mat2):
    #every element in the mats are rows
    #every element in the rows are the elements in that column of the row
    result = numpy.kron(mat1, mat2)
    result = result.tolist()

    return result
=======
import random

#initializes an n qubit state: takes number of qubits you want and
def initialize (qubits):
    # returns an intiial state psi that is a list of lists with the probability constant and binary state
    i = 1
    list_qubits = []
    while i <= qubits:
        list_qubits = list_qubits + [make_qubit()]
        i += 1
    result = [0]
    for qubit in list_qubits:
        result = tensor_product (result, qubit)
    return result

#makes a qubit with coefficients a and b and two states 0 and 1
def make_qubit ():
    # returns a list that contains two lists: each containing complex number and state
    # [[a,0], [b,1]]
    #Let a1 and a2 be the respective real and imaginary parts of a (same with b)
    a1, a2 = random.randint(1,101), random.randint(1,101)
    b1, b2 = random.randint(1,101), random.randint(1,101)
    a, b = complex(a1, a2), complex(b1, b2)

    qubit = [[a,[0]], [b,[1]]]
    qubit = normalize (qubit) #make sure that the sum of squared magnitudes of a and b are equal to 1
    return qubit

def tensor_product(result, qubit):
    # returns the tensor product of two given qubit states

    if result[0] == 0: #if this is the first product
        product = [elem for elem in qubit]
    else:
        product = []
        for elem1 in result:
            for elem2 in qubit:
                product += [[elem1[0]*elem2[0],elem1[1]+elem2[1]]]
    return product

def product_complex (comp1, comp2): #multiplies two complex numbers together
    # a = real part of resultant, b=imaginary part of resultant
    a = comp1.real*comp2.real - comp1.imag*comp2.imag
    b = comp1.real*comp2.imag + comp2.real*comp1.imag
    result = complex(a,b)

    return result

def normalize (result):
    #returns a normalized version of the new initial state (sums of square magnitudes equal 1)
    sum = 0
    for elem in result:
        sum = sum + (magnitude(elem[0]))**2
    result = [[elem[0]/sum**(1/2), elem[1]] for elem in result]
    return result


def magnitude(comp_num): #returns the magnitude of a complex number
    return (comp_num.real**2 + comp_num.imag**2)**(1/2)

def measure(psi): #takes the initialized qubit state list
    ran_num = random.uniform(0,1) #generates a random float 0 to 1
    q = 0

    if 'Collapsed' in psi:
        state = [elem for elem in psi if 'Collapsed State' in elem]
        return state [0][1]

    for state in psi:
        q += (magnitude(state[0]))**2
        if ran_num < q:
            state.extend(['Collapsed State'])
            state = state[1]
            psi.extend(['Collapsed'])
            return state
    # uses probability given by coefficients to decide which measurement state the n-qubit will collapse to
    # returns the state in which the qubit is now in...must collapse to it and NOT change

#returns a random state
"""def make_state():
    psi = [['a', 1/(2**(1/2))], ['b', 0], ['c', 0], ['d', 1], ['e', 0], ['f', 0], ['g', 0], ['h', 1/(2**(1/2))]]

    ran_num = random.uniform (0, 1) #generates random float 0 to 1

    return decider (psi, ran_num, find_binary) #returns the binary of a random state


#converts a basis state to binary value
def find_binary(converter, basis):
    return converter(basis)

#randomly decides which basis state to choose and returns binary value
def decider (psi, random, binary):
    converter = {'a':000, 'b':001, 'c':010, 'd': 100, 'e': 011, 'f': 110, 'g': 101, 'h': 111}
    q = 0
    for state in psi:
        q = state[1]**2
        if random < q:
            return binary (converter, state[0])"""

#Use distributive property to find the tensor product and then use that to construct you 2^n qubit register
#To find the coefficients a,b,c... use complex numbers whose sum of squared magnitudes equal 1
#then, find those respective amplitudes...normalize them by dividing out by general magnitude so it sums to 1
#Use double for loop or nested lists to represent data
#Make sure you have one list for psi that lists all of the complex coefficients but also another list that represents the entire vector space
>>>>>>> 0e6620a... my cool ass project
