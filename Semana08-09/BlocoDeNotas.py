// ---------- HelloWorld ----------
 
I. First Program
 
1. New Project (File | New File or Project)
2. Qt Widgets Application
3. Set Project Name, Project Directory and Default Project Location
4. Select Desktop Qt kit
5. Leave class names as default
6. Finish
7. Click mainwindow.ui under Forms
8. Drag a Label out and change the text to Hello World
9. Click Run in bottom left hand corner
 
II. Interface
 
1. Widget Box : Contains all widgets you can drag into the Form Editor
2. Form Toolbar : is above the Form Editor : Click on different layouts
3. Object Inspector : Lists all current Widgets
4. Property Editor : Change properties of currently selected Widget
5. Action Editor : Create actions associated with your toolbars and menubars
6. Output Pane : At very bottom, provides information for debugging
 
// ---------- END HelloWorld ----------
 
// ---------- WIDGETS ----------
 
I. Layouts : Provide structure and a common look
 
1. Vertical : layout widgets in columns from top to bottom
2. Horizontal : layout in rows from left to right
3. Grid : layout in 2 dimensional grid in which widgets can take up more then 1 cell
4. Form : layout in a 2 column style
 
// ---------- END WIDGETS ----------
 
// ---------- STYLE SHEETS ----------
 
// Stylesheets in Qt are similar to CSS
// Stylesheets can be changed by your code, the properties editor, or
// by right clicking a widget and then selecting Change stylesheet
 
// To change styling on a layout, select it in the Object Inspector and
// then Right click -> Morph into -> QFrame
 
// ---------- END STYLE SHEETS ----------
 
// ---------- NOTEPAD.PRO ----------
 
# Add printing support
QT       += core gui printsupport
 
// ---------- END NOTEPAD.PRO ----------
 
// ---------- NOTEPAD.H ----------
 
#ifndef NOTEPAD_H
#define NOTEPAD_H
 
// Provides the main application window on which the user interface
// is built by adding widgets
#include <QMainWindow>
 
#include <QFile>
#include <QFileDialog>
#include <QTextStream>
#include <QMessageBox>
#include <QPrinter>
#include <QPrintDialog>
 
// Use the standard UI namespace which is tied to the .ui file
namespace Ui {
class Notepad;
}
 
class Notepad : public QMainWindow
{
    // Declares our class as a QObject which is the base class
    // for all Qt objects
    // QObjects handle events
    // Each QObject executes on a thread
    Q_OBJECT
 
public:
 
    // Declare a constructor and by passing 0 we state this widget
    // has no parent
    explicit Notepad(QWidget *parent = 0);
 
    // Declare a destructor which will free resources
    ~Notepad();
 
private slots:
    void on_actionNew_triggered();
 
    void on_actionOpen_triggered();
 
    void on_actionSave_as_triggered();
 
    void on_actionPrint_triggered();
 
    void on_actionExit_triggered();
 
    void on_actionSave_triggered();
 
    void on_actionCopy_triggered();
 
    void on_actionCut_triggered();
 
    void on_actionPaste_triggered();
 
    void on_actionUndo_triggered();
 
    void on_actionRedo_triggered();
 
private:
 
    // Point to the ui class
    Ui::Notepad *ui;
 
    // A Qt character string that will hold text entered by the user
    QString currentFile = "";
};
 
#endif // NOTEPAD_H
 
// ---------- END NOTEPAD.H ----------
 
// ---------- MAIN.CPP ----------
 
#include "notepad.h"
 
// Handles widgets, event handling, mouse, windows look and feel
#include <QApplication>
 
// Where execution begins
int main(int argc, char *argv[])
{
    // Creates the application object
    QApplication a(argc, argv);
 
    // Create the main application object and display it on screen
    Notepad w;
    w.show();
 
    // Puts the application into a loop in which events are handled
    return a.exec();
}
 
// ---------- END MAIN.CPP ----------
 
// ---------- NOTEPAD.CPP ----------
 
#include "notepad.h"
#include "ui_notepad.h"
 
// The Notepad constructor
Notepad::Notepad(QWidget *parent) :
 
    // Call the QMainWindow constructor
    QMainWindow(parent),
 
    // Create the UI class and assign it to the ui member
    ui(new Ui::Notepad)
{
    // Setup the UI
    ui->setupUi(this);
 
    // Have the textedit widget take up the whole window
    this->setCentralWidget(ui->textEdit);
}
 
// Destructor that deletes the UI
Notepad::~Notepad()
{
    delete ui;
}
 
// We can type in commands on our menubar which will then appear in
// the Action Editor.
// Right click the Action -> Go to slot -> Triggered -> Add code for the event
 
