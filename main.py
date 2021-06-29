from contextlib import nullcontext
from pickle import PicklingError
import numpy as np
import subprocess
#subprocess.call("pause",shell=True)
from numpy import genfromtxt
from numpy.core.fromnumeric import shape
from abaqusparser import AbaqusParser
from mesh import Mesh
from interfnode import Interfnode
from newmesh import NewMesh
#------- input file define -----------
inpfile = AbaqusParser('Job-1') # define the input file name
inpfile.ReadElsets() # ???
#------- array define -----------
array_node=inpfile.ReadNodes() # import the nodes
array_node=np.array(array_node,dtype=float)
array_elements=inpfile.ReadBulkElems() # import the elements
array_elements=np.array(array_elements,dtype=int)
array_cohesive=np.zeros((1,7),dtype=int) # define array store cohesive element
#------- initiate the face array  -----------
array_faces=[]
for i in range(array_elements.shape[0]):
    face=[]
    face.append(array_elements[i][0])
    face.append(array_elements[i][1])
    face.append(array_elements[i][2])
    face.append(array_elements[i][3])
    array_faces.append(face)
    face=[]
    face.append(array_elements[i][0])
    face.append(array_elements[i][4])
    face.append(array_elements[i][3])
    face.append(array_elements[i][2])
    array_faces.append(face)
    face=[]
    face.append(array_elements[i][0])
    face.append(array_elements[i][3])
    face.append(array_elements[i][4])
    face.append(array_elements[i][1])
    array_faces.append(face)
    face=[]
    face.append(array_elements[i][0])
    face.append(array_elements[i][1])
    face.append(array_elements[i][4])
    face.append(array_elements[i][2])
    array_faces.append(face)
array_faces=np.array(array_faces,dtype=int)
#------- initiate parameters -----------
node_sum=len(array_node) # get the total number of nodes
add_num=pow(10,int(np.log10(node_sum))+2) # caculate the addon to node/element numbers changed
cohesive_num=add_num # caculate the chesive element No.
#array_elements_new=array_elements
#print(node_sum)
#print(array_elements)
#print(add_num)
####################################
########### MAIN PROCEDURE #########
####################################
# loop starts by face, to find the element which has the same face by matching the nodes.
# chang the nodes on face by adding $add_sum, and define the cohesive element.
for n in range(array_faces.shape[0]): # loop starts with faces
    print('#####################################')
    print('## DEAL with faces in element No.',array_faces[n][0])
    print('#####################################')
    print('-- nodes in face No. ', n, ' are \n', array_faces[n])
