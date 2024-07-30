class Bus():
    def __init__(self, args):
        # pull in args
        self._debug = args.debug
        self._verbose = args.verbose   

        self._ROM_file_path = args.filename
        self._memory_size = args._memory_size

        # initialize ROM
        self._memory = [0] * self._memory_size

        # read in ROM
        if self._ROM_file_path != "":
            with open(self._ROM_file_path, "rb") as file:
                hex_data = file.read().hex()
                self._memory = [int(hex_data[i:i+2], 16) 
                                for i in range(0, len(hex_data), 2)]

    def read(self, memAddr):
        return self._memory[memAddr]
    
    def write(self, memAddr, val):
        self._memory[memAddr] = val