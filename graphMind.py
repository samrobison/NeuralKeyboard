#!/usr/bin/python

import graphTypes,sys

def main(argv):
    if argv[0] == "abg":
        graphTypes.alphaBetaGamma()
    if argv[0] == 'am':
        graphTypes.attentionMeditation()
        
if __name__ == "__main__":
   main(sys.argv[1:])