#------------- element matching procedure ----------------
    for i in range(array_elements.shape[0]):
        #print('-- element matching now is No.', array_elements[i][0], ' are ')
        #print(array_elements[i])
        if ( array_faces[n][0] < array_elements[i][0] ): # make sure the matching procedure in different elements
         # and make sure one way matching
            face_pos=np.where(array_elements[...,0]==array_faces[n][0])[0][0] # get the element No. which the face belong
            print('-- face in element No. ', face_pos)
        #----- find the coordinates of matching nodes in $array_element -----
            node_match= np.where(array_elements[i][...,1:]==array_faces[n][1])[0]
            p=np.where(array_elements[i][...,1:]==array_faces[n][2])[0]
            node_match=np.append(node_match,p)
            p=np.where(array_elements[i][...,1:]==array_faces[n][3])[0]
            node_match=np.append(node_match,p)
            node_match=node_match+1
            #print('node match is', node_match)
        #-------------- element node changing procedure ----------------------
            if (node_match.size == 3):
                print('-- 3 nodes same --')
                print('face is ', array_faces[n])
                print('element is ', array_elements[i])
                cohesive_num=cohesive_num+1
                cohesive=[]
                cohesive.append(cohesive_num)
                cohesive.append(array_faces[n][1]+add_num)
                cohesive.append(array_faces[n][2]+add_num)
                cohesive.append(array_faces[n][3]+add_num)
                cohesive.append(array_faces[n][1])
                cohesive.append(array_faces[n][2])
                cohesive.append(array_faces[n][3])
                cohesive=np.array(cohesive,dtype=int)
                array_cohesive=np.append(array_cohesive,[cohesive],axis=0)
                print('array cohesive is ', array_cohesive,array_cohesive[...,1].size)
                print('--- changing procedure start ---')
                node_match= np.where(array_elements[face_pos][...,1:]==array_faces[n][1])[0]
                p=np.where(array_elements[face_pos][...,1:]==array_faces[n][2])[0]
                node_match=np.append(node_match,p)
                p=np.where(array_elements[face_pos][...,1:]==array_faces[n][3])[0]
                node_match=np.append(node_match,p)
                node_match=node_match+1
                for p in node_match:
                    print('--- element node array is ',array_elements[face_pos])
                    print('--- face node array is ',array_faces[n])
                    node_pos=np.where(array_node[...,0]==array_elements[face_pos][p])[0]
                    print('node_pos in node array is ', node_pos)
                    array_elements[face_pos][p]=array_elements[face_pos][p]+add_num
                    array_node_add=np.array([array_elements[face_pos][p],array_node[node_pos[0]][1],array_node[node_pos[0]][2],array_node[node_pos[0]][3]])
                    print('node to add in ', array_node_add)
                    node_ex=array_node[...,0][np.where(array_node[...,0]==array_elements[face_pos][p])]
                    if node_ex.size==0:            
                        array_node=np.append(array_node,[array_node_add], axis=0)
                        print('new node added')
                print('element node now is ', array_elements[face_pos])
                print('-- change element node done --')
                
                if array_faces[n][0] > 1:
                    add_num=add_num+pow(10,int(np.log10(node_sum))+2)
                    node_match_row= np.where(array_cohesive[...,1:]==array_faces[n][1])[0][0]
                    node_match_col= np.where(array_cohesive[...,1:]==array_faces[n][1])[1][0]+1
                    print('node 1 ',array_faces[n][1],' in array_cohesive, the node pos is column ', node_match_col)
                    print('node 1 ',array_faces[n][1],' in array_cohesive, the node pos is row ', node_match_row)
                    print('before change',array_cohesive)
                    array_cohesive[node_match_row][node_match_col]=array_faces[n][1]+add_num
                    print('after',array_cohesive)
                    subprocess.call("pause",shell=True)
            '''p=np.where(array_elements[face_pos][...,1:]==array_faces[n][2])[0]
            node_match=np.append(node_match,p)
            p=np.where(array_elements[face_pos][...,1:]==array_faces[n][3])[0]
            node_match=np.append(node_match,p)
            node_match=node_match+1
            for p in node_match:
                print('--- element node array is ',array_elements[face_pos])
                print('--- face node array is ',array_faces[n])
                node_pos=np.where(array_node[...,0]==array_elements[face_pos][p])[0]
                print('node_pos in node array is ', node_pos)
                array_elements[face_pos][p]=array_elements[face_pos][p]+add_num
                array_node_add=np.array([array_elements[face_pos][p],array_node[node_pos[0]][1],array_node[node_pos[0]][2],array_node[node_pos[0]][3]])
                print('node to add in ', array_node_add)
                node_ex=array_node[...,0][np.where(array_node[...,0]==array_elements[face_pos][p])]
                if node_ex.size==0:            
                    array_node=np.append(array_node,[array_node_add], axis=0)
                    print('new node added')
            print('element node now is ', array_elements[face_pos])
            subprocess.call("pause",shell=True)
'''
"""
                for j in range(1,11):
                    if ( array_faces[n][1] == array_elements[i][j] ):
                        print('-- face node is ', array_faces[n])
                        print('change node number 1', array_elements[i])
                        array_elements[i][j]=array_faces[n][1]+add_num
                        print('to ', array_elements[i])
                        array_faces[n][1]=0
                        node_ex=array_node[...,0][np.where(array_node[...,0]==array_elements[i][j])]
                        #print(array_faces[n][1])
                        #cohesive.append(array_elements[i][j])
                        #print(cohesive)
                        #subprocess.call("pause",shell=True)
                        if node_ex.size==0:
                            for k in range(len(array_node)):
                                if array_faces[n][1]==array_node[k][0]:
                                    array_node_add=np.array([array_node[k][0]+add_num,array_node[k][1],array_node[k][2],array_node[k][3]])
                                    array_node=np.append(array_node,[array_node_add], axis=0)
                    if ( array_faces[n][2] == array_elements[i][j] ):
                        print('change node number 2', array_elements[i])
                        array_elements[i][j]=array_faces[n][2]+add_num
                        print('to ', array_elements[i])
                        array_faces[n][2]=0
                        node_ex=array_node[...,0][np.where(array_node[...,0]==array_elements[i][j])]
                        #print(array_faces[n][2])
                        #cohesive.append(array_elements[i][j])
                        #print(cohesive)
                        #subprocess.call("pause",shell=True)
                        if node_ex.size==0:
                            for k in range(len(array_node)):
                                if array_faces[n][2]==array_node[k][0]:
                                    array_node_add=np.array([array_node[k][0]+add_num,array_node[k][1],array_node[k][2],array_node[k][3]])
                                    array_node=np.append(array_node,[array_node_add], axis=0)
                    if ( array_faces[n][3] == array_elements[i][j] ):
                        print('change node number 3', array_elements[i])
                        array_elements[i][j]=array_faces[n][3]+add_num
                        print('to ', array_elements[i])
                        array_faces[n][3]=0
                        print('-- face node is now', array_faces[n])
                        node_ex=array_node[...,0][np.where(array_node[...,0]==array_elements[i][j])]
                        #print(array_faces[n][3])                        
                        #cohesive.append(array_elements[i][j])                        
                        #print(cohesive)                        
                        subprocess.call("pause",shell=True)
                        if node_ex.size==0:
                            for k in range(len(array_node)):
                                if array_faces[n][3]==array_node[k][0]:
                                    array_node_add=np.array([array_node[k][0]+add_num,array_node[k][1],array_node[k][2],array_node[k][3]])
                                    array_node=np.append(array_node,[array_node_add], axis=0)
"""
#array_cohesive=np.array(list_cohesive)
#print(array_cohesive)
#print(array_elements)
#array_elements=np.append(array_elements,array_cohesive, axis=0)
fout = open('array_elements.inp','w')
for i in range(array_elements.shape[0]):
    fout.write(str(array_elements[i])+"\n")
fout.close()
fout = open('face.inp','w')
for i in range(array_faces.shape[0]):
    fout.write(str(array_faces[i])+"\n")
fout.close()
fout = open('array_cohesive.inp','w')
for i in range(array_cohesive.shape[0]):
    fout.write(str(array_cohesive[i])+"\n")
fout.close()
fout = open('array-new-nodes.inp','w')
for line in array_node:
    str_line=str(int(line[0]))+',  '+str(line[1])+',  '+str(line[2])+',  '+str(line[3])+'\n'
    fout.write(str_line)
fout.close()
