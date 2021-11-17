import argparse
import numpy as np
import pysam
import pysamstats

parser = argparse.ArgumentParser(description="""NM Edit Distance  -  Meriam Guellil  -  August 2019 v.2.0""",epilog="""Can be run multiple times and will append output to the same file if it was given as output. Does not overwrite.""")
parser.add_argument('-b',metavar='in.bam', dest='bams', required=True, type=str, nargs='+', help='List of sorted BAM Files')
parser.add_argument('-d',metavar='Max Range', dest='max', required=False, default=10, type=int, help='Maximum Calculated Edit Distance (default = 10).')
parser.add_argument('-o',metavar='out.csv', dest='csv', required=False, help='csv output File.')
parser.add_argument('-r',metavar='region', dest='region', required=False, type=str, nargs='+', help='Eg.: CHR1:1-10000 (seperated by spaces), can be used with the -s flag, which will output all headers and the intervals of choice.')
parser.add_argument('-s', dest='flag', action='store_true', required=False, help='Output each chromosome separately.')
parser.add_argument('-q',metavar='mapping quality', dest='mq', required=False, type=float, default=0, help='only use reads with mapping quality above specified value.')
args= parser.parse_args()

####VARIABLES
Header = ["File","Seq ID","Min MQ","Read Count","Mean ED"]
for i in range (0,(args.max+1)):
    Header.extend(("ED "+str(i),"%ED "+str(i))) 

####FUNCTIONS
def ED_List (bam,head):
    NM_list_MQ = [read.get_tag("NM") for read in bam if read.mapping_quality >= args.mq]
    ED_Dict_PERC = {x: "{0:.3f}".format((NM_list_MQ.count(x)/len(NM_list_MQ))*100) for x in range(0,(args.max+1))}
    ED_Dict_COUNT = {x: "{0:.3f}".format(NM_list_MQ.count(x)) for x in range(0,(args.max+1))}
    count = len(NM_list_MQ)
    mean= np.average(NM_list_MQ)
    Data = [str(baml),str(head),str(args.mq),str(count),str(mean)]
    print('\n>> FILE: '+baml,"[ "+str(head)+" ]",'READS: '+str(count),'MIN MQ: '+str(args.mq), sep='\t')
    if count != 0:
        for i in range(0,(args.max+1)):#filter per ED
            Data.extend((ED_Dict_COUNT[i],ED_Dict_PERC[i]))
            print(str(ED_Dict_PERC[i]) + "% of Mapped Reads Edit Distance " + str(i))
        print('\n'+'Mean Edit Distance = '+str(mean))
    DataList.append(Data)

####RUN
for baml in args.bams:
    bam = pysam.AlignmentFile(baml, "rb")
    DataList = []
    SN = [n["SN"] for n in bam.header['SQ']]
    if args.flag is True: #IF all headers should be written out seperatly
        for head in SN:
            bamh = bam.fetch(head)
            ED_List(bamh,head)
    if args.region: #IF Specific coordinates were supplied
        for i in args.region:
            bamh = bam.fetch(i.split(':')[0],int(i.split(':')[1].split('-')[0]),int(i.split('-')[1]))
            ED_List(bamh,i)
    else:
            ED_List(bam,head="ALL") # Standard Run with every read concatenated

if args.csv:
    with open (args.csv,'a') as out_csv:
        out_csv.write(','.join(Header)+'\n')
        for i in DataList:
            out_csv.write(','.join(i) + '\n')
        print('\n'+'====> Output File:   ' + str(args.csv)+'\n')

#Meriam Guellil 2021