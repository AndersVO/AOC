"""
http://adventofcode.com/2017/day/8
"""

from typing import Dict

from typing import NamedTuple, List, Dict
import re
import operator
from collections import defaultdict



# Ups jeg blev ikke færdig.
# example line: o inc 394 if tcy >= -3

class Condition(NamedTuple):
    register: str
    comparison: str
    target: int

class Instruction(NamedTuple):
    register: str
    operation: str
    increment: int
    Condition: Condition




# example line: o inc 394 if tcy >= -3
def create_instruction(s: str) -> Instruction:
    instr, condi = s.split(" if ")
    instr_split = re.split('( dec | inc )', instr)
    reg_name = str(instr_split[0]) # o
    operation = str(instr_split[1]).strip() # inc without whitespaces
    increment = int(instr_split[2]) # 394

    # find condition
    condition_split = re.split('( == | >= | <= | > | < | != )', condi)
    register = condition_split[0]
    comparison = condition_split[1].strip() # again remove whitespace
    target = int(condition_split[2])
    condition = Condition(register, comparison, target)

    instruction = Instruction(reg_name, operation, increment, condition)
    return instruction

def conduct_instruction(instruction: Instruction) -> None:
    ops = {"==": operator.eq, ">=": operator.ge, "<=": operator.le, "<": operator.lt, ">": operator.gt,
           "!=": operator.ne}
    max_value = int(-100000)
    registers = defaultdict(int)
    for instruction in instructions:
        #first determine if we want to do anything
        condition = instruction.Condition


        value = registers.get(condition.register, 0)
        print("value in register: "+ condition.register + " " + str(value) + condition.comparison + str(condition.target))


        if ops[condition.comparison](value, condition.target):
            print("condition met")
            reg_value = registers.get(instruction.register, 0)
            if instruction.operation == 'inc':
                registers[instruction.register] = reg_value + instruction.increment
                print(instruction.register + " set to: " + str(
                    registers[instruction.register]) + "should be: " + str(reg_value + instruction.increment))
            elif instruction.operation == 'dec':
                registers[instruction.register] = reg_value - instruction.increment
                print(instruction.register + " set to: " + str(registers[instruction.register]) + "should be: " + str(reg_value - instruction.increment))
            #print(instruction.register + " set to: " + str(registers[instruction.register]))
        else:
            print("condition not met")

        print(registers.values())
        if max_value < registers[instruction.register]:
            max_value = max(registers.values())

    print(max_value)
    return registers

if __name__ == "__main__":
    with open("day8_input.txt") as f:
        instructions = [create_instruction(line.strip()) for line in f]

    registers = conduct_instruction(instructions)
    print(max(registers.values()))

