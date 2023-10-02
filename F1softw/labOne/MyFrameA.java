package F1softw.labOne;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MyFrameA extends JFrame implements ActionListener {

    static JFrame frame = new JFrame("Simon SN");
    static MyButtonA button1 = new MyButtonA();
    static MyButtonA button2 = new MyButtonA();

    public static void main(String []args) {
        button1.addActionListener(new MyButtonA());
        button2.addActionListener(new MyButtonA());

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());
        Icon icon = new ImageIcon("nomi2.png");
        JLabel label = new JLabel(icon);
        frame.add(label);

        // frame.getContentPane().setBackground(Color.black);
        frame.setSize(600, 600);
        button1.setSize(100 , 80);
        button1.setLocation(80 , 150);
        button1.setBackground(Color.blue);
        label.add(button1);
        button2.setSize(100 , 80);
        button2.setLocation(360 , 150);
        button2.setBackground(Color.red);
        label.add(button2);
        frame.pack();

        frame.setVisible(true);
        frame.setLocationRelativeTo(null);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
            e.getSource().toggleState();
        }
}
