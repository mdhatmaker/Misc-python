import QtQuick 2.3
import QtQuick.Controls 2.3

Rectangle {
    id: rect
    width: 250; height: 250

    Button {
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        text: "Change color!"
        onClicked: {
            rect.color = Qt.rgba(Math.random(), Math.random(), Math.random(), 1);
            /*text = "CHANGED!";
            repaint();
            update();
            qApp.processEvents();*/
        }
    }
}

