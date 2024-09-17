import itertools

INITIAL_CONVS = [
    ([1,64,230,230], [3,64,7,7], 2, [1,3,112,112], "f32", "f32"),
    ([1,64,58,58], [64,64,3,3], 1, [1,64,56,56], "f32", "f32"),
    ([1,128,58,58], [128,128,3,3], 2, [1,128,28,28], "f32", "f32"),
    ([1,512,56,56], [256,512,1,1], 2, [1,256,28,28], "f32", "f32"),
    ([1,128,30,30], [128,128,3,3], 1, [1,128,28,28], "f32", "f32"),
    ([1,256,30,30], [256,256,3,3], 2, [1,256,14,14], "f32", "f32"),
    ([1,1024,28,28], [512,1024,1,1], 2, [1,512,14,14], "f32", "f32"),
    ([1,256,16,16], [256,256,3,3], 1, [1,256,14,14], "f32", "f32"),
    ([1,512,16,16], [512,512,3,3], 2, [1,512,7,7], "f32", "f32"),
    ([1,2048,14,14], [1024,2048,1,1], 2, [1,1024,7,7], "f32", "f32"),
    ([1,512,9,9], [512,512,3,3], 1, [1,512,7,7], "f32", "f32"),
]

def conv(configs):
    configs.extend(INITIAL_CONVS)
