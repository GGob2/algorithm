def solution(v):
	
    answer = []
    
    x = v[0][0] ^ v[1][0] ^ v[2][0]
    y = v[0][1] ^ v[1][1] ^ v[2][1]
    
    answer = [x, y]
    
    return answer