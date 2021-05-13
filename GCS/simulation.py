"""
@file simulation.py
@author Joshua Tenorio

Functionality and implementation of Simulation Mode
"""

# TODO: add a way to specify the filename for simulation file


def parse_sim_profile(file_name):
    # figure out file extension bc not sure if it will be in .txt or .csv
    f_extension = file_name.split(".")[1]
    file = open(file_name, mode = "r")
    if f_extension == "txt": # case 1: txt file
        data = []
        for line in file:
            if line[0].strip() != "#" or line.strip() == "":
                if line.strip() == "### End of file ###":
                    break
                args = line.split(",")
                if len(args) > 1:
                    data.append(args[3])
        
        file.close()
        return data

    elif f_extension == "csv": # case 2: csv file
        pass
    else:
        print("Profile is not a .txt or .csv file")
        return 0

# returns the nth packet in the sim profile to transmit to container
def get_next_packet(n):
    sim_profile = parse_sim_profile("simp_cmd_example.txt")
    if n < 0 or n > sim_profile.__len__:
        err_msg = "SIM ERR: attempted to retrieve a packet out of profile's bounds"
        print(err_msg)
        return err_msg
    
    # if n is a valid packet num, return the packet
    return sim_profile[n]