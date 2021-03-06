# -*- coding: utf-8 -*-


from PyQt4.QtGui import QApplication

from converterpages import (LoadFilePage, CustomInputHeaderPage,
                            HeaderOrderPage, CustomColumnNamesPage,
                            ColorPatternPage, ChangeStylePage, SaveFilePage)
from wizutils import OdmltablesWizard

from settings import Settings


class ConversionWizard(OdmltablesWizard):
    NUM_PAGES = 7

    (PageLoadFile, PageCustomInputHeader, PageHeaderOrder, PageCustomColumNames,
     PageColorPattern, PageChangeStyle, PageSaveFile) = range(NUM_PAGES)

    def __init__(self, parent=None):
        super(ConversionWizard, self).__init__('Conversion Wizard', parent)
        settings = Settings(self.settingsfile)

        self.setPage(self.PageLoadFile, LoadFilePage(settings))
        self.setPage(self.PageCustomInputHeader,
                     CustomInputHeaderPage(settings))
        self.setPage(self.PageHeaderOrder, HeaderOrderPage(settings))
        self.setPage(self.PageCustomColumNames, CustomColumnNamesPage(settings))
        self.setPage(self.PageColorPattern, ColorPatternPage(settings))
        self.setPage(self.PageChangeStyle, ChangeStylePage(settings))
        self.setPage(self.PageSaveFile, SaveFilePage(settings))

    def _createHelpMsgs(self):
        msgs = {}
        msgs[self.PageLoadFile] = self.tr(
                "Select an input file using the browser"
                " and choose your output file format.")
        msgs[self.PageCustomInputHeader] = self.tr(
                "You need to assign the header "
                " titles used in the input file "
                " to valid odml column types.")
        msgs[self.PageHeaderOrder] = self.tr("Select the headers you want be"
                                             " present in the output table. "
                                             " You need to select at least "
                                             " 'Path to Section', 'Property "
                                             "Name',"
                                             " 'Value' and 'odML Data Type' "
                                             "to be"
                                             " able to convert the table back "
                                             "into "
                                             " an odml file.")
        msgs[self.PageCustomColumNames] = self.tr(
                "Select the colums you want to "
                "have in the final table and move them to "
                "the right list using the central "
                "buttons. You can adjust the order "
                "of the columns using the buttons "
                "to the right.")
        msgs[self.PageColorPattern] = self.tr(
                "Select a pattern used for better "
                "visualization of you table.")
        msgs[self.PageChangeStyle] = self.tr("Select change the style of the "
                                             "different cell schemes by "
                                             "clicking "
                                             "on a cell and changing its "
                                             "properties "
                                             "using the settings at the right.")
        msgs[self.PageSaveFile] = self.tr("Select a location to save your "
                                          "file by clicking on the browse "
                                          "button.")
        msgs[self.NUM_PAGES + 1] = self.tr(
                "Sorry, for this page there is no help available.")
        return msgs


# main ========================================================================
def main():
    import sys

    app = QApplication(sys.argv)
    wiz = ConversionWizard()
    wiz.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
