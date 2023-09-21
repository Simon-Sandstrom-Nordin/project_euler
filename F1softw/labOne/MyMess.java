package F1softw.labOne;

import javax.swing.*;
import java.awt.*;

public abstract class MyMess extends JButton {

    // static JFrame frame = new JFrame("State 1");
    // frame.getContentPane().setBackground(Color.pink);
    static JFrame frame = new JFrame("Simon SN");
    static int state = 0;  // Zero represents ground state, One excited state.

    public static void main(String []args) {

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 600);
        frame.getContentPane().setBackground(Color.blue);
        frame.setLayout(new BorderLayout());
        frame.add(new JLabel("State 1"), BorderLayout.CENTER);
        frame.pack();

        toggleState();

        frame.setVisible(true);
        frame.setLocationRelativeTo(null);

    }

    private static void toggleState() {

        if (state == 0) {
            state = 1;
            frame.getContentPane().setBackground(Color.red);
            frame.add(new JLabel("State 1"), BorderLayout.CENTER);
        } else {
            state = 0;
            frame.getContentPane().setBackground(Color.blue);
            frame.add(new JLabel("State 2"), BorderLayout.CENTER);
        }

    }

}

