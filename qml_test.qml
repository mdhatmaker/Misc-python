import QtQuick 2.0
//import QtQuick.Controls 1.4


Rectangle {
    width: 200
    height: 100
    color: "red"
    Text {
        anchors.centerIn: parent
        text: "Hello, World!"
    }
    /*TapHandler {
        onTapped: parent.color = "blue"
    }*/
    MouseArea {
        anchors.fill: parent;
        onClicked: { parent.color = "blue"; }
    }

    focus: true
    Keys.onPressed: {
        color = "yellow";
        if (event.key == Qt.Key_Return) {
            color = "blue";
            event.accepted = true;
        }
    }
}