// With Qt objects communicate in a different way from other frameworks
 
// Most frameworks handle an event by creating a function that processes
// events by calling other functions when an event occurs
 
// With Qt widgets issue a Signal when an event occurs and specific
// Slots (functions) are called in response to the signal
 
// ----- ADDING ICONS TO TOOLBAR & MENU -----
 
// 1. Add Resource Folder : Right Click Project -> Add New ->
// Qt -> Qt Resource File -> Name : Resources Path: Folder
 
// 2. Add Icons to Resource Folder : Select resource file ->
// Add Prefix -> /imgs -> Add Files -> Select icons
 
// 3. Add Icons to File Menu : Right click item in Action Editor ->
// Choose Resource -> Select Icon -> Click to show image
 
// 4. Add items to the toolbar by dragging from the Action
// Editor to the toolbar
 
// ----- END ADDING ICONS TO TOOLBAR & MENU -----
 
void Notepad::on_actionNew_triggered()
{
    // Global referencing the current file that we are clearing
    currentFile.clear();
 
    // Clear the textEdit widget buffer
    ui->textEdit->setText(QString());
}
 
void Notepad::on_actionOpen_triggered()
{
    // Opens a dialog that allows you to select a file to open
    QString fileName = QFileDialog::getOpenFileName(this, "Open the file");
 
    // An object for reading and writing files
    QFile file(fileName);
 
    // Store the currentFile name
    currentFile = fileName;
 
    // Try to open the file as a read only file if possible or display a
    // warning dialog box
    if (!file.open(QIODevice::ReadOnly | QFile::Text)) {
        QMessageBox::warning(this, "Warning", "Cannot open file: " + file.errorString());
        return;
    }
 
    // Set the title for the window to the file name
    setWindowTitle(fileName);
 
    // Interface for reading text
    QTextStream in(&file);
 
    // Copy text in the string
    QString text = in.readAll();
 
    // Put the text in the textEdit widget
    ui->textEdit->setText(text);
 
    // Close the file
    file.close();
}
 
void Notepad::on_actionSave_as_triggered()
{
    // Opens a dialog for saving a file
    QString fileName = QFileDialog::getSaveFileName(this, "Save as");
 
    // An object for reading and writing files
    QFile file(fileName);
 
    // Try to open a file with write only options
    if (!file.open(QFile::WriteOnly | QFile::Text)) {
        QMessageBox::warning(this, "Warning", "Cannot save file: " + file.errorString());
        return;
    }
 
    // Store the currentFile name
    currentFile = fileName;
 
    // Set the title for the window to the file name
    setWindowTitle(fileName);
 
    // Interface for writing text
    QTextStream out(&file);
 
    // Copy text in the textEdit widget and convert to plain text
    QString text = ui->textEdit->toPlainText();
 
    // Output to file
    out << text;
 
    // Close the file
    file.close();
}
 
void Notepad::on_actionSave_triggered()
{
    QString fileName = QFileDialog::getSaveFileName(this, "Save");
    QFile file(fileName);
    if (!file.open(QFile::WriteOnly | QFile::Text)) {
        QMessageBox::warning(this, "Warning", "Cannot save file: " + file.errorString());
        return;
    }
    currentFile = fileName;
    setWindowTitle(fileName);
    QTextStream out(&file);
    QString text = ui->textEdit->toPlainText();
    out << text;
    file.close();
}
 
void Notepad::on_actionPrint_triggered()
{
    // Allows for interacting with printer
    QPrinter printer;
 
    // You'll put your printer name here
    printer.setPrinterName("Printer Name");
 
    // Create the print dialog and pass the name and parent
    QPrintDialog pDialog(&printer, this);
 
    if(pDialog.exec() == QDialog::Rejected){
        QMessageBox::warning(this, "Warning", "Cannot Access Printer");
        return;
    }
 
    // Send the text to the printer
    ui->textEdit->print(&printer);
 
}
 
void Notepad::on_actionExit_triggered()
{
    QApplication::quit();
}
 
 
void Notepad::on_actionCopy_triggered()
{
    ui->textEdit->copy();
}
 
void Notepad::on_actionCut_triggered()
{
    ui->textEdit->cut();
}
 
void Notepad::on_actionPaste_triggered()
{
    ui->textEdit->paste();
}
 
void Notepad::on_actionUndo_triggered()
{
    ui->textEdit->undo();
}
 
void Notepad::on_actionRedo_triggered()
{
    ui->textEdit->redo();
}
 
// ---------- END NOTEPAD.CPP ----------