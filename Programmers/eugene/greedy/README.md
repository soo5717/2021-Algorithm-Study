# [Programmers-42860] 조이스틱

## 접근 방식

조이스틱 이동 횟수를 구하려면 변경할 위치로 이동하는 과정과 이동 후 알파벳을 변경하는 과정이 필요하다. 
<br>또한 Greedy 주제에 맞게 "현재 상황에서 가장 좋은 선택"을 하는 방법을 생각하면 과정을 어렵지 않다.

#### _STEP1. 알파벳 변경 횟수(위, 아래 방향키)_

##### 현재 있는 위치의 문자가 A가 아닌 경우 알파벳을 변경해줘야 한다. <br> A부터 시작하는 경우와 뒤로 돌아가 Z부터 시작하는 두 가지 방법 중 더 적게 이동하는 방법을 선택해 answer에 추가한다.<br><br> 아스키 코드로 해당 문자와 A와의 차이를 구하는 방식으로 알파벳 변경을 위한 최소 이동 횟수를 구해주면 된다. 
```
        if name[i] != 'A': 
            answer+=min(ord(name[i]) - ord('A'), ord('Z')-ord(name[i])+1)
```
#### _STEP2. 커서 이동 횟수(왼쪽, 오른쪽 방향키)_

##### A가 아닌 위치로 가서 변경을 하기 위해 해당 위치로 이동해주어야 한다. <br>현재 위치에서 A가 아닌 문자가 더 가까운 방향으로 이동한다.
```
        for k in range(1,len(name)):
            if name[i+k]=="A": right+=1
            else : break 
            
            if name[i-k]=="A" : left+=1               
            else: break
            
        if left<right:
            answer+=left
            i-=left
        else:
            answer+=right
            i+=right
```
#### _STEP3. 종료_
##### 1) step1에서 문자를 변경하고 해당 위치의 문자를 A로 바꿔준다. <br> 2) 주어진 name이 모두 A로 변하면 더 이상 이동하지 않아도 되므로 종료한다.
```
        name[i] = 'A'
        if ['A'] * len(name) == name:
            break
```

## 완성 코드와 실행시간
```
def solution(name):
    answer,i = 0,0
    name=list(name)
    
    while(True):
        left, right =1,1

        if name[i] != 'A': 
            answer+=min(ord(name[i]) - ord('A'), ord('Z')-ord(name[i])+1 )   
    
        name[i] = 'A'
        if ['A'] * len(name) == name:
            break
            
        #커서 이동 카운트
        for k in range(1,len(name)):
            if name[i+k]=="A": right+=1
            else : break
                
            if name[i-k]=="A" : left+=1               
            else: break
        
        #left/right 중 더 가까운 방향으로 이동        
        if left<right:
            answer+=left
            i-=left
        else:
            answer+=right
            i+=right
    return answer
```
  <img width="266" alt="joystick_result" src="https://user-images.githubusercontent.com/54016224/111744040-ec5b1f00-88cd-11eb-8e51-619f32433332.png">
