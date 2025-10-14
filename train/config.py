import argparse


def get_config():
    parser = argparse.ArgumentParser(description="Smooth-AP")

    # common settings
    parser.add_argument("--backbone", type=str, default="resnet50_frozen_normalize", help="see _network.py")
    parser.add_argument("--data_dir", type=str, default="../_datasets", help="directory to dataset")
    parser.add_argument("--n_workers", type=int, default=4, help="number of dataloader workers")
    parser.add_argument("--n_epochs", type=int, default=400, help="number of epochs to train for")
    parser.add_argument("--batch_size", type=int, default=224, help="input batch size")
    parser.add_argument("--optimizer", type=str, default="adam", help="sgd/rmsprop/adam/amsgrad/adamw")
    parser.add_argument("--scheduler", type=str, default="step", help="step/none")
    parser.add_argument("--lr", type=float, default=1e-5, help="learning rate")
    parser.add_argument("--wd", type=float, default=4e-4, help="weight decay")
    parser.add_argument("--device", type=str, default="cuda:0", help="device (accelerator) to use")
    parser.add_argument("--parallel-val", type=bool, default=True, help="use a separate thread for validation")

    # changed at runtime
    parser.add_argument("--dataset", type=str, default="cifar", help="cifar/nuswide/flickr/coco")
    parser.add_argument("--n-classes", type=int, default=10, help="number of dataset classes")
    parser.add_argument("--topk", type=int, default=None, help="mAP@topk")
    parser.add_argument("--save-dir", type=str, default="./output", help="directory to output results")
    parser.add_argument("--n-bits", type=int, default=32, help="length of hashing binary")

    # special settings
    parser.add_argument("--gamma", default=0.3, type=float, help="learning rate reduction after tau epochs")
    parser.add_argument(
        "--tau", default=[200, 300], nargs="+", type=int, help="stepsize(s) before reducing learning rate"
    )

    parser.add_argument(
        "--temperature",
        default=0.01,
        type=float,
        help="SmoothAP: the temperature of the sigmoid used in SmoothAP loss",
    )
    args = parser.parse_args()

    # mods
    # args.optimizer = "adam"
    # args.lr = 5e-5

    return args
