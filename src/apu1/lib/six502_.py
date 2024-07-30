class Six502():
    def __init__(self, args):
        # pull in args
        self._debug = args.debug
        self._verbose = args.verbose  

        # registers
        self._registers = {
        ACC"   : 0x00,
        X : 0x00,
        Y : 0x00,
        STK"   : 0x00,
        STA"   : 0x20, # N Negative, V Overflow, _ - ignored, 
                            # B - Break, D - Decimal , 
                            # I - Interrupt (IRQ disable), 
                            # Z - Zero, C - Carry
        PC: 0xfffc
        }

        # instructions
        self._instructions = [
            ["BRK",  _IMPL,  _BRK],
            ["BPL",  _REL,  _BPL],
            ["JSR",  _ABS,  _JSR],
            ["BMI",  _REL,  _BMI],
            ["RTI",  _IMPL,  _RTI],
            ["BVC",  _REL,  _BVC],
            ["RTS",  _IMPL,  _RTS],
            ["BVS",  _REL,  _BVS],
            ["NOP",  _IMPL,  _NOP],
            ["BCC",  _REL,  _BCC],
            ["LDY",  _IMM,  _LDY],
            ["BCS",  _REL,  _BCS],
            ["CPY",  _IMM,  _CPY],
            ["BNE",  _REL,  _BNE],
            ["CPX",  _IMM,  _CPX],
            ["BEQ",  _REL,  _BEQ],
            ["ORA",  _X_IND,  _ORA],
            ["ORA",  _IND_Y,  _ORA],
            ["AND",  _X_IND,  _AND],
            ["AND",  _IND_Y,  _AND],
            ["EOR",  _X_IND,  _EOR],
            ["EOR",  _IND_Y,  _EOR],
            ["ADC",  _X_IND,  _ADC],
            ["ADC",  _IND_Y,  _ADC],
            ["STA",  _X_IND,  _STA],
            ["STA",  _IND_Y,  _STA],
            ["LDA",  _X_IND,  _LDA],
            ["LDA",  _IND_Y,  _LDA],
            ["CMP",  _X_IND,  _CMP],
            ["CMP",  _IND_Y,  _CMP],
            ["SBC",  _X_IND,  _SBC],
            ["SBC",  _IND_Y,  _SBC],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["LDX",  _IMM,  _LDX],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["BIT",  _ZPG,  _BIT],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["STY",  _ZPG,  _STY],
            ["STY",  _ZPG_X,  _STY],
            ["LDY",  _ZPG,  _LDY],
            ["LDY",  _ZPG_X,  _LDY],
            ["CPY",  _ZPG,  _CPY],
            ["NOP",  _IMPL,  _NOP],
            ["CPX",  _ZPG,  _CPX],
            ["NOP",  _IMPL,  _NOP],
            ["ORA",  _ZPG,  _ORA],
            ["ORA",  _ZPG_X,  _ORA],
            ["AND",  _ZPG,  _AND],
            ["AND",  _ZPG_X,  _AND],
            ["EOR",  _ZPG,  _EOR],
            ["EOR",  _ZPG_X,  _EOR],
            ["ADC",  _ZPG,  _ADC],
            ["ADC",  _ZPG_X,  _ADC],
            ["STA",  _ZPG,  _STA],
            ["STA",  _ZPG_X,  _STA],
            ["LDA",  _ZPG,  _LDA],
            ["LDA",  _ZPG_X,  _LDA],
            ["CMP",  _ZPG,  _CMP],
            ["CMP",  _ZPG_X,  _CMP],
            ["SBC",  _ZPG,  _SBC],
            ["SBC",  _ZPG_X,  _SBC],
            ["ASL",  _ZPG,  _ASL],
            ["ASL",  _ZPG_X,  _ASL],
            ["ROL",  _ZPG,  _ROL],
            ["ROL",  _ZPG_X,  _ROL],
            ["LSR",  _ZPG,  _LSR],
            ["LSR",  _ZPG_X,  _LSR],
            ["ROR",  _ZPG,  _ROR],
            ["ROR",  _ZPG_X,  _ROR],
            ["STX",  _ZPG,  _STX],
            ["STX",  _ZPG_Y,  _STX],
            ["LDX",  _ZPG,  _LDX],
            ["LDX",  _ZPG_Y,  _LDX],
            ["DEC",  _ZPG,  _DEC],
            ["DEC",  _ZPG_X,  _DEC],
            ["INC",  _ZPG,  _INC],
            ["INC",  _ZPG_X,  _INC],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["PHP",  _IMPL,  _PHP],
            ["CLC",  _IMPL,  _CLC],
            ["PLP",  _IMPL,  _PLP],
            ["SEC",  _IMPL,  _SEC],
            ["PHA",  _IMPL,  _PHA],
            ["CLI",  _IMPL,  _CLI],
            ["PLA",  _IMPL,  _PLA],
            ["SEI",  _IMPL,  _SEI],
            ["DEY",  _IMPL,  _DEY],
            ["TYA",  _IMPL,  _TYA],
            ["TAY",  _IMPL,  _TAY],
            ["CLV",  _IMPL,  _CLV],
            ["INY",  _IMPL,  _INY],
            ["CLD",  _IMPL,  _CLD],
            ["INX",  _IMPL,  _INX],
            ["SED",  _IMPL,  _SED],
            ["ORA",  _IMM,  _ORA],
            ["ORA",  _ABS_Y,  _ORA],
            ["AND",  _IMM,  _AND],
            ["AND",  _ABS_Y,  _AND],
            ["EOR",  _IMM,  _EOR],
            ["EOR",  _ABS_Y,  _EOR],
            ["ADC",  _IMM,  _ADC],
            ["ADC",  _ABS_Y,  _ADC],
            ["NOP",  _IMPL,  _NOP],
            ["STA",  _ABS_Y,  _STA],
            ["LDA",  _IMM,  _LDA],
            ["LDA",  _ABS_Y,  _LDA],
            ["CMP",  _IMM,  _CMP],
            ["CMP",  _ABS_Y,  _CMP],
            ["SBC",  _IMM,  _SBC],
            ["SBC",  _ABS_Y,  _SBC],
            ["ASL",  _A,  _ASL],
            ["NOP",  _IMPL,  _NOP],
            ["ROL",  _A,  _ROL],
            ["NOP",  _IMPL,  _NOP],
            ["LSR",  _A,  _LSR],
            ["NOP",  _IMPL,  _NOP],
            ["ROR",  _A,  _ROR],
            ["NOP",  _IMPL,  _NOP],
            ["TXA",  _IMPL,  _TXA],
            ["TXS",  _IMPL,  _TXS],
            ["TAX",  _IMPL,  _TAX],
            ["TSX",  _IMPL,  _TSX],
            ["DEX",  _IMPL,  _DEX],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["BIT",  _ABS,  _BIT],
            ["NOP",  _IMPL,  _NOP],
            ["JMP",  _ABS,  _JMP],
            ["NOP",  _IMPL,  _NOP],
            ["JMP",  _IND,  _JMP],
            ["NOP",  _IMPL,  _NOP],
            ["STY",  _ABS,  _STY],
            ["NOP",  _IMPL,  _NOP],
            ["LDY",  _ABS,  _LDY],
            ["LDY",  _ABS_X,  _LDY],
            ["CPY",  _ABS,  _CPY],
            ["NOP",  _IMPL,  _NOP],
            ["CPX",  _ABS,  _CPX],
            ["NOP",  _IMPL,  _NOP],
            ["ORA",  _ABS,  _ORA],
            ["ORA",  _ABS_X,  _ORA],
            ["AND",  _ABS,  _AND],
            ["AND",  _ABS_X,  _AND],
            ["EOR",  _ABS,  _EOR],
            ["EOR",  _ABS_X,  _EOR],
            ["ADC",  _ABS,  _ADC],
            ["ADC",  _ABS_X,  _ADC],
            ["STA",  _ABS,  _STA],
            ["STA",  _ABS_X,  _STA],
            ["LDA",  _ABS,  _LDA],
            ["LDA",  _ABS_X,  _LDA],
            ["CMP",  _ABS,  _CMP],
            ["CMP",  _ABS_X,  _CMP],
            ["SBC",  _ABS,  _SBC],
            ["SBC",  _ABS_X,  _SBC],
            ["ASL",  _ABS,  _ASL],
            ["ASL",  _ABS_X,  _ASL],
            ["ROL",  _ABS,  _ROL],
            ["ROL",  _ABS_X,  _ROL],
            ["LSR",  _ABS,  _LSR],
            ["LSR",  _ABS_X,  _LSR],
            ["ROR",  _ABS,  _ROR],
            ["ROR",  _ABS_X,  _ROR],
            ["STX",  _ABS,  _STX],
            ["NOP",  _IMPL,  _NOP],
            ["LDX",  _ABS,  _LDX],
            ["LDX",  _ABS_Y,  _LDX],
            ["DEC",  _ABS,  _DEC],
            ["DEC",  _ABS_X,  _DEC],
            ["INC",  _ABS,  _INC],
            ["INC",  _ABS_X,  _INC],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP],
            ["NOP",  _IMPL,  _NOP]
        ]

    def _IMPL(self):
        pass

    def _REL (self):
            pass

    def _ABS (self):
            pass

    def _IMM (self):
            pass

    def _X_IND(self):
            pass

    def _IND_Y(self):
            pass

    def _ZPG (self):
            pass

    def _ZPG_X(self):
            pass

    def _ZPG_Y(self):
            pass

    def _ABS_Y(self):
            pass

    def _A(self):
            pass

    def _IND (self):
            pass

    def _ABS_X(self):
            pass

    def _BRK(self):
        pass

    def _BPL(self):
            pass

    def _JSR(self):
            pass

    def _BMI(self):
            pass

    def _RTI(self):
            pass

    def _BVC(self):
            pass

    def _RTS(self):
            pass

    def _BVS(self):
            pass

    def _NOP(self):
            pass

    def _BCC(self):
            pass

    def _LDY(self):
            pass

    def _BCS(self):
            pass

    def _CPY(self):
            pass

    def _BNE(self):
            pass

    def _CPX(self):
            pass

    def _BEQ(self):
            pass

    def _ORA(self):
            pass

    def _AND(self):
            pass

    def _EOR(self):
            pass

    def _ADC(self):
            pass

    def _STA(self):
            pass

    def _LDA(self):
            pass

    def _CMP(self):
            pass

    def _SBC(self):
            pass

    def _LDX(self):
            pass

    def _BIT(self):
            pass

    def _STY(self):
            pass

    def _ASL(self):
            pass

    def _ROL(self):
            pass

    def _LSR(self):
            pass

    def _ROR(self):
            pass

    def _STX(self):
            pass

    def _DEC(self):
            pass

    def _INC(self):
            pass

    def _PHP(self):
            pass

    def _CLC(self):
            pass

    def _PLP(self):
            pass

    def _SEC(self):
            pass

    def _PHA(self):
            pass

    def _CLI(self):
            pass

    def _PLA(self):
            pass

    def _SEI(self):
            pass

    def _DEY(self):
            pass

    def _TYA(self):
            pass

    def _TAY(self):
            pass

    def _CLV(self):
            pass

    def _INY(self):
            pass

    def _CLD(self):
            pass

    def _INX(self):
            pass

    def _SED(self):
            pass

    def _TXA(self):
            pass

    def _TXS(self):
            pass

    def _TAX(self):
            pass

    def _TSX(self):
            pass

    def _DEX(self):
            pass

    def _JMP(self):
            pass











































































































































































































    def reset(self):
        self._registers = {
        ACC"   : 0x00,
        X : 0x00,
        Y : 0x00,
        STK"   : 0x00,
        STA"   : 0x20, # N Negative, V Overflow, _ - ignored, 
                            # B - Break, D - Decimal , 
                            # I - Interrupt (IRQ disable), 
                            # Z - Zero, C - Carry
        PC: 0xfffc
        }
    
    def step(self):
        opCode = self._bus.read(self._registers["PC"])
        self._registers["PC"] += 0x01