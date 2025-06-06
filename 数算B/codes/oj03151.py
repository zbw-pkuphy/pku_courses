import sys
from collections import deque

def main():
    A, B, C = map(int, sys.stdin.readline().split())

    def bfs():
        visited = set()
        queue = deque()
        queue.append(((0, 0), []))  # 初始状态和路径
        visited.add((0, 0))
        
        while queue:
            (a, b), path = queue.popleft()
            # 检查是否达到目标状态
            if a == C or b == C:
                return path
            
            # 生成所有可能的下一步操作
            # 操作：FILL(1) 填满第一个水壶
            new_state = (A, b)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [f"FILL(1)"]))
            
            # 操作：FILL(2) 填满第二个水壶
            new_state = (a, B)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [f"FILL(2)"]))
            
            # 操作：DROP(1) 倒空第一个水壶
            new_state = (0, b)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [f"DROP(1)"]))
            
            # 操作：DROP(2) 倒空第二个水壶
            new_state = (a, 0)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [f"DROP(2)"]))
            
            # 操作：POUR(1,2) 从第一个水壶向第二个水壶倒水
            pour = min(a, B - b)
            new_state = (a - pour, b + pour)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [f"POUR(1,2)"]))
            
            # 操作：POUR(2,1) 从第二个水壶向第一个水壶倒水
            pour = min(b, A - a)
            new_state = (a + pour, b - pour)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [f"POUR(2,1)"]))
        
        # 如果无法达到目标状态
        return None

    path = bfs()
    if path is None:
        print("impossible")
    else:
        print(len(path))
        for op in path:
            print(op)

if __name__ == "__main__":
    main()