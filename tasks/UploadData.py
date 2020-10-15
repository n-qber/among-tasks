from .DownloadData import DownloadData


class UploadData(DownloadData):
    pass


if __name__ == '__main__':
    upload_data = UploadData()
    upload_data.solve()
