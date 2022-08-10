'''
 ******************************************************************************
 * @file: main.py
 * @author: Jabed-Akhtar
 * @date: 09.03.2022
 *****************************************************************************
 * Description:
 * 
 * 
 ******************************************************************************
'''

# imports
from ir_gui import *

def main():
    """
    :Description:
        - running App (GUI)
    :return: nothing
    """

    app = QApplication(sys.argv)
    ex = GUI_MainWin()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

# ****************************** END OF FILE ******************************