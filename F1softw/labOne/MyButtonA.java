package F1softw.labOne;

import javax.swing.*;
import java.util.Objects;

public class MyButtonA extends JButton {

    String Colour1 = "Black";
    String Colour2 = "Purple";
    String CurrentColour = Colour1;
    String Text1 = "State 1";
    String Text2 = "State 2";
    String CurrentText = Text1;

    public void main(String[] args) {
        this.setText(Text1);
    }

    public void toggleState() {
        if (Objects.equals(this.CurrentColour, this.Colour1)) {
            this.CurrentColour = Colour2;
            this.CurrentText = Text2;
        } else {
            this.CurrentColour = Colour1;
            this.CurrentText = Text1;
        }
    }

}
