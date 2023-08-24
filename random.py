import random

# 블록 모양을 정의한 리스트
block_shapes = [
    [[1, 1, 1, 1]],  # I 블록
    [[1, 1, 1], [1, 0, 0]],  # L 블록
    [[1, 1, 1], [0, 0, 1]],  # J 블록
    [[1, 1, 1], [0, 1, 0]],  # T 블록
    [[0, 1, 1], [1, 1, 0]],  # S 블록
    [[1, 1, 0], [0, 1, 1]],  # Z 블록
    [[1, 1, 0], [1, 1, 0]],  # O 블록
]

class Tetromino:
    def __init__(self, block_type):
        self.block_type = block_type
        self.rotation = 0

# 블록 타입 상수 정의
I_BLOCK = 0
L_BLOCK = 1
J_BLOCK = 2
T_BLOCK = 3
S_BLOCK = 4
Z_BLOCK = 5
O_BLOCK = 6

def GenerateRandomBlock():
    random_block_type = random.choice([I_BLOCK, L_BLOCK, J_BLOCK, T_BLOCK, S_BLOCK, Z_BLOCK, O_BLOCK])
    return Tetromino(random_block_type)

# 블록 타입과 색상 매핑
block_color_mapping = {
    I_BLOCK: "cyan",
    L_BLOCK: "orange",
    J_BLOCK: "blue",
    T_BLOCK: "purple",
    S_BLOCK: "green",
    Z_BLOCK: "red",
    O_BLOCK: "yellow",
}

# 세트에 사용할 블록 타입들을 리스트로 정의
block_type_set = [I_BLOCK, L_BLOCK, J_BLOCK, T_BLOCK, S_BLOCK, Z_BLOCK, O_BLOCK]

# 한 세트에서 7개의 블록이 모두 다른 블록 타입으로 뽑힐 때까지 반복
while block_type_set:
    
    selected_block_types = []
    while len(selected_block_types) < len(block_type_set):
        # 무작위 블록 생성
        random_block = GenerateRandomBlock()
        random_block_type = random_block.block_type
        
        if random_block_type not in selected_block_types:
            selected_block_types.append(random_block_type)
            print("Random Block Type:", random_block.block_type)
            print("Block Color:", block_color_mapping[random_block.block_type])
    