# Leo colorizer control file for assembly_r2000 mode.
# This file is in the public domain.

# Properties for assembly_r2000 mode.
properties = {
    "blockComment": "#",
    "wordBreakChars": ",()",
}

# Attributes dict for assembly_r2000_main ruleset.
assembly_r2000_main_attributes_dict = {
    "default": "null",
    "digit_re": "",
    "escape": "\\",
    "highlight_digits": "true",
    "ignore_case": "true",
    "no_word_sep": "",
}

# Dictionary of attributes dictionaries for assembly_r2000 mode.
attributesDictDict = {
    "assembly_r2000_main": assembly_r2000_main_attributes_dict,
}

# Keywords dict for assembly_r2000_main ruleset.
assembly_r2000_main_keywords_dict = {
    "$a0": "keyword2",
    "$a1": "keyword2",
    "$a2": "keyword2",
    "$a3": "keyword2",
    "$at": "keyword2",
    "$f0": "keyword3",
    "$f1": "keyword3",
    "$f10": "keyword3",
    "$f11": "keyword3",
    "$f12": "keyword3",
    "$f13": "keyword3",
    "$f14": "keyword3",
    "$f15": "keyword3",
    "$f16": "keyword3",
    "$f17": "keyword3",
    "$f18": "keyword3",
    "$f19": "keyword3",
    "$f2": "keyword3",
    "$f20": "keyword3",
    "$f21": "keyword3",
    "$f22": "keyword3",
    "$f23": "keyword3",
    "$f24": "keyword3",
    "$f25": "keyword3",
    "$f26": "keyword3",
    "$f27": "keyword3",
    "$f28": "keyword3",
    "$f29": "keyword3",
    "$f3": "keyword3",
    "$f30": "keyword3",
    "$f31": "keyword3",
    "$f4": "keyword3",
    "$f5": "keyword3",
    "$f6": "keyword3",
    "$f7": "keyword3",
    "$f8": "keyword3",
    "$f9": "keyword3",
    "$fp": "keyword2",
    "$k0": "keyword2",
    "$k1": "keyword2",
    "$ra": "keyword2",
    "$s0": "keyword2",
    "$s1": "keyword2",
    "$s2": "keyword2",
    "$s3": "keyword2",
    "$s4": "keyword2",
    "$s5": "keyword2",
    "$s6": "keyword2",
    "$s7": "keyword2",
    "$sp": "keyword2",
    "$t1": "keyword2",
    "$t2": "keyword2",
    "$t3": "keyword2",
    "$t4": "keyword2",
    "$t5": "keyword2",
    "$t6": "keyword2",
    "$t7": "keyword2",
    "$t8": "keyword2",
    "$t9": "keyword2",
    "$v0": "keyword2",
    "$v1": "keyword2",
    "$zero": "keyword2",
    ".align": "keyword1",
    ".ascii": "keyword1",
    ".asciiz": "keyword1",
    ".byte": "keyword1",
    ".data": "keyword1",
    ".double": "keyword1",
    ".extern": "keyword1",
    ".float": "keyword1",
    ".globl": "keyword1",
    ".half": "keyword1",
    ".kdata": "keyword1",
    ".ktext": "keyword1",
    ".space": "keyword1",
    ".text": "keyword1",
    ".word": "keyword1",
    "abs.d": "function",
    "abs.s": "function",
    "add": "function",
    "add.d": "function",
    "add.s": "function",
    "addi": "function",
    "addiu": "function",
    "addu": "function",
    "and": "function",
    "andi": "function",
    "b": "function",
    "bczf": "function",
    "bczt": "function",
    "beq": "function",
    "beqz": "function",
    "bge": "function",
    "bgeu": "function",
    "bgez": "function",
    "bgezal": "function",
    "bgt": "function",
    "bgtu": "function",
    "bgtz": "function",
    "ble": "function",
    "bleu": "function",
    "blez": "function",
    "blt": "function",
    "bltu": "function",
    "bltz": "function",
    "bltzal": "function",
    "blu": "function",
    "bne": "function",
    "bnez": "function",
    "break": "function",
    "c.eq.d": "function",
    "c.eq.s": "function",
    "c.le.d": "function",
    "c.le.s": "function",
    "c.lt.d": "function",
    "c.lt.s": "function",
    "cbt.d.w": "function",
    "cvt.d.s": "function",
    "cvt.s.d": "function",
    "cvt.s.w": "function",
    "cvt.w.d": "function",
    "cvt.w.s": "function",
    "div": "function",
    "div.d": "function",
    "div.s": "function",
    "divu": "function",
    "j": "function",
    "jal": "function",
    "jalr": "function",
    "jr": "function",
    "l.d": "function",
    "l.s": "function",
    "la": "function",
    "lb": "function",
    "lh": "function",
    "lhu": "function",
    "li": "function",
    "lui": "function",
    "lw": "function",
    "lwcz": "function",
    "lwl": "function",
    "lwr": "function",
    "mfc1.d": "function",
    "mfcz": "function",
    "mfhi": "function",
    "mflo": "function",
    "mov.d": "function",
    "mov.s": "function",
    "move": "function",
    "mtcz": "function",
    "mthi": "function",
    "mtlo": "function",
    "mul": "function",
    "mul.d": "function",
    "mul.s": "function",
    "mulo": "function",
    "mulou": "function",
    "mult": "function",
    "multu": "function",
    "neg": "function",
    "neg.d": "function",
    "neg.s": "function",
    "negu": "function",
    "nop": "function",
    "nor": "function",
    "not": "function",
    "or": "function",
    "ori": "function",
    "rem": "function",
    "remu": "function",
    "rfe": "function",
    "rol": "function",
    "ror": "function",
    "s.d": "function",
    "s.s": "function",
    "sb": "function",
    "sd": "function",
    "seq": "function",
    "sge": "function",
    "sgt": "function",
    "sgtu": "function",
    "sh": "function",
    "sle": "function",
    "sleu": "function",
    "sll": "function",
    "sllv": "function",
    "slt": "function",
    "slti": "function",
    "sltiu": "function",
    "sltu": "function",
    "sne": "function",
    "sra": "function",
    "srav": "function",
    "srl": "function",
    "srlv": "function",
    "sub": "function",
    "sub.d": "function",
    "sub.s": "function",
    "subu": "function",
    "sw": "function",
    "swcz": "function",
    "swl": "function",
    "swr": "function",
    "syscall": "function",
    "ulh": "function",
    "ulhu": "function",
    "ulw": "function",
    "ush": "function",
    "usw": "function",
    "xor": "function",
    "xori": "function",
}

