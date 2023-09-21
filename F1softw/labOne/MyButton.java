package F1softw.labOne;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Objects;

public class MyButton extends JButton implements ActionListener {


    static JFrame frame = new JFrame("Simon SN");
    // frame.getContentPane().setBackground(Color.pink);
    static JButton button1 = new JButton("State 1");
    // , new ImageIcon("nomi2.png")
    static JButton button2 = new JButton("State 2");

    // static int state1 = 0;  // Zero represents ground state, One excited state.
    // static int state2 = 1;  // Zero represents ground state, One excited state.

    public static void main(String []args) {

        button1.addActionListener(new MyButton());
        button2.addActionListener(new MyButton());

        frame.setLayout(new BorderLayout());
        Icon icon = new ImageIcon("nomi2.png");
        JLabel label = new JLabel(icon);
        frame.add(label);

        // frame.getContentPane().setBackground(Color.black);
        // frame.add(new JLabel("State 1"), BorderLayout.CENTER);
        // frame.setSize(600, 600);
        button1.setSize(100 , 80);
        button1.setLocation(80 , 150);
        button1.setBackground(Color.blue);
        label.add(button1);
        button2.setSize(100 , 80);
        button2.setLocation(360 , 150);
        button2.setBackground(Color.red);
        label.add(button2);
        frame.pack();

        // toggleState(button1, state1);
        // toggleState(button2, state2);

        // frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);


    }

    public static void toggleState(JButton button) {

        if (Objects.equals(button.getText(), "State 1")) {
            // state = 1;
            // frame.getContentPane().setBackground(Color.red);
            button.setBackground(Color.red);
            // frame.add(new JLabel("State 1"), BorderLayout.CENTER);
            button.setText("State 2");
        } else {
            // state = 0;
            // frame.getContentPane().setBackground(Color.blue);
            button.setBackground(Color.blue);
            // frame.add(new JLabel("State 2"), BorderLayout.CENTER);
            button.setText("State 1");
        }

    }

    //@Override
    //public void actionPerformed(ActionEvent e) {
    //    MyButton.toggleState(e.getSource());
    //}

    // gpt save... kinda not :(
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == button1) {
            toggleState(button1);
        } else if (e.getSource() == button2) {
            toggleState(button2);
        }
    }


}
