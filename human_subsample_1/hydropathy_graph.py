#!/usr/bin/env python
#!/usr/bin/env python
import sys
# this prints the usage statement if there are less than 7 Arguments
# this creates usage statement then exits the system once done
if (len(sys.argv)) < 6:
    print ""
    print "usage: hydropathyEDC.py -i <input file> -o <output file> -v <threshold value> w < window size>"
    print "-i: .fasta file"
    print "-v: threshold value"
    print "-w: window size"
    #print "-o: output file"
    print ""
    sys.exit()

# this creates the arguments in the module
# for any argument in list of arguments in sys.argv
for i in range(len(sys.argv)):
    # sets the input directory to the first argument that follows -i
    if sys.argv[i] == "-i":
        InSeqFileName = sys.argv[i+1]
    # sets the output file name to the first argument that follows -o
    #elif sys.argv[i] == "-o":
        #OutFileName = sys.argv[i+1]
    # sets the threshold value equal to the first argument that follows -v
    elif sys.argv[i] == "-v":
        thresholdvalue = int(float(sys.argv[i+1]))
    # sets the window size equal to the first argument that follows -w
    elif sys.argv[i] == "-w":
        window_size = int(float(sys.argv[i+1]))
    #elif sys.argv[i] == "-o":
        OutFileName = sys.argv[i+1]
#Working template of hydropathy score calculation script
#You need to put in comments for every line

InFileName = "amino_acid_hydropathy_values.txt"
InFile = open(InFileName, 'r')
Data=[]
Hydropathy={}
LineNumber = 0

for Line in InFile:
    if(LineNumber>0):
        Line = Line.strip("\n")
        Data = Line.split(",")
        Hydropathy[Data[1]]=float(Data[2])
    LineNumber = LineNumber + 1
InFile.close()


window=int(window)
Value=0
window_counter=0

InSeqFile = open(InSeqFileName, 'r')
LineNumber = 0

for Line in InSeqFile:
    if(LineNumber>0):
        ProtSeq=Line.strip('\n')
    LineNumber = LineNumber + 1
InSeqFile.close()

OutFileName = InSeqFileName.strip('.fasta') + ".output.csv"
OutFile = open(OutFileName,"w")

for i in range(len(ProtSeq)):
    Value+=Hydropathy[ProtSeq[i]]
    if(i>(window-1) and i<=(len(ProtSeq)-window)):
        Value=Value-Hydropathy[ProtSeq[i-window]]
        OutString = "%d,%.2f" % (window_counter, Value)
        OutFile.write(OutString + "\n")

    window_counter+=1

OutFile.close()
