# Nicolo Grilli
# University of Oxford
# AWE project 2020
# 23 Giugno 2020
import numpy as np
# class representing abaqus input file
# and functions for parsing

class AbaqusParser:

	# prefissofile is the prefix of abaqus .inp file
	def __init__(self,prefissofile):
		self.prefissofile = prefissofile
		self.filename = prefissofile + '.inp'

	# read element sets from file
	# only generate keyword is accepted
	def ReadElsets(self,SetName):
		fid = open(self.filename,'r')
		elsetsfilename = self.prefissofile + '-'+SetName+'.inp'
		fout = open(elsetsfilename,'w')
		ls=[]
		flagprintnextline = False # next line should be printed or not
		for line in fid:
			if (flagprintnextline):
				line=line.strip('\n')
				ls.append(line.split(','))
				flagprintnextline = False
			if (line[0:6] == '*Elset'): # this is an elset
				posgrain = line.find(SetName) # -1 if this is not a grain
				posgenerate = line.find('generate') # generate is only format accepted
				if (posgrain >= 0): # this is a grain
					if (posgenerate >= 0):
						flagprintnextline = True # print next line containing the elements start/end
					else:
						print('generate keyword is not present' + '\n')
						print('generate keyword is the only accepted format' + '\n')
						exit()
		fid.close()
		fout.close()
		ls=np.array(ls,dtype=int)
		fout = open(elsetsfilename,'w')
		for i in range(ls.shape[0]):
			fout.write(str(ls[i])+"\n")
		fout.close()  #关闭文件
		return ls

	# read nodes from file
	def ReadNodes(self):
		ls=[]
		fid = open(self.filename,'r')
		nodesfilename = self.prefissofile + '-node.inp'
		fout = open(nodesfilename,'w')
		flagfoundnodes = False # block with nodes has been found
		for line in fid:
			if (flagfoundnodes): # this line may contain nodes
				if (line[0] == '*'): # reached the end of nodes
					flagfoundnodes = False
					#line=str(node_num)
					#fout.write(line)
					break # needed because you may find also *Node Output
				else:
					fout.write(line)
					line=line.strip('\n')
					ls.append(line.split(','))
			if (line[0:5] == '*Node'): # these are the nodes
				flagfoundnodes = True
		fid.close()
		fout.close()
		ls=np.array(ls,dtype=float)
		return ls

	# read bulk elements from file
	def ReadBulkElems(self):
		ls=[]
		fid = open(self.filename,'r')
		elemsfilename = self.prefissofile + '-bulk-elems.inp'
		fout = open(elemsfilename,'w')
		flagfoundelems = False # block with elements has been found
		for line in fid:
			if (flagfoundelems): # this line may contain elements
				if (line[0] == '*'): # reached the end of elements
					flagfoundelems = False
					break # needed because you may find also *Element Output
				else:
					fout.write(line)
					line=line.strip('\n')
					ls.append(line.split(','))
			if (line[0:8] == '*Element'): # these are the elements
				flagfoundelems = True
		fid.close()
		fout.close()
		ls=np.array(ls,dtype=int)
		elemsfilename = self.prefissofile + '-elems.inp'
		fout = open(elemsfilename,'w')
		for i in range(ls.shape[0]):
			fout.write(str(ls[i])+"\n")
		fout.close()  #关闭文件
		return ls

	def ReadElsetElems(self,SetName):
		ls_elsets=self.ReadElsets(SetName)
		ls_elem=self.ReadBulkElems()
		ls=[]
		for n in range(ls_elsets.shape[0]):
			for i in range(ls_elsets[n][0],ls_elsets[n][1]+ls_elsets[n][2],ls_elsets[n][2]):
				for j in range(ls_elem.shape[0]):
					if i==ls_elem[j][0]:
						ls.append(ls_elem[j])
		ls=np.array(ls,dtype=int)
		elemsfilename = self.prefissofile +'-'+ SetName +'-elems.inp'
		fout = open(elemsfilename,'w')
		for i in range(ls.shape[0]):
			fout.write(str(ls[i])+"\n")
		fout.close()  #关闭文件
		return ls
	
	def DefineFaces(self,array_elements):
		array_faces=[]
		for i in range(array_elements.shape[0]):# loop in all elements to define the faces
			face=[]
			face.append(array_elements[i][0])
			face.append(array_elements[i][1])
			face.append(array_elements[i][2])
			face.append(array_elements[i][3])
			face.append(array_elements[i][5])
			face.append(array_elements[i][6])
			face.append(array_elements[i][7])
			array_faces.append(face)
			face=[]
			face.append(array_elements[i][0])
			face.append(array_elements[i][4])
			face.append(array_elements[i][3])
			face.append(array_elements[i][2])
			face.append(array_elements[i][10])
			face.append(array_elements[i][6])
			face.append(array_elements[i][9])
			array_faces.append(face)
			face=[]
			face.append(array_elements[i][0])
			face.append(array_elements[i][3])
			face.append(array_elements[i][4])
			face.append(array_elements[i][1])
			face.append(array_elements[i][10])
			face.append(array_elements[i][8])
			face.append(array_elements[i][7])
			array_faces.append(face)
			face=[]
			face.append(array_elements[i][0])
			face.append(array_elements[i][1])
			face.append(array_elements[i][4])
			face.append(array_elements[i][2])
			face.append(array_elements[i][8])
			face.append(array_elements[i][9])
			face.append(array_elements[i][5])
			array_faces.append(face)
		array_faces=np.array(array_faces,dtype=int)
		filename='array_faces.inp'
		fout=open(filename,'w')
		for i in range(array_faces.shape[0]):
			fout.write(str(array_faces[i])+"\n")
		fout.close() #关闭文件
		return array_faces




