array = [ 10, 12, 9, 8, 10, 15, 1, 3, 2 ]
n = len( array )
k = 3
max_sum = -math.inf

def re_arrange ( array1, array2 ) :
    ans = []
    index1 = 0
    index2 = 0
    while ( index1 < len( array1 ) and index2 < len( array2 ) ) :
        if array1 [ index1 ] > array2 [ index2 ] :
            ans.append ( array1 [ index1 ] )
            index1 += 1
        elif array1 [ index1 ] < array2 [ index2 ] :
            ans.append ( array2 [ index2 ] )
            index2 += 1
        else: 
            ans.append ( array1 [ index1 ] )
            ans.append ( array2 [ index2 ] )
            index1 += 1
            index2 += 1
            
        if index1 == len( array1 ) :
            while index2 != len ( array2 ) : 
                ans.append ( array2 [ index2 ] )
                index2 += 1
        elif index2 == len ( array2 ) : 
            while index1 != len ( array1 ) : 
                ans.append ( array1 [ index1 ] )
                index1 += 1
                
        if len( ans ) == len ( array1 ) + len ( array2 ) : break
    return ( ans )
    
def separate ( array ) :
    if ( len(array) > 1 ) : 
        middle_index = int( 1 + ( len(array)-1) /2 )
        ans1 = separate ( array [ : middle_index ] )
        ans2 = separate ( array [ middle_index : ] )
        ans = re_arrange ( ans1 , ans2 )
        return ( ans )
    return ( array )
    
array = separate ( array )

for index in range ( 0 , n-k+1 ) :
    temp_sum = 0
    for i in range ( index , index+k-1 ) :
        if array [ i ] == ( array [ i+1 ] +1 ): 
            temp_sum += array [ i ]
            if ( i+2 == index+k ) : temp_sum += array [ i+1 ]
    if temp_sum > max_sum : max_sum = temp_sum
print ( max_sum )}
