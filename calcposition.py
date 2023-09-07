import random
import copy
from settings import extendbegin

uplayer_pos_right = [1,2,1,2]
uplayer_pos_left = [1,2,1,2]
downlayer_pos_right = [1,2,1,2]
downlayer_pos_left = [1,2,1,2]

length = random.randint(10,13)
el = ['','']
scramble = [copy.deepcopy(el) for x in range(length)]
sets=0

moves = ['1', '-1', '2', '-2', '3', '-3', '4', '-4', '5', '-5', '6', '-6']

def launchGenScramble():
    scramble[sets][0]=random.choice(moves)
    scramble[sets][1]=random.choice(moves)
    UpLayer.slashCheck()
    DownLayer.slashCheck()

def genScramble(set: int, layer: int):
    '''
    Input: to which set of moves(int) scramble should be generated
    Output: scramble with one more generated set of moves
    '''
    scramble[set][layer]=random.choice(moves)
    if layer==0:
        UpLayer.slashCheck()
    if layer==1:
        DownLayer.slashCheck()


class UpLayer():
    n_pieces_move_right_plus=0
    n_pieces_move_left_plus=0
    n_pieces_move_right_minus=0
    n_pieces_move_left_minus=0

    def slashCheck():
        global sets
        ## Uplayer; if plus scramble.
        if '-' not in scramble[sets][0]:
            print('uplayer minus not detected')
            int_move_plus=int(scramble[sets][0]) # generated move
            needed_plus=[] # counter of value of pieces in current position
            piece=0 # counter for list that contains values of pieces in current position
            while sum(needed_plus)<int_move_plus:
                needed_plus.append(copy.deepcopy(uplayer_pos_right[piece]))
                piece+=1
            if sum(needed_plus)==int_move_plus:
                print('success uplayer right plus!') # will do nothing here
            elif sum(needed_plus)>int_move_plus:
                print('has to regenerate. detected uplayer right plus')
                return genScramble(sets,0) # will regenerate  
            
            needed_plus=[]
            piece=0
            while sum(needed_plus)<int_move_plus:
                needed_plus.append(copy.deepcopy(uplayer_pos_left[piece]))
                piece+=1
            if sum(needed_plus)==int_move_plus:
                print('success uplayer left plus!')
                return UpLayer.turnCalcPlus() # will call next function
            elif sum(needed_plus)>int_move_plus:
                print('has to regenerate. detected uplayer left plus!')
                return genScramble(sets,0) # will regenerate
            

        ## Uplayer; if minus scramble.
        if '-' in scramble[sets][0]:
            print('uplayer minus detected')
            int_move_minus=abs(int(scramble[sets][0]))
            needed_minus=[]
            piece_l=-1
            while sum(needed_minus)<int_move_minus:
                needed_minus.append(copy.deepcopy(uplayer_pos_right[piece_l]))
                piece_l-=1
            if sum(needed_minus)==int_move_minus:
                print('success uplayer right minus!') 
            elif sum(needed_minus)>int_move_minus:
                print('has to regenerate. detected uplayer right minus.')
                return genScramble(sets,0)

            needed_minus=[]
            piece_l=-1
            while sum(needed_minus)<int_move_minus:
                needed_minus.append(copy.deepcopy(uplayer_pos_left[piece_l]))
                piece_l-=1
            if sum(needed_minus)==int_move_minus:
                print('success uplayer left minus!')
                return UpLayer.turnCalcMinus()
            elif sum(needed_minus)>int_move_minus:
                print('has to regenerate. uplayer detected left minus.')
                return genScramble(sets,0)

    def turnCalcPlus():
        global sets
        '''
        Input: set of moves from scramble
        Output: edits uplayer_pos_... lists
        '''
        print('calc plus uplayer started')
        # Uplayer; plus; right side
        end_piece=2
        summa=uplayer_pos_right[0]
        if uplayer_pos_right[0]==int(scramble[sets][0]):
            UpLayer.n_pieces_move_right_plus=1
            print('need to move only first uplayer right element')
        while summa!=int(scramble[sets][0]):
            lost=uplayer_pos_right[end_piece-1]
            if sum(uplayer_pos_right[0:end_piece])==int(scramble[sets][0]):
                UpLayer.n_pieces_move_right_plus=end_piece
                print('need to move first '+str(end_piece)+' elements from uplayer right') # end_piece is [0:end_piece] elements has to be moved
                break
            end_piece+=1
            summa+=lost
        
        # Uplayer; plus; left side
        end_piece=2
        summa=uplayer_pos_left[0]
        if uplayer_pos_left[0]==int(scramble[sets][0]):
            UpLayer.n_pieces_move_left_plus=1
            print('need to move only first uplayer left element')
        while summa!=int(scramble[sets][0]):
            lost=uplayer_pos_left[end_piece-1]
            if sum(uplayer_pos_left[0:end_piece])==int(scramble[sets][0]):
                UpLayer.n_pieces_move_left_plus=end_piece
                print('need to move first '+str(end_piece)+' elements from uplayer left')
                break
            end_piece+=1
            summa+=lost
        print('DONE for plus uplayer')
        UpLayer.posNewPlus()

    def turnCalcMinus():
        global sets
        print('calc uplayer minus started')
        # Uplayer; minus; right side.
        for_pr=2
        end_piece=len(uplayer_pos_right)-2
        summa=uplayer_pos_right[-1]
        if uplayer_pos_right[-1]==abs(int(scramble[sets][0])):
            UpLayer.n_pieces_move_right_minus=1
            print('need to move only last uplayer right element')
        while summa!=abs(int(scramble[sets][0])):
            lost=uplayer_pos_right[end_piece]
            if sum(uplayer_pos_right[end_piece:])==abs(int(scramble[sets][0])):
                UpLayer.n_pieces_move_right_minus=for_pr
                print('need to move last '+str(for_pr)+' elements from uplayer right')
                break
            for_pr+=1
            end_piece-=1
            summa+=lost
        
        # Uplayer; minus; left side
        end_piece=len(uplayer_pos_left)-2
        summa=uplayer_pos_left[-1]
        for_pr=2
        if summa==abs(int(scramble[sets][0])):
            UpLayer.n_pieces_move_left_minus=1
            print('need to move only last uplayer left element')
        while summa!=abs(int(scramble[sets][0])):
            lost=uplayer_pos_left[end_piece]
            if sum(uplayer_pos_left[end_piece:])==abs(int(scramble[sets][0])):
                UpLayer.n_pieces_move_left_minus=for_pr
                print('need to move last '+str(for_pr)+' elements from uplayer left')
                break
            for_pr+=1
            end_piece-=1
            summa+=lost
        print('DONE for minus uplayer')
        UpLayer.posNewMinus()

    def posNewPlus():
        global sets
        uplayer_pos_left.extend(uplayer_pos_right[0:UpLayer.n_pieces_move_right_plus])
        del uplayer_pos_right[0:UpLayer.n_pieces_move_right_plus]
        uplayer_pos_right.extend(uplayer_pos_left[0:UpLayer.n_pieces_move_left_plus])
        del uplayer_pos_left[0:UpLayer.n_pieces_move_left_plus]
        print(uplayer_pos_right)
        print(uplayer_pos_left)
        print(scramble)

    def posNewMinus():
        global sets
        global uplayer_pos_right
        global uplayer_pos_left
        ans=extendbegin(uplayer_pos_right, UpLayer.n_pieces_move_right_minus, uplayer_pos_left, UpLayer.n_pieces_move_left_minus)
        uplayer_pos_right=ans[0]
        uplayer_pos_left=ans[1]
        print(uplayer_pos_right)
        print(uplayer_pos_left)
        print(scramble)