# Dictionary of keywords dictionaries for assembly_r2000 mode.
keywordsDictDict = {
    "assembly_r2000_main": assembly_r2000_main_keywords_dict,
}

# Rules for assembly_r2000_main ruleset.

def assembly_r2000_rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def assembly_r2000_rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def assembly_r2000_rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def assembly_r2000_rule3(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def assembly_r2000_rule4(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for assembly_r2000_main ruleset.
rulesDict1 = {
    "\"": [assembly_r2000_rule2,],
    "#": [assembly_r2000_rule0,],
    "$": [assembly_r2000_rule4,],
    "'": [assembly_r2000_rule1,],
    ".": [assembly_r2000_rule4,],
    "0": [assembly_r2000_rule4,],
    "1": [assembly_r2000_rule4,],
    "2": [assembly_r2000_rule4,],
    "3": [assembly_r2000_rule4,],
    "4": [assembly_r2000_rule4,],
    "5": [assembly_r2000_rule4,],
    "6": [assembly_r2000_rule4,],
    "7": [assembly_r2000_rule4,],
    "8": [assembly_r2000_rule4,],
    "9": [assembly_r2000_rule4,],
    ":": [assembly_r2000_rule3,],
    "@": [assembly_r2000_rule4,],
    "A": [assembly_r2000_rule4,],
    "B": [assembly_r2000_rule4,],
    "C": [assembly_r2000_rule4,],
    "D": [assembly_r2000_rule4,],
    "E": [assembly_r2000_rule4,],
    "F": [assembly_r2000_rule4,],
    "G": [assembly_r2000_rule4,],
    "H": [assembly_r2000_rule4,],
    "I": [assembly_r2000_rule4,],
    "J": [assembly_r2000_rule4,],
    "K": [assembly_r2000_rule4,],
    "L": [assembly_r2000_rule4,],
    "M": [assembly_r2000_rule4,],
    "N": [assembly_r2000_rule4,],
    "O": [assembly_r2000_rule4,],
    "P": [assembly_r2000_rule4,],
    "Q": [assembly_r2000_rule4,],
    "R": [assembly_r2000_rule4,],
    "S": [assembly_r2000_rule4,],
    "T": [assembly_r2000_rule4,],
    "U": [assembly_r2000_rule4,],
    "V": [assembly_r2000_rule4,],
    "W": [assembly_r2000_rule4,],
    "X": [assembly_r2000_rule4,],
    "Y": [assembly_r2000_rule4,],
    "Z": [assembly_r2000_rule4,],
    "a": [assembly_r2000_rule4,],
    "b": [assembly_r2000_rule4,],
    "c": [assembly_r2000_rule4,],
    "d": [assembly_r2000_rule4,],
    "e": [assembly_r2000_rule4,],
    "f": [assembly_r2000_rule4,],
    "g": [assembly_r2000_rule4,],
    "h": [assembly_r2000_rule4,],
    "i": [assembly_r2000_rule4,],
    "j": [assembly_r2000_rule4,],
    "k": [assembly_r2000_rule4,],
    "l": [assembly_r2000_rule4,],
    "m": [assembly_r2000_rule4,],
    "n": [assembly_r2000_rule4,],
    "o": [assembly_r2000_rule4,],
    "p": [assembly_r2000_rule4,],
    "q": [assembly_r2000_rule4,],
    "r": [assembly_r2000_rule4,],
    "s": [assembly_r2000_rule4,],
    "t": [assembly_r2000_rule4,],
    "u": [assembly_r2000_rule4,],
    "v": [assembly_r2000_rule4,],
    "w": [assembly_r2000_rule4,],
    "x": [assembly_r2000_rule4,],
    "y": [assembly_r2000_rule4,],
    "z": [assembly_r2000_rule4,],
}

# x.rulesDictDict for assembly_r2000 mode.
rulesDictDict = {
    "assembly_r2000_main": rulesDict1,
}

# Import dict for assembly_r2000 mode.
importDict = {}

