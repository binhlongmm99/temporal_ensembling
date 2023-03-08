import numpy as np

def main():
    # print("Hello World!")
    data_to_path = './data/cifar10.npz'
    data = np.load(data_to_path)
    print(data.files)
    print(data["images"].shape)
    print(data["labels"].shape)

    print(type(data["images"]))
    train_x = data["images"][:6000, ]
    print(train_x.shape)
    # data['train_x'], data['test_x'] = data["images"][:6000, ], data["images"][6000:, ]
    # data['train_y'], data['test_y'] = data["labels"][6000:, ]

if __name__ == '__main__':
    main()