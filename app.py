from mypythontools import pyvueel
from mypythontools.pyvueel import expose

# Expose python functions to Js with decorator
@expose
def load_data(neznama):
    # You can return dict - will be object in js
    # You can return list - will be an array in js

    print(666)

    return neznama

    # return {'Hello': 1}


# End of file
if __name__ == '__main__':
    pyvueel.run_gui()
