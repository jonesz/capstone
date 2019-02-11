# Capstone Python bindings, Ethan Jones <etn.jones@gmail.com>

import ctypes
from . import copy_ctypes_list
from .riscv_const import *

#define the API
class RiscvOpMem(ctypes.Structure):
    _fields_ = (
        ('base', ctypes.c_uint),
        ('disp', ctypes.c_int64),
    )

class RiscvOpValue(ctypes.Union):
    _fields_ = (
        ('reg', ctypes.c_uint),
        ('imm', ctypes.c_int64),
        ('mem', RiscvOpMem),
    )

class RiscvOp(ctypes.Structure):
    _fields_ = (
        ('type', ctypes.c_uint),
        ('value', RiscvOpValue),
    )

    @property
    def imm(self):
        return self.value.imm

    @property
    def reg(self):
        return self.value.reg

    @property
    def mem(self):
        return self.value.mem

class CsRiscv(ctypes.Structure):
    _fields_ = (
        ('op_count', ctypes.c_uint8),
        ('operands', RiscvOp * 8),
    )

def get_arch_info(a):
    return copy_ctypes_list(a.operands[:a.op_count])

