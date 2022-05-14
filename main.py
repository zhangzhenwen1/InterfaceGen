import numpy as np
import subprocess
#subprocess.call("pause",shell=True)
from abaqusparser import AbaqusParser
#------- array define -----------
inpfile = AbaqusParser('Job-1') # define the input file name
array_INCLUSION=inpfile.ReadElsetElems('IN') # 
array_SUBSTRATE=inpfile.ReadElsetElems('SUB') # 
array_node=inpfile.ReadNodes() # import the nodes
#array_elements=inpfile.ReadBulkElems() # import the elements
array_elements=array_SUBSTRATE
array_cohesive=np.zeros((1,14),dtype=int) # define array store cohesive element, 
# it is structured by the cohesive element No. + the element No. of the face contacted + the nodes.
array_faces=inpfile.DefineFaces(array_INCLUSION) # define the face array
#------- initiate parameters -----------
node_sum=len(array_node) # get the total number of nodes
cohesive_num=pow(10,int(np.log10(node_sum))+2) # caculate the chesive element No.
####################################
########### MAIN PROCEDURE #########
####################################
# loop starts by face, to find the element which has the same face by matching the nodes.
# chang the nodes on face by adding $add_sum, and define the cohesive element.
for n in range(array_faces.shape[0]): # loop starts with faces
    print('########################################')
    print('## DEAL with faces in element No.',array_faces[n][0],' ##')
    print('########################################')
    print(' nodes in face No. ', n, ' are ', array_faces[n])
    add_num=pow(10,int(np.log10(node_sum))+2)*array_faces[n][0] # caculate the addon to node/element numbers changed
