
def createTriangle():
    f=open('triangle.txt')
    print 'Reading File...\n'
    time.sleep(0.5)
    triLst=f.readlines()
    i=0
    for line in triLst:
        triLst[i]=line.rstrip('\n').split()
        i+=1
    return triLst

def findMaxOfLine(i,triLst):
    if i==0: return triLst[0][0]
    else:
        j=triLst[i-1].index(findMaxOfLine(i-1,triLst))
        return str(max(int(triLst[i][j]),int(triLst[i][j+1])))
    

def main():
    triLst=createTriangle()
    print 'Database Established!\n'
    time.sleep(1)
    resultLst=[]
    i=0
    while i<len(triLst):
        resultLst.append(int(findMaxOfLine(i,triLst)))
        print 'Max of Line '+str(i+1)+' is '+str(resultLst[-1])
        i+=1
    print '\nThe result is '+str(sum(resultLst))
    raw_input()

if __name__=='__main__':
    main()
