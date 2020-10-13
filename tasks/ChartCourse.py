from statistics import mean
from Task import Task


class ChartCourse(Task):

    def __init__(self):
        self.course_x_points = [565, 763, 960, 1157, 1353]
        self.supplements_x = [5, 5, 5, 10]
        self.supplements_y = [10, 10, 10, 60]
        self.y_range = range(270, 810)
        self.identifier_mean = mean((38, 116, 167))
        super().__init__()

    def identify_y_course_point(self, pixels, course_x_point):
        for y in self.y_range:
            pixel = pixels[course_x_point, y]
            #if pixel[0] > 60 or pixel[1] > 165:
            #    return y
            if abs(mean(pixel) - self.identifier_mean) < 10:
                return y

    def drive_course_path(self, path_points):
        assert len(path_points), "[!] Points array is empty: path_points = []"
        self.set_pos(*path_points[0])
        self.click_down()
        for n, xy in enumerate(path_points[1:]):
            self.set_pos(xy[0] + self.supplements_x[n], xy[1] + self.supplements_y[n], .07)
        self.click_up()

    def _solve(self, frame):
        pixels = frame.load()
        course_points = []
        for course_x_point in self.course_x_points:
            course_point = (course_x_point, self.identify_y_course_point(pixels, course_x_point))
            course_points.append(course_point)

        self.drive_course_path(course_points)

        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    chart_course = ChartCourse()
    chart_course.solve()
