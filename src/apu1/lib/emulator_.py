class Emulator():
    def __init__(self, args):
        # pull in args
        self._debug = args.debug
        self._verbose = args.verbose  
        self._step = args.step 

        # setup cpu, bus, disp, and kbd
        self._bus = Bus(args)
        self._cpu = Six502(args)
        self._disp = Display(args)
        self._kbd = Keyboard(args)