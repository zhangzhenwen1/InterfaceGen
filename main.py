import numpy as np
import subprocess
#subprocess.call("pause",shell=True)
from abaqusparser import AbaqusParser
###################################
###     ARRAY INITIALIAZITON    ###
###################################
# --- DEFINE THE JOB NAME TO PARSER ---
inpfile = AbaqusParser('Job-1') 

# --- IMPORT ELEMENT DATA ---
# --- data structure is: element No. + node No. ---
array_INCLUSION=inpfile.ReadElsetElems('IN')
array_SUBSTRATE=inpfile.ReadElsetElems('SUB')
#array_elements=inpfile.ReadBulkElems() # import all the elements

# --- IMPORT NODE DATA ---
# --- data structure is: node No. + coordinate ---
array_node=inpfile.ReadNodes() # import the nodes

# --- DEINE THE FACE & ELEMENT ARRAY TO MATCH ---
array_faces=inpfile.DefineFaces(array_INCLUSION)
array_elements=array_SUBSTRATE
array_face_elements=array_INCLUSION

# --- INITIALIZE COHESIVE DATA ---
# data structur: 
# cohesive element No. + the element No. of the face contacted + node No.
array_cohesive=np.zeros((1,14),dtype=int) 
#------- initiate parameters -----------
node_sum=len(array_node) # get the total number of nodes
add_num=pow(10,int(np.log10(node_sum))+2) # caculate the initial chesive element No.
cohesive_num=add_num
####################################
########### MAIN PROCEDURE #########
####################################
# loop starts by face, to find the element which has the same face by matching the nodes.
# chang the nodes on face by adding $add_sum, and define the cohesive element.

for n in range(array_faces.shape[0]): # loop starts with faces

    #print('INFO: DEAL with faces in element No.',array_faces[n][0])
    #print('INFO: nodes in face No. ', n, ' are ', array_faces[n])
    
    # caculate the addon to node/element numbers changed
    #add_num=pow(10,int(np.log10(node_sum))+2)*array_faces[n][0] 

    for i in range(array_elements.shape[0]):
        if ( array_faces[n][0] != array_elements[i][0] ): # make sure the matching procedure in different elements
                                                          # and make sure one way matching
             # get the array index which the face belong
            if ((np.where(array_face_elements[...,0]==array_faces[n][0])[0].shape)[0]!=0):
                face_pos=np.where(array_face_elements[...,0]==array_faces[n][0])[0][0]
                #print(' this face is in the element No. ', face_pos+1, ', finding the match between face and element...')
        #------------- NODE MATCHING PROCEDURE ----------------
        # matching the node position in the element loop i and face loop n
            # matching face node 1
            node_match= np.where(array_elements[i][...,1:]==array_faces[n][1])[0]
            # matching face node 2
            p=np.where(array_elements[i][...,1:]==array_faces[n][2])[0]
            node_match=np.append(node_match,p)
            # matching face node 3
            p=np.where(array_elements[i][...,1:]==array_faces[n][3])[0]
            node_match=np.append(node_match,p)
            # get the true position from the index
            node_match=node_match+1

        #-------------- COHESIVE ELEMENT INCERT PROCEDURE ----------------------
            if (node_match.size == 3):
                #print('find the matched nodes coordinates in element are ', node_match)
                #print('## element node changing procedure starts ( 3 nodes same )')
                #print('    face   :', array_faces[n])
                #print('    element:', array_elements[i])

            #------------- define cohesive element ----------------
            # data structur: 
            # cohesive element No. + the element No. of the face contacted + node No.
                cohesive_num=cohesive_num+1
                cohesive=[]
                cohesive.append(cohesive_num) # cohesive element No.
                cohesive.append(array_face_elements[face_pos][0]) # the element No. of the face contacted
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
                #print('  array cohesive defined now is \n', array_cohesive)
                #print('----')
            #--------- element node chang & new node add ---------
                # find node index in the face element
                node_match= np.where(array_face_elements[face_pos][...,1:]==array_faces[n][1])[0]
                p=np.where(array_face_elements[face_pos][...,1:]==array_faces[n][2])[0]
                node_match=np.append(node_match,p)
                p=np.where(array_face_elements[face_pos][...,1:]==array_faces[n][3])[0]
                node_match=np.append(node_match,p)
                p=np.where(array_face_elements[face_pos][...,1:]==array_faces[n][4])[0]
                node_match=np.append(node_match,p)
                p=np.where(array_face_elements[face_pos][...,1:]==array_faces[n][5])[0]
                node_match=np.append(node_match,p)
                p=np.where(array_face_elements[face_pos][...,1:]==array_faces[n][6])[0]
                node_match=np.append(node_match,p)
                node_match=node_match+1
                print(node_match)
                for p in node_match:
                # changing the node No. in $array_node
                    # find the face node index in $array_node
                    node_index=np.where(array_node[...,0]==array_face_elements[face_pos][p])[0]
                    # changing the node No. in elements
                    array_face_elements[face_pos][p]=array_node[...,0][node_index]+add_num 
                    #print('  the element with the face is changed to', array_elements[face_pos])
                  # changing the corresponding node in $array_cohesive
                    # find the index in array_cohesive matching face element
                    #cohesive_index =np.where(array_cohesive[...,1]==array_face_elements[face_pos][0])[0]
                    #if cohesive_index.size>0:
                    #    for index in cohesive_index:
                            # find the node index needing to change of array_cohesive matching the specific node
                    #        change_index=np.where(array_cohesive[index][...,2:]==array_node[...,0][node_index][0])[0]
                    #        if change_index.size>0:
                                #print('  and having corresponding node to change in cohesive elements')
                                #print('    the original cohesive element No.',q,' is ', array_cohesive[q])
                                #print('    the node to change is ',array_node[...,0][node_pos][0])
                    #            change_index[0]=change_index[0]+2
                    #            array_cohesive[index][change_index[0]]=array_face_elements[face_pos][p]
                                #print('    the cohesive element is changed to ',array_cohesive[q])
                                #subprocess.call("pause",shell=True) 
                    # add the new cohesive node into node array
                    array_node_add=np.array([array_face_elements[face_pos][p],array_node[node_index[0]][1],array_node[node_index[0]][2],array_node[node_index[0]][3]])
                    #print('       node to add in ', array_node_add)
                    # find if duplicate node existes
                    node_duplicate=array_node[...,0][np.where(array_node[...,0]==array_node_add[0])]
                    if node_duplicate.size==0: # no duplicate
                        array_node=np.append(array_node,[array_node_add], axis=0)
                        #print('       and new node added')
                # changing the node No. in elements
                #print('----')
        else:
            if ( array_faces[n][0] == array_elements[i][0] ):
                #print('  the face is in the element matching now, the procedure skip..')
                continue
            else:
                #print('   the direction is backward, the procedure skips..')
                continue
                
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
