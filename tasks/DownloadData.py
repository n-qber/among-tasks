from Task import Task


class DownloadData(Task):

    def __init__(self):
        self.download_position = (960, 660)
        super().__init__()

    def _solve(self, frame):
        self.set_pos(*self.download_position)
        self.sleep(.1)
        self.click()
        self.sleep(10.5)
        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    download_data = DownloadData()
    download_data.solve()