#------------- element matching procedure ----------------
    for i in range(array_elements.shape[0]):
        print('-- START ELEMENT MATCHING PROCEDURE --')
        if ( array_faces[n][0] < array_elements[i][0] ): # make sure the matching procedure in different elements
         # and make sure one way matching
            if ((np.where(array_elements[...,0]==array_faces[n][0])[0].shape)[0]==0):
                continue
            face_pos=np.where(array_elements[...,0]==array_faces[n][0])[0][0] # get the element No. which the face belong
            print(' this face is in the element No. ', face_pos+1, ', finding the match between face and element...')
        #----- find the coordinates of matching nodes in $array_element -----
            node_match= np.where(array_elements[i][...,1:]==array_faces[n][1])[0]
            p=np.where(array_elements[i][...,1:]==array_faces[n][2])[0]
            node_match=np.append(node_match,p)
            p=np.where(array_elements[i][...,1:]==array_faces[n][3])[0]
            node_match=np.append(node_match,p)
            node_match=node_match+1
        #-------------- cohesive element insert procedure ----------------------
            if (node_match.size == 3):
                print('find the matched nodes coordinates in element are ', node_match)
                print('## element node changing procedure starts ( 3 nodes same )')
                print('    face   :', array_faces[n])
                print('    element:', array_elements[i])
            #------------- define cohesive element ----------------
                cohesive_num=cohesive_num+1
                cohesive=[]
                cohesive.append(cohesive_num)
                cohesive.append(array_elements[i][0])
                cohesive.append(array_faces[n][1]+add_num)
                cohesive.append(array_faces[n][2]+add_num)
                cohesive.append(array_faces[n][3]+add_num)
                cohesive.append(array_faces[n][4]+add_num)
                cohesive.append(array_faces[n][5]+add_num)
                cohesive.append(array_faces[n][6]+add_num)
                cohesive.append(array_faces[n][1])
                cohesive.append(array_faces[n][2])
                cohesive.append(array_faces[n][3])
                cohesive.append(array_faces[n][4])
                cohesive.append(array_faces[n][5])
                cohesive.append(array_faces[n][6])
                cohesive=np.array(cohesive,dtype=int)
                array_cohesive=np.append(array_cohesive,[cohesive],axis=0)
                print('  array cohesive defined now is \n', array_cohesive)
                print('----')
            #--------- element node changing & new node adding procedure start ---------
                print('  the face belong to the element:',array_elements[face_pos])
                node_match= np.where(array_elements[face_pos][...,1:]==array_faces[n][1])[0]
                p=np.where(array_elements[face_pos][...,1:]==array_faces[n][2])[0]
                node_match=np.append(node_match,p)
                p=np.where(array_elements[face_pos][...,1:]==array_faces[n][3])[0]
                node_match=np.append(node_match,p)
                p=np.where(array_elements[face_pos][...,1:]==array_faces[n][4])[0]
                node_match=np.append(node_match,p)
                p=np.where(array_elements[face_pos][...,1:]==array_faces[n][5])[0]
                node_match=np.append(node_match,p)
                p=np.where(array_elements[face_pos][...,1:]==array_faces[n][6])[0]
                node_match=np.append(node_match,p)
                node_match=node_match+1
                for p in node_match:
                # changing the node No. in $array_node
                    node_pos=np.where(array_node[...,0]==array_elements[face_pos][p])[0]# find the face node coordintaes in $array_node
                    array_elements[face_pos][p]=array_node[...,0][node_pos]+add_num # changing the node No. in elements
                    print('  the element with the face is changed to', array_elements[face_pos])
                  # changing the corresponding node in $array_cohesive
                    cohesive_node_to_change=np.where(array_cohesive[...,1]==array_elements[face_pos][0])[0]
                    if cohesive_node_to_change.size>0:
                        for q in cohesive_node_to_change:
                            change_pos=np.where(array_cohesive[q][...,2:]==array_node[...,0][node_pos][0])[0]
                            if change_pos.size>0:
                                print('  and having corresponding node to change in cohesive elements')
                                print('    the original cohesive element No.',q,' is ', array_cohesive[q])
                                print('    the node to change is ',array_node[...,0][node_pos][0])
                                change_pos[0]=change_pos[0]+2
                                array_cohesive[q][change_pos[0]]=array_elements[face_pos][p]
                                print('    the cohesive element is changed to ',array_cohesive[q])
                                #subprocess.call("pause",shell=True) 
                    array_node_add=np.array([array_elements[face_pos][p],array_node[node_pos[0]][1],array_node[node_pos[0]][2],array_node[node_pos[0]][3]])
                    print('       node to add in ', array_node_add)
                    node_duplicate=array_node[...,0][np.where(array_node[...,0]==array_node_add[0])]# find if duplicate node existes
                    if node_duplicate.size==0: # no duplicate
                        array_node=np.append(array_node,[array_node_add], axis=0)
                        print('       and new node added')
                # changing the node No. in elements
                print('----')
        else:
            if ( array_faces[n][0] == array_elements[i][0] ):
                print('  the face is in the element matching now, the procedure skip..')
            else:
                print('   the direction is backward, the procedure skips..')
                
                '''
                if array_faces[n][0] > 1:
                    print('the element changed is ',array_elements[face_pos])
                    node_match_row_1= np.where(array_cohesive[...,2:]==array_faces[n][1])[0][0]
                    node_match_col_1= np.where(array_cohesive[...,2:]==array_faces[n][1])[1][0]+1
                    print('node 1 ',array_faces[n][1],' in array_cohesive, the node pos is column ', node_match_col_1)
                    print('           in array_cohesive, the node pos is row ', node_match_row_1)
                    if array_cohesive[node_match_row_1][1]!=array_faces[n][0]:
                        print('before change',array_cohesive)
                        array_cohesive[node_match_row_1][node_match_col_1]=array_faces[n][1]+add_num
                        print('after',array_cohesive)
                    subprocess.call("pause",shell=True)
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

fout = open('array_cohesive.inp','w')
for line in array_cohesive:
    if line[0]==0:
        continue
    str_line=str(int(line[0]))
    for i in range(2,14):
        str_line=str_line+',  '+str(line[i])
    str_line=str_line+'\n'
    fout.write(str_line)
fout.close()

fout = open('array-new-nodes.inp','w')
for line in array_node:
    str_line=str(int(line[0]))+',  '+str(line[1])+',  '+str(line[2])+',  '+str(line[3])+'\n'
    fout.write(str_line)
fout.close()
