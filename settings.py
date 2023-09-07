# layer_right=[1,2,3,4]
# layer_left=[5,6,7,8]
# a=3

def extendbegin(pos_rightlayer: list, num_pieces_fromright: int, pos_leftlayer: list, num_pieces_fromleft: int) -> list:
    buf_r=pos_rightlayer[-num_pieces_fromright:] # end taken
    del pos_rightlayer[-num_pieces_fromright:]
    buf_l=pos_leftlayer[-num_pieces_fromleft:] # end taken
    del pos_leftlayer[-num_pieces_fromleft:]
    buf_r.extend(pos_leftlayer)
    buf_l.extend(pos_rightlayer)
    pos_rightlayer=buf_l
    pos_leftlayer=buf_r
    return pos_rightlayer, pos_leftlayer

# ans=extendbegin(layer_right, a, layer_left, 2)
# print(ans)
# layer_right=ans[0]
# layer_left=ans[1]
# print(layer_right)
# print(layer_left)

# def layerSlashCheckBad(la):
#     '''
#     Input: (2d list)
#     Output: 'True' if layer can be turned
#             'False' if layer cannot be turned
#             'Wrong sequence of pieces values was given!!!' if given an impossible layout
#     '''
#     turn_checker=0
#     x=0
#     while x<len(la) or turn_checker>6:
#         try:
#             int_el=la[x][0]
#             turn_checker+=int_el
#             print('loop done on x: ' + str(x) + '; turn_checker: ' + str(turn_checker) + '.')
#             x+=1
#         except IndexError:
#             break
#     if turn_checker==6:
#         return True
#     elif turn_checker==7 or turn_checker==5:
#         return False
#     else:
#         return 'Wrong sequence of pieces values was given!!!'