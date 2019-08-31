import QtQuick        2.0
import QtQuick.Window 2.0

Window {
    id: win1;
    width: 320;
    height: 240;
    visible: true;
    color: "yellow";
    title: "First Window";

    Text {
        anchors.centerIn: parent;
        text: "First Window";

        Text {
            id: statusText;
            text: "second window is " + (win2.visible ? "visible" : "invisible");
            anchors.top: parent.bottom;
            anchors.horizontalCenter: parent.horizontalCenter;
        }
    }
    MouseArea {
        anchors.fill: parent;
        onClicked: { win2.visible = !win2.visible; }
    }

    Window {
        id: win2;
        width: win1.width;
        height: win1.height;
        x: win1.x + win1.width;
        y: win1.y;
        color: "green";
        title: "Second Window";

        Rectangle {
            anchors.fill: parent
            anchors.margins: 10

            Text {
                anchors.centerIn: parent
                text: "Second Window"
            }
        }
    }
}