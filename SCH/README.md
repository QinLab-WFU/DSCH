# 2024 TPAMI Cross-Modal Hashing Method with Properties of Hamming Space: A New Perspective

[[Paper]](https://ieeexplore.ieee.org/document/10506992)
[[Code]](https://github.com/hutt94/SCH)

# Performance

| Method\Dataset |  cifar   | nuswide  |  flickr  |   coco   |
|:--------------:|:--------:|:--------:|:--------:|:--------:|
|       m1       | 0.847@84 | 0.813@79 | 0.789@59 | 0.654@94 |
|       m2       | 0.682@94 |          |          |          |
|       m3       | 0.827@24 |          |          |          |
|       m4       | 0.152@24 |          |          |          |
|       m5       | 0.833@29 | 0.811@24 | 0.783@54 | 0.646@44 |
|       m6       | 0.859@69 | 0.837@94 | 0.831@84 | 0.681@99 |
|     m7(*)      | 0.872@49 | 0.830@69 | 0.817@59 | 0.686@99 |
|       m8       | 0.863@14 | 0.831@54 | 0.824@79 | 0.694@64 |
|       m9       | 0.866@79 | 0.825@99 | 0.811@74 | 0.664@94 |

# Parameters

```
# same
args.n_bits = 16
args.batch_size = 32
args.n_epochs = 100
```

| Method\Type | backbone                  |  opt  | batch-size |  lr  |  wd  | momentum |
|:-----------:|:--------------------------|:-----:|:----------:|:----:|:----:|:--------:|
|     m1      | resnet50                  |  sgd  |     32     | 5e-3 | 5e-4 |   0.7    |
|     m2      | resnet50_frozen_normalize |  sgd  |     32     | 5e-3 | 5e-4 |   0.7    |
|     m3      | resnet50                  | adam  |     32     | 1e-5 | 4e-4 |    -     |
|     m4      | resnet50                  |  sgd  |    128     | 5e-3 | 5e-4 |   0.7    |
|     m5      | resnet50                  | adam  |    128     | 1e-5 | 4e-4 |    -     |
|     m6      | resnet50_tanh             |  sgd  |     32     | 5e-3 | 5e-4 |   0.7    |
|     m7      | resnet50_tanh+alpha       |  sgd  |     32     | 5e-3 | 5e-4 |   0.7    |
|     m8      | resnet50_tanh+alpha       |  sgd  |     32     | 5e-3 | 5e-4 |   0.9    |
|     m9      | resnet50_tanh+alpha       | adamw |     32     | 2e-6 | 4e-4 |    -     |

- m1: near code default
- m6: near code default + tanh
- m7: near code default + tanh + set_alpha, 16-128's map is better than m8
- m8: near paper