import sys

import matplotlib
import pandas as pd
from PySide6 import (
    QtWidgets,
)  # import PySide6 before matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import (
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure

matplotlib.use("QtAgg")


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the maptlotlib FigureCanvasQTAgg object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)

        # Create our pandas DataFrame with some simple
        # data and headers.
        df = pd.DataFrame(
            [
                [0, 10],
                [5, 15],
                [2, 20],
                [15, 25],
                [4, 10],
            ],
            columns=["A", "B"],
        )

        # plot the pandas DataFrame, passing in the
        # matplotlib Canvas axes.
        df.plot(ax=sc.axes)

        # Create toolbar, passing canvas as first parameter, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec()