class DownLayer():

    n_pieces_move_right_plus=0
    n_pieces_move_left_plus=0
    n_pieces_move_right_minus=0
    n_pieces_move_left_minus=0
    
    def slashCheck():
        global sets
        ## Downlayer; if plus scramble.
        if '-' not in scramble[sets][1]:
            print('minus not detected downlayer')
            int_move_plus=int(scramble[sets][1]) # generated move
            needed_plus=[] # counter of value of pieces in current position
            piece=0 # counter for list that contains values of pieces in current position
            while sum(needed_plus)<int_move_plus:
                needed_plus.append(copy.deepcopy(downlayer_pos_right[piece]))
                piece+=1
            if sum(needed_plus)==int_move_plus:
                print('success right plus downlayer!') # will do nothing here
            elif sum(needed_plus)>int_move_plus:
                print('has to regenerate. detected right plus downlayer')
                return genScramble(sets,1) # will regenerate  
            
            needed_plus=[]
            piece=0
            while sum(needed_plus)<int_move_plus:
                needed_plus.append(copy.deepcopy(downlayer_pos_left[piece]))
                piece+=1
            if sum(needed_plus)==int_move_plus:
                print('success downlayer left plus!')
                return DownLayer.turnCalcPlus() # will call next function
            elif sum(needed_plus)>int_move_plus:
                print('has to regenerate. detected downlayer left plus!')
                return genScramble(sets,1) # will regenerate
            

        ## Uplayer; if minus scramble.
        if '-' in scramble[sets][1]:
            print('downlayer minus detected')
            int_move_minus=abs(int(scramble[sets][1]))
            needed_minus=[]
            piece_l=-1
            while sum(needed_minus)<int_move_minus:
                needed_minus.append(copy.deepcopy(downlayer_pos_right[piece_l]))
                piece_l-=1
            if sum(needed_minus)==int_move_minus:
                print('success downlayer right minus!') 
            elif sum(needed_minus)>int_move_minus:
                print('has to regenerate. detected downlayer right minus.')
                return genScramble(sets,1)

            needed_minus=[]
            piece_l=-1
            while sum(needed_minus)<int_move_minus:
                needed_minus.append(copy.deepcopy(downlayer_pos_left[piece_l]))
                piece_l-=1
            if sum(needed_minus)==int_move_minus:
                print('success left downlayer minus!')
                return DownLayer.turnCalcMinus()
            elif sum(needed_minus)>int_move_minus:
                print('has to regenerate. detected downlayer left minus.')
                return genScramble(sets,1)
    
    def turnCalcPlus():
        global sets
        print('calc plus downlayer started')
        # Downlayer; plus; right side
        end_piece=2
        summa=downlayer_pos_right[0]
        if downlayer_pos_right[0]==int(scramble[sets][1]):
            DownLayer.n_pieces_move_right_plus=1
            print('need to move only first downlayer right element')
        while summa!=int(scramble[sets][1]):
            lost=downlayer_pos_right[end_piece-1]
            if sum(downlayer_pos_right[0:end_piece])==int(scramble[sets][1]):
                DownLayer.n_pieces_move_right_plus=end_piece
                print('need to move first '+str(end_piece)+' elements from downlayer right') # end_piece is [0:end_piece] elements has to be moved
                break
            end_piece+=1
            summa+=lost
        
        # Downlayer; plus; left side
        end_piece=2
        summa=downlayer_pos_left[0]
        if downlayer_pos_left[0]==int(scramble[sets][1]):
            DownLayer.n_pieces_move_left_plus=1
            print('need to move only first downlayer left element')
        while summa!=int(scramble[sets][1]):
            lost=downlayer_pos_left[end_piece-1]
            if sum(downlayer_pos_left[0:end_piece])==int(scramble[sets][1]):
                DownLayer.n_pieces_move_left_plus=end_piece
                print('need to move first '+str(end_piece)+' elements from downlayer left')
                break
            end_piece+=1
            summa+=lost
        print('DONE for plus downlayer')
        DownLayer.posNewPlus()

    def turnCalcMinus():
        global sets
        print('calc downlayer minus started')
        # Downlayer; minus; right side.
        for_pr=2
        end_piece=len(downlayer_pos_right)-2
        summa=downlayer_pos_right[-1]
        if downlayer_pos_right[-1]==abs(int(scramble[sets][1])):
            DownLayer.n_pieces_move_right_minus=1
            print('need to move only last downlayer right element')
        while summa!=abs(int(scramble[sets][1])):
            lost=downlayer_pos_right[end_piece]
            if sum(downlayer_pos_right[end_piece:])==abs(int(scramble[sets][1])):
                DownLayer.n_pieces_move_right_minus=for_pr
                print('need to move last '+str(for_pr)+' elements from downlayer right')
                break
            for_pr+=1
            end_piece-=1
            summa+=lost
        
        # Uplayer; minus; left side
        end_piece=len(downlayer_pos_left)-2
        summa=downlayer_pos_left[-1]
        for_pr=2
        if summa==abs(int(scramble[sets][1])):
            DownLayer.n_pieces_move_left_minus=1
            print('need to move only last downlayer left element')
        while summa!=abs(int(scramble[sets][1])):
            lost=downlayer_pos_left[end_piece]
            if sum(downlayer_pos_left[end_piece:])==abs(int(scramble[sets][1])):
                DownLayer.n_pieces_move_left_minus=for_pr
                print('need to move last '+str(for_pr)+' elements from downlayer left')
                break
            for_pr+=1
            end_piece-=1
            summa+=lost
        print('DONE for minus downlayer')
        DownLayer.posNewMinus()

    def posNewPlus():
        global sets
        downlayer_pos_left.extend(downlayer_pos_right[0:DownLayer.n_pieces_move_right_plus])
        del downlayer_pos_right[0:DownLayer.n_pieces_move_right_plus]
        downlayer_pos_right.extend(downlayer_pos_left[0:DownLayer.n_pieces_move_left_plus])
        del downlayer_pos_left[0:DownLayer.n_pieces_move_left_plus]
        print(downlayer_pos_right)
        print(downlayer_pos_left)
        # print(scramble)
        looperScramble()

    def posNewMinus():
        global sets
        global downlayer_pos_right
        global downlayer_pos_left
        ans=extendbegin(downlayer_pos_right, DownLayer.n_pieces_move_right_minus, downlayer_pos_left, DownLayer.n_pieces_move_left_minus)
        downlayer_pos_right=ans[0]
        downlayer_pos_left=ans[1]
        print(downlayer_pos_right)
        print(downlayer_pos_left)
        # print(scramble)
        looperScramble()

def looperScramble():
    global sets
    global uplayer_pos_right
    global downlayer_pos_right
    sets+=1
    if sets==length:
        finalPrint()
        print('checkerend')
        print('THE END')
        quit()
    slash_buf=copy.deepcopy(list(reversed(downlayer_pos_right)))
    downlayer_pos_right=copy.deepcopy(list(reversed(uplayer_pos_right)))
    uplayer_pos_right=copy.deepcopy(slash_buf)


    scramble[sets][0]=random.choice(moves)
    scramble[sets][1]=random.choice(moves)
    UpLayer.slashCheck()
    DownLayer.slashCheck()

def finalPrint():
    finale=scramble
    print(finale)