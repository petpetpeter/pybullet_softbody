# %%
def openFile(filename):
    fileList = []
    f = open(filename)
    for line in f:
        block = line.split()
        fileList.append(block)
    f.close()
    return fileList

def getInfoIndex(resultList):
    cellIndex = 0
    meshIndex = 0
    for i,line in enumerate(resultList):
        if "CELLS" in line:
            cellIndex = i
        if "CELL_TYPES" in line:
            meshIndex = i
    return cellIndex,meshIndex
           
def removeLine(fileList):
    removeCellList = []
    twoDCellList = []
    resultCellList = []
    twoDMeshList = []
    ####remove2Dcell########
    for line in fileList:
        if len(line) > 0:
            if len(line) != 4 or line[0] != '3':
                removeCellList.append(line)
            else:
                twoDCellList.append(line)
        else:
            removeCellList.append(line)
    ###remove2Dmesh########
    for line in removeCellList:
        if len(line) > 0:
            if len(line) != 1 or line[0] != '5':
                resultCellList.append(line)
            else:
                twoDMeshList.append(line)
        else:
            resultCellList.append(line)

    return resultCellList,len(twoDCellList),len(twoDMeshList)

def changeNumber(resultList,n2dc,n2dm,ci,mi):
    resultList[ci][1] = str(int(resultList[ci][1])-n2dc)
    resultList[ci][2] = str(int(resultList[ci][2])-n2dc*4)
    resultList[mi][1] = str(int(resultList[mi][1])-n2dm)
    return resultList

def writeFile(writeFileList,outFile):
    with open(outFile, "w",encoding="utf-8") as fo:
        fo.write('\n'.join([' '.join(i) for i in writeFileList]))

import sys
inFile = sys.argv[1]
outFile = sys.argv[2]
fileList = openFile(inFile)
resultList,numOf2DCell,numOf2DMesh = removeLine(fileList)
cellIndex,meshIndex = getInfoIndex(resultList)
writeFileList = changeNumber(resultList,numOf2DCell,numOf2DMesh,cellIndex,meshIndex)
writeFile(writeFileList,outFile)
print('finishTheJOB')

#triggerDict["startList"] = t0_list

# %%
