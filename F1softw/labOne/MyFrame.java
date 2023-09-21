package F1softw.labOne;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

// with code from https://docs.oracle.com/javase/tutorial/uiswing/components/frame.html

public class MyFrame extends JFrame {

    //1. Create the frame.
    static JFrame frame = new JFrame("Simon SN");
    // static JLabel label = new JLabel("Test");


    public static void main(String []args) {

        //2. Optional: What happens when the frame closes?
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 600);

        //4. Size the frame.
        // frame.pack();
        //frame.setBackground(Color.pink);
        frame.getContentPane().setBackground(Color.pink);
        // label.setText("test text");
        frame.setLayout(new BorderLayout());
        frame.add(new JLabel("State 1"), BorderLayout.CENTER);
        frame.add(new JLabel("State 2"), BorderLayout.CENTER);
        frame.pack();


        frame.setVisible(true);
        frame.setLocationRelativeTo(null);

    }

}
