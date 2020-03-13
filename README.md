# gradient_descent
A generalised gradient descent module for hamiltonian minimization in any system

The main function of the module is GradDescent which takes the following arguments:
1. Init : Initial State of the system (any type supported by Mutator and Printer functions). Eg - Numpy arrays
2. Mutator : A function that takes in system state and generates neighboring system states. (Inputs : System State)
3. H : Hamiltonian function. (Inputs : System State)
4. ofile : An output file to write the results of GradDescent. (Note: This output file should already be open for writing)
5. Printer : A Printer function that converts system state to a string that can be written to the output file.


Usage:
```python
import gradient_descent

outputfile = open(<outputfilename>,"w+")

GradDescent(Init,Mutator,H,outputfile,Printer)

outputfile.close()
```
Contact kbhaskar AT iisc DOT ac DOT in


