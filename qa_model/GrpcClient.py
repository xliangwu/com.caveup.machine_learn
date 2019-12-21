import grpc


def run():
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')


if __name__ == '__main__':
    run()
