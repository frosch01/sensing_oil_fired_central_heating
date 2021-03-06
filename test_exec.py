import traceback

class TestExec:
    """This class enables simplyfied testing
    Initialize with a method or lambda to be called
    Execute test calling execute() method
    Test methods shall take as first parameter the instance of TestExec.
    Through the TestExec instance these methods may be called:
        report(): To report a result
        call_except(): To call a method expecting an Exception. 
                       Make use of lambda methods as required.
    """
    def __init__(self, method):
        self.method = method
        self.name = method.__qualname__
        self.success = True
        
    def __del__(self):
        print("{}: {}".format("Success" if self.success else "FAILED", self.name))
    
    def execute(self, *args, **kwargs):
        self.call_except(lambda: self.method(self, *args, **kwargs))
                
    def call_except(self, method, expected_exception=None, verbose=False):
        if expected_exception:
            try:
                method()
            except expected_exception:
                if (verbose):
                    self.report(True, "Exception rised as expected")
            except BaseException as e:
                self.report(False, "Unexpected execption caught", verbose, e)
            except:
                self.report(False, "Unknown exception caught", verbose)
            else: 
                self.report(False, "Expected exception {} was not raised".format(expected_exception), verbose)
        else:
            try:
                method()
            except BaseException as e:
                self.report(False, "Unexpected execption caught", verbose, e)
            except:
                self.report(False, "Unknown exception caught", verbose)
                 
    def report(self, success, text="", verbose=False, error=None):
        if success:
            if verbose:
                print("Success: ", end = "")
        else:
            self.success = False
            print("Failed: ", end = "")
        if not success or verbose:
            print(self.name + ": ", end = "")
        if error:
            print(text, ": ", type(error))
            traceback.print_exc()
        elif verbose or not success:
            print(text)
        elif verbose:
            print()
        if not success:
            print(traceback.format_stack(limit=2)[0])
