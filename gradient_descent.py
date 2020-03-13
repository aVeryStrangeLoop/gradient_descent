# Gradient descent subroutine for multistate-ising solver
# Written by Bhaskar Kumawat (github/aVeryStrangeLoop)

import numpy as np

def GradDescent(Init,Mutator,H,ofile,Printer):
    ## Gradient Descent module -- Main

    GDheader(ofile) ## Write header of gradient descent module in output file

    ## ALGORITHM
    ##  1. Create variables to store optimal state and its Energy
    optimalState = Init
    optimalEnergy = H(Init)

    stateStagnant = False
    step = 0
    print("Beginning gradient descent!")
    while not stateStagnant:
        ### Print the current state of the descent

        ## Uncomment  next line to write to file at all intermediate steps
        #PrintDescentState(ofile,step,optimalEnergy,optimalState)   
             
        print("Step: %d, Energy: %f" % (step,optimalEnergy))
        ## Get Neighbors in phase space
        neighborStates = Mutator(optimalState)
        neighborEnergy = np.zeros(len(neighborStates))
            
        ## Calculate energy of each neighbor
        for i in range(len(neighborStates)):
            neighborEnergy[i] = H(neighborStates[i])

        # Get the difference between current state energy and neighbor energy
        neighborEnergyDiff = neighborEnergy - optimalEnergy

        # Find the index of neighbor with minimum difference (max negative difference)
        idx_optimal = np.argmin(neighborEnergyDiff)

        # If that difference is zero or greater, gradient is stagnant
        # Directly break out of while loop
        if neighborEnergyDiff[idx_optimal]>=0.0:
            stateStagnant = True
            break
        
        # If some difference less than zero, move to that state
        optimalState = neighborStates[idx_optimal]
        optimalEnergy = neighborEnergy[idx_optimal]
        step +=1
    
    PrintDescentState(ofile,step,optimalEnergy,optimalState,Printer)
    ofile.write("### END OF GRADIENT DESCENT")

def GDheader(ofile):
    ofile.write("## RUNNING GRADIENT DESCENT MODULE##\n")
    ofile.write("# Written by Bhaskar Kumawat (@aVeryStrangeLoop)\n")
    ofile.write("step,opt_energy,opt_state\n")



def PrintDescentState(ofile,step,optEnergy,optState,Printer):
    ofile.write("%d,%f," % (step,optEnergy))
    ofile.write("%s\n" % Printer(optState))

    






