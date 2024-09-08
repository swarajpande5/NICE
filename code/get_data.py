import torchvision


def get_data():
    print("Downloading CIFAR10...")
    torchvision.datasets.CIFAR10(root="./datasets/cifar", train=True, download=True)
    print("Downloading SVHN...")
    torchvision.datasets.SVHN(root="./datasets/svhn", split='train', download=True)
    print("Downloading MNIST...")
    torchvision.datasets.MNIST(root="./datasets/mnist", train=True, download=True)

    print("...All done.")


if __name__ == '__main__':
    get_data()
