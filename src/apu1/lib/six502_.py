class Six502():
    def __init__(self, args):
        # pull in args
        self._debug = args.debug
        self._verbose = args.verbose  

        # registers
        self._registers = {
            "ACC"   : 0x00,
            "X" : 0x00,
            "Y" : 0x00,
            "STK"   : 0x00,
            "STA"   : 0x20, # N Negative, V Overflow, _ - ignored, 
                                # B - Break, D - Decimal , 
                                # I - Interrupt (IRQ disable), 
                                # Z - Zero, C - Carry
            "PC": 0xfffc
        }

        # instructions
        self._instructions = [
            ["BRK",  self._IMPL,  self._BRK],
            ["BPL",  self._REL,  self._BPL],
            ["JSR",  self._ABS,  self._JSR],
            ["BMI",  self._REL,  self._BMI],
            ["RTI",  self._IMPL,  self._RTI],
            ["BVC",  self._REL,  self._BVC],
            ["RTS",  self._IMPL,  self._RTS],
            ["BVS",  self._REL,  self._BVS],
            ["NOP",  self._IMPL,  self._NOP],
            ["BCC",  self._REL,  self._BCC],
            ["LDY",  self._IMM,  self._LDY],
            ["BCS",  self._REL,  self._BCS],
            ["CPY",  self._IMM,  self._CPY],
            ["BNE",  self._REL,  self._BNE],
            ["CPX",  self._IMM,  self._CPX],
            ["BEQ",  self._REL,  self._BEQ],
            ["ORA",  self._X_IND,  self._ORA],
            ["ORA",  self._IND_Y,  self._ORA],
            ["AND",  self._X_IND,  self._AND],
            ["AND",  self._IND_Y,  self._AND],
            ["EOR",  self._X_IND,  self._EOR],
            ["EOR",  self._IND_Y,  self._EOR],
            ["ADC",  self._X_IND,  self._ADC],
            ["ADC",  self._IND_Y,  self._ADC],
            ["STA",  self._X_IND,  self._STA],
            ["STA",  self._IND_Y,  self._STA],
            ["LDA",  self._X_IND,  self._LDA],
            ["LDA",  self._IND_Y,  self._LDA],
            ["CMP",  self._X_IND,  self._CMP],
            ["CMP",  self._IND_Y,  self._CMP],
            ["SBC",  self._X_IND,  self._SBC],
            ["SBC",  self._IND_Y,  self._SBC],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["LDX",  self._IMM,  self._LDX],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["BIT",  self._ZPG,  self._BIT],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["STY",  self._ZPG,  self._STY],
            ["STY",  self._ZPG_X,  self._STY],
            ["LDY",  self._ZPG,  self._LDY],
            ["LDY",  self._ZPG_X,  self._LDY],
            ["CPY",  self._ZPG,  self._CPY],
            ["NOP",  self._IMPL,  self._NOP],
            ["CPX",  self._ZPG,  self._CPX],
            ["NOP",  self._IMPL,  self._NOP],
            ["ORA",  self._ZPG,  self._ORA],
            ["ORA",  self._ZPG_X,  self._ORA],
            ["AND",  self._ZPG,  self._AND],
            ["AND",  self._ZPG_X,  self._AND],
            ["EOR",  self._ZPG,  self._EOR],
            ["EOR",  self._ZPG_X,  self._EOR],
            ["ADC",  self._ZPG,  self._ADC],
            ["ADC",  self._ZPG_X,  self._ADC],
            ["STA",  self._ZPG,  self._STA],
            ["STA",  self._ZPG_X,  self._STA],
            ["LDA",  self._ZPG,  self._LDA],
            ["LDA",  self._ZPG_X,  self._LDA],
            ["CMP",  self._ZPG,  self._CMP],
            ["CMP",  self._ZPG_X,  self._CMP],
            ["SBC",  self._ZPG,  self._SBC],
            ["SBC",  self._ZPG_X,  self._SBC],
            ["ASL",  self._ZPG,  self._ASL],
            ["ASL",  self._ZPG_X,  self._ASL],
            ["ROL",  self._ZPG,  self._ROL],
            ["ROL",  self._ZPG_X,  self._ROL],
            ["LSR",  self._ZPG,  self._LSR],
            ["LSR",  self._ZPG_X,  self._LSR],
            ["ROR",  self._ZPG,  self._ROR],
            ["ROR",  self._ZPG_X,  self._ROR],
            ["STX",  self._ZPG,  self._STX],
            ["STX",  self._ZPG_Y,  self._STX],
            ["LDX",  self._ZPG,  self._LDX],
            ["LDX",  self._ZPG_Y,  self._LDX],
            ["DEC",  self._ZPG,  self._DEC],
            ["DEC",  self._ZPG_X,  self._DEC],
            ["INC",  self._ZPG,  self._INC],
            ["INC",  self._ZPG_X,  self._INC],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["PHP",  self._IMPL,  self._PHP],
            ["CLC",  self._IMPL,  self._CLC],
            ["PLP",  self._IMPL,  self._PLP],
            ["SEC",  self._IMPL,  self._SEC],
            ["PHA",  self._IMPL,  self._PHA],
            ["CLI",  self._IMPL,  self._CLI],
            ["PLA",  self._IMPL,  self._PLA],
            ["SEI",  self._IMPL,  self._SEI],
            ["DEY",  self._IMPL,  self._DEY],
            ["TYA",  self._IMPL,  self._TYA],
            ["TAY",  self._IMPL,  self._TAY],
            ["CLV",  self._IMPL,  self._CLV],
            ["INY",  self._IMPL,  self._INY],
            ["CLD",  self._IMPL,  self._CLD],
            ["INX",  self._IMPL,  self._INX],
            ["SED",  self._IMPL,  self._SED],
            ["ORA",  self._IMM,  self._ORA],
            ["ORA",  self._ABS_Y,  self._ORA],
            ["AND",  self._IMM,  self._AND],
            ["AND",  self._ABS_Y,  self._AND],
            ["EOR",  self._IMM,  self._EOR],
            ["EOR",  self._ABS_Y,  self._EOR],
            ["ADC",  self._IMM,  self._ADC],
            ["ADC",  self._ABS_Y,  self._ADC],
            ["NOP",  self._IMPL,  self._NOP],
            ["STA",  self._ABS_Y,  self._STA],
            ["LDA",  self._IMM,  self._LDA],
            ["LDA",  self._ABS_Y,  self._LDA],
            ["CMP",  self._IMM,  self._CMP],
            ["CMP",  self._ABS_Y,  self._CMP],
            ["SBC",  self._IMM,  self._SBC],
            ["SBC",  self._ABS_Y,  self._SBC],
            ["ASL",  self._A,  self._ASL],
            ["NOP",  self._IMPL,  self._NOP],
            ["ROL",  self._A,  self._ROL],
            ["NOP",  self._IMPL,  self._NOP],
            ["LSR",  self._A,  self._LSR],
            ["NOP",  self._IMPL,  self._NOP],
            ["ROR",  self._A,  self._ROR],
            ["NOP",  self._IMPL,  self._NOP],
            ["TXA",  self._IMPL,  self._TXA],
            ["TXS",  self._IMPL,  self._TXS],
            ["TAX",  self._IMPL,  self._TAX],
            ["TSX",  self._IMPL,  self._TSX],
            ["DEX",  self._IMPL,  self._DEX],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["NOP",  self._IMPL,  self._NOP],
            ["BIT",  self._ABS,  self._BIT],
            ["NOP",  self._IMPL,  self._NOP],
            ["JMP",  self._ABS,  _JMP],
            ["NOP",  self._IMPL,  _NOP],
            ["JMP",  self._IND,  _JMP],
            ["NOP",  self._IMPL,  _NOP],
            ["STY",  self._ABS,  _STY],
            ["NOP",  self._IMPL,  _NOP],
            ["LDY",  self._ABS,  _LDY],
            ["LDY",  self._ABS_X,  _LDY],
            ["CPY",  self._ABS,  _CPY],
            ["NOP",  self._IMPL,  _NOP],
            ["CPX",  self._ABS,  _CPX],
            ["NOP",  self._IMPL,  _NOP],
            ["ORA",  self._ABS,  _ORA],
            ["ORA",  self._ABS_X,  _ORA],
            ["AND",  self._ABS,  _AND],
            ["AND",  self._ABS_X,  _AND],
            ["EOR",  self._ABS,  _EOR],
            ["EOR",  self._ABS_X,  _EOR],
            ["ADC",  self._ABS,  _ADC],
            ["ADC",  self._ABS_X,  _ADC],
            ["STA",  self._ABS,  _STA],
            ["STA",  self._ABS_X,  _STA],
            ["LDA",  self._ABS,  _LDA],
            ["LDA",  self._ABS_X,  _LDA],
            ["CMP",  self._ABS,  _CMP],
            ["CMP",  self._ABS_X,  _CMP],
            ["SBC",  self._ABS,  self._SBC],
            ["SBC",  self._ABS_X,  self._SBC],
            ["ASL",  self._ABS,  self._ASL],
            ["ASL",  self._ABS_X,  self._ASL],
            ["ROL",  self._ABS,  self._ROL],
            ["ROL",  self._ABS_X,  self._ROL],
            ["LSR",  self._ABS,  self._LSR],
            ["LSR",  self._ABS_X,  self._LSR],
            ["ROR",  self._ABS,  self._ROR],
            ["ROR",  self._ABS_X,  self._ROR],
            ["STX",  self._ABS,  self._STX],
            ["NOP",  self._IMPL,  self._NOP],
            ["LDX",  self._ABS,  self._LDX],
            ["LDX",  self._ABS_Y,  self._LDX],
            ["DEC",  self._ABS,  self._DEC],
            ["DEC",  self._ABS_X,  self._DEC],
            ["INC",  self._ABS,  self._INC],
            ["INC",  self._ABS_X,  self._INC],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP],
            ["NOP",  self._IMPL, self._NOP]
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