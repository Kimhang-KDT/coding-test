def solution(babbling):
    answer = 0
    
    words = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        for word in words:
            if word in bab:
                bab = bab.replace(word, " ")
                
        if bab.strip() == "":
            answer += 1
            
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
