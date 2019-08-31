import QtQuick 2.12

Rectangle {
    width: 200
    height: 100
    color: "red"

    Text {
        anchors.centerIn: parent
        text: "Hello, World!"
    }

    TapHandler {
        onTapped: parent.color = "blue"
    }
}