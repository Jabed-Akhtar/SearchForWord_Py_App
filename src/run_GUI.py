"""
 ******************************************************************************
 * @file: run_GUI.py
 * @author: Jabed-Akhtar (Github)
 * @date: 05.09.2022
 *****************************************************************************
 * :Description:
 *
 *
 ******************************************************************************
"""

# Imports
import os, sys
sys.path.append(os.getcwd())
from utils.gui_Widget import *

UI_WinPOS_X = 100  # 1500 #use 0
UI_WinPOS_Y = 100  # use 0
AW = 1925  # Application window width 594
AH = 1000  # Application window height 371
OFFSET_X = 10
WINDOW_TITLE = "Search-For-Word(s)_Py"


class GUI_MainWin(QMainWindow):
    """
    A class used to ---
    ...
    Attributes
    ----------
    says_str : str
        a formatted string to print out ---
    name : str
        the name of the ---
    Methods
    -------
    says(sound=None)
        Prints the ---
    """

    def __init__(self):
        super().__init__()

        # initializations
        self.initUI()
        self.initOthers()

    def initUI(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # adding components to vertical layout (vLayout)
        self.createGUI_menuBar()

        # creating vertical layout for all contents inside GUI
        vLayout = QVBoxLayout()
        self.setLayout(vLayout)

        # configuring GUI-Window
        # self.setGeometry(UI_WinPOS_X, UI_WinPOS_Y, AW, AH)  # 594x371mm is the total size of 7inch display
        self.setWindowTitle(WINDOW_TITLE)
        self.setStyleSheet('background-color: grey;')

        # adding Tab to GUI-Widget
        self.tab_widget = WidgetTab(self)
        self.setCentralWidget(self.tab_widget)
        self.tab_widget.move(0, 20)
        self.tab_widget.setMinimumSize(500, 500)

        # showing the GUI
        #self.showMaximized()  # showing the GUI will maximized size of display
        self.show()

    def initOthers(self):
        """
        :Description:
            here other initialisations, beside the GUIs, are done
        :return: nth
        """
        a_tmp = 0

    def createGUI_menuBar(self):
        """
        :Description:
            here Menu-Bar GUI are to be initialized/created
        :return: nth
        """

        # creating menu var >>>>>
        menuBar = self.menuBar()
        menuBar.setMinimumSize(1000, 25)
        menuBar.setStyleSheet("background-color: green")

        # creating menus >>>>>
        # File menu **********
        fileMenu = QMenu("&File", self)
        fileMenu.setStyleSheet("border-width: 1px;")
        # adding components to file menu
        self.varSaveOut = QAction('save Result as Text')
        fileMenu.addAction(self.varSaveOut)
        self.varExit = QAction('Exit', fileMenu)
        fileMenu.addAction(self.varExit)
        # Setting menu **********
        settingMenu = QMenu("&Settings", self)
        # Help menu **********
        self.helpMenu = QMenu("&Help", self)
        self.menuHelpDoc = self.helpMenu.addAction('Doc')
        self.menuHelpAbt = self.helpMenu.addAction('About SearchForWord_Py')

        # get triggered as soon as menu_button is clicked
        # config.triggered.connect(lambda: self.canInfo_clicked())

        # adding components to menu bar
        menuBar.addMenu(fileMenu)
        menuBar.addMenu(settingMenu)
        menuBar.addMenu(self.helpMenu)
        # menuBar.addMenu(canInfoMenu) # !!! not in use for now

        # adding responses
        # file menu responses
        self.varSaveOut.triggered.connect(lambda: self.on_varSaveOut_clicked())
        self.varExit.triggered.connect(lambda: self.on_Exit_clicked())
        # Help menu responses
        self.menuHelpDoc.triggered.connect(self.on_MenuHelpDoc_clicked)
        self.menuHelpAbt.triggered.connect(self.on_MenuHelpAbt_clicked)


    def on_varSaveOut_clicked(self):
        pass
    
    
    def on_Exit_clicked(self):
        """
        :Description:
            function to be called when the exit option is pressed
        :return: nth
        """

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setWindowTitle("Exit Window")
        msg.setText("Want to exit?")
        msg.setInformativeText("Warning: Result is not saved.")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msg.buttonClicked.connect(msg)

        retval = msg.exec_()
        print(retval)
        if retval==1024:
            self.close()
        else:
            pass

    def on_MenuHelpDoc_clicked(self):
        print("----->>> MenuHelpDoc clicked!")
        msg = QMessageBox()
        msg.setWindowTitle("Doc")
        msg.setText("tbd!")
        x = msg.exec_()

    def on_MenuHelpAbt_clicked(self):
        print("----->>> MenuHelpAbt clicked!")
        msg = QMessageBox()
        msg.setWindowTitle("About this Project")
        msg.setText("tbd!")
        x = msg.exec_()


def main():
    """
    :Description:
        - running App (GUI) (if this file is runned)
    :return: nth
    """

    app = QApplication(sys.argv)
    ex = GUI_MainWin()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


# ****************************** END OF FILE ******************************