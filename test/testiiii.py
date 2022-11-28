import test_com
import com


def testcom():
    mock = test_com.spidev_mock()
    communicator = com.SPICom(1,2,mock)
    communicator.openConnection()
    print(f"{communicator.state=}")


def main():
    testcom()


if __name__ == "__main__":
    main()