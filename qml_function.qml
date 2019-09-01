import QtQuick 2.3

Item {
    width: 400
    height: 200
    Rectangle {
        id: rect
        anchors.fill: parent
        color: "blue"
    }

    function printValue(which, value) {
        console.log(which + " = " + value);
    }

    Component.onCompleted: {
        var t0 = new Date();
        for (var i = 0; i < 1000; ++i) {
            var rectColor = rect.color; // resolve the common base.
            printValue("red", rectColor.r);
            printValue("green", rectColor.g);
            printValue("blue", rectColor.b);
            printValue("alpha", rectColor.a);
        }
        var t1 = new Date();
        console.log("Took: " + (t1.valueOf() - t0.valueOf()) + " milliseconds for 1000 iterations");
    }
}