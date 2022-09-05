"""
 ******************************************************************************
 * @file: gui_tabWidget.py
 * @author: Jabed-Akhtar
 * @date: 09.03.2022
 *****************************************************************************
 * :Description:
 *
 *
 ******************************************************************************
"""


from utils.import_all import *

global file_path

class WidgetTab(QWidget):
    """
    A class used to represent an ---
    ...
    Attributes
    ----------
    says_str : str
        a formatted string to print out what the ---
    name : str
        the name of the ---
    Methods
    -------
    says(sound=None)
        Prints the ---
    """

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        # configuring Tabs/Groups
        self.confTabs()

        # creating a thread object
        self.thread = {}

        # starting a thread which monitors received CAN msgs
        #self.CANMon_Worker()

    def confTabs(self):
        """
        :Description:
            here all UI/Groups are to be initialized
        :return: nothing
        """

        # creating grid layout to add all groups
        self.layout = QHBoxLayout(self)

        # adding all groups to the grid layout
        #self.layout.addWidget(self.createGUI_IN(), 0, 0, 0, 1) # adding CAN-Monitor group to left side
        #self.layout.addWidget(self.createGUI_TMP(), 0, 1) # adding CAN-Send group to right-top side
        #self.layout.addWidget(self.createGUI_InfoConsole(), 2, 1) # adding CAN-Send group to right-bottom side
        self.layout.addWidget(self.createGUI_IN())
        self.layout.addWidget(self.createGUI_InfoConsole())

        # writting welcome message to InfoConsole
        self.consMsgInfoConsole.setText('---> Programm ready!')

        # setting the grid layout
        self.setLayout(self.layout)

    def createGUI_IN(self):
        """
        :Description:
            ---
        :return: grpBox (QGroupBox)
        """

        # creating a object of QGroupBox
        grpBox = QGroupBox('CAN-Msg-Monitor')
        # configuring Group-Layout
        grpBox.setMinimumWidth(500)
        grpBox.setStyleSheet('background-color: Tan;')

        # definning layout (inside the QGroupBox)
        #vbox = QVBoxLayout()
        self.butSelectFile = QPushButton('Select-File')
        self.selectSeKeyType = QComboBox()
        self.textFromTextKey = QLineEdit()
        self.textFromFile = QPushButton('Select-File')
        self.butRunSearch = QPushButton('Run')
        
        # editing sub-contents
        self.selectSeKeyType.addItems(['--- Select One ---', 'Text(s)', 'From-File'])

        # defnning components ***************
        self.lay_Form = QFormLayout()
        
        self.lay_Form.addRow(QLabel('Select File to search?'), self.butSelectFile)
        self.lay_Form.addRow(QLabel('Text, Texts or From-File'), self.selectSeKeyType)
        self.lay_Form.addRow(QLabel('Text(s)'), self.textFromTextKey)
        self.lay_Form.addRow(QLabel('Select File with searching keywords'), self.textFromFile)
        self.lay_Form.addRow(QLabel('Run Search'), self.butRunSearch)

        # configuring the components added in the group
        #self.lay_Form.setStyleSheet('border: 2px solid black;'
        #                                  'background-color: DarkGray;')
        #self.consMsgMonitor.setContentsMargins(10, 10, 10, 10)

        # setting the vLayout layout to groupLayout
        grpBox.setLayout(self.lay_Form)
        
        self.butSelectFile.clicked.connect(lambda: self.openFileNamesDialog())
        self.selectSeKeyType.currentIndexChanged.connect(self.on_selectSeKeyType_clicked)
        self.textFromFile.clicked.connect(lambda: self.on_selectTextKeyWordFromFile_clicked())
        self.butRunSearch.clicked.connect(lambda: self.on_butRunSearch_clicked())

        # returning the groupLayout
        return grpBox

    def createGUI_InfoConsole(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # creating a object of QGroupBox
        grpBox = QGroupBox('CAN-Msg-Info-Console')
        # configuring Group-Layout
        grpBox.setMinimumWidth(600)
        grpBox.setStyleSheet('background-color: Tan;')

        # definning layout (inside the QGroupBox)
        vbox = QVBoxLayout()

        # defnning components ***************
        self.consMsgInfoConsole = QTextEdit()
        self.consMsgInfoConsole.setReadOnly(True)
        self.consMsgInfoConsole.setText('---> Programm ready CAN-Cons!')

        # configuring the QTextEdit
        self.consMsgInfoConsole.setStyleSheet('border: 1px solid black;'
                                                'background-color: LightGray;')

        # adding components to vLayout
        vbox.addWidget(self.consMsgInfoConsole)
        # vbox.addStretch(1)

        # setting the vLayout layout to groupLayout
        grpBox.setLayout(vbox)

        # returning the groupLayout
        return grpBox
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files[0])
            
        file_path = files[0]
        file_path= "'" + files[0] + "'"
        print(file_path)
            
    def on_selectSeKeyType_clicked(self, i):
        print(i)
        if i==1:
            print('---> Search Keywords from Manual-enter!')
        else:
            print('---> Search Keywords from File!')
            
    def on_selectTextKeyWordFromFile_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files[0])
            
        file_path = files[0]
        file_path= "'" + files[0] + "'"
        print(file_path)

    def on_butRunSearch_clicked(self):
        print('----->>> on_butRunSearch_clicked entered!')
        #self.files = 'test_scripts/gTest_sample.cpp'
        #self.files = files[0]
        print(self.textFromTextKey.text())
        search_str = self.textFromTextKey.text()
        
        r_f = open(file_path)
        lines_r_f = r_f.readlines()
        
        self.consMsgInfoConsole.append('----->>> Keywords found:')
        
        for n_line, lines in enumerate(lines_r_f):
            #print('----->>> Check-1')
            lines = lines.strip()
            #print(lines)
            if search_str in lines:
                #print('----->>> Check-2')
                print(search_str)
                print(n_line+1)
                #CANMon_writeToGUI(search_str)
                str_msg = ':-> ' + 'Keyword: ' + str(search_str) + '  --  ' + 'File: ' + self.files + '  --  ' + 'Line: ' + str(n_line+1)
                self.consMsgInfoConsole.append(str_msg)
        
        self.consMsgInfoConsole.append('-----<<<')
        self.consMsgInfoConsole.append('\n')


class A_Thread(QThread):
    """
    :Description:
        - a class with thread (QThread)
        - here a thread will run and wait for incoming CAN-Messages
    :return: msg (incoming CAN-Messages)
    """

    # defining a signal (object) to store incoming CAN-Messages
    any_signal = pyqtSignal(object)

    def __init__(self, parent=None, index=0):
        super(A_Thread, self).__init__(parent)
        self.index = index
        self.is_running = True

    def run(self):
        print('Starting thread...', self.index)
        # while loop to keep waiting for incoming CAN-Messages
        while (True):
            msg = canUt.CANMonitor()
            print(msg.data)
            # sending out receinved CAN-Messages
            self.any_signal.emit(msg)

    def stop(self):
        self.is_running = False
        print('Stopping thread...', self.index)
        self.terminate()


if __name__ == '__main__':
    main()


# ****************************** END OF FILE ******************************